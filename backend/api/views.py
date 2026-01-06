from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
import os
import re
from openai import OpenAI

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def extract_relevant_sentences(page_text, question, max_sentences=12, min_score=2):
    sentences = re.split(r'(?<=[.!?])\s+', page_text)
    question_words = set(
        word.lower() for word in re.findall(r"\w+", question) if len(word) > 3
    )

    scored = []
    for s in sentences:
        s_words = set(re.findall(r"\w+", s.lower()))
        score = len(question_words & s_words)
        if score >= min_score:
            scored.append((score, s.strip()))

    scored.sort(reverse=True)
    return [s for _, s in scored[:max_sentences]]

@csrf_exempt
def answer_question(request):
    if request.method != "POST":
        return JsonResponse({"error": "Invalid request"}, status=400)

    data = json.loads(request.body)
    question = data.get("question", "")
    page_text = data.get("page_text", "")

    if not question or not page_text:
        return JsonResponse({"answer": "Not enough information to answer."})

    relevant_sentences = extract_relevant_sentences(page_text, question)

    if not relevant_sentences:
        return JsonResponse({
            "answer": "This question can’t be answered using the content of the current page.",
            "sources": []
        })

    context = "\n".join(relevant_sentences)

    prompt = f"""Answer the question using ONLY the information below.
            Be concise and factual.

            Context:
            {context}

            Question:
            {question}
            """

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.2,
    )

    answer = response.choices[0].message.content.strip()

    return JsonResponse({
        "answer": answer,
        "sources": relevant_sentences
    })
