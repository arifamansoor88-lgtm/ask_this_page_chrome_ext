document.getElementById("askBtn").addEventListener("click", async () => {
  const question = document.getElementById("questionInput").value;
  const answerBox = document.getElementById("answerBox");
  answerBox.textContent = "Thinking...";

  const [tab] = await chrome.tabs.query({ active: true, currentWindow: true });

  chrome.tabs.sendMessage(tab.id, { type: "GET_PAGE_TEXT" }, async (response) => {
    if (!response || !response.text) {
      answerBox.textContent = "Could not read page content.";
      return;
    }

    const res = await fetch("http://127.0.0.1:8000/api/answer/", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({
        question,
        page_text: response.text,
      }),
    });

    const data = await res.json();

    let html = `<strong>Answer</strong><br>${data.answer || "No answer"}<br><br>`;

    if (data.sources && data.sources.length) {
      html += `<strong>From this page:</strong><ul>`;
      data.sources.slice(0, 3).forEach(s => {
        html += `<li>${s}</li>`;
      });
      html += `</ul>`;
    }

    answerBox.innerHTML = html;
  });
});
