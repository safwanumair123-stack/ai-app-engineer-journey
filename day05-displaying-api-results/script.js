const form = document.getElementById("postForm");
const titleInput = document.getElementById("title");
const bodyInput = document.getElementById("body");
const submitBtn = document.getElementById("submitBtn");
const statusText = document.getElementById("status");
const output = document.getElementById("output");

const resultSection = document.getElementById("resultSection");
const resultTitle = document.getElementById("resultTitle");
const resultBody = document.getElementById("resultBody");
const resultId = document.getElementById("resultId");

form.addEventListener("submit", async (event) => {
  event.preventDefault();

  const title = titleInput.value.trim();
  const body = bodyInput.value.trim();

  statusText.textContent = "";
  output.textContent = "";

  resultSection.hidden = true;
  resultTitle.textContent = "";
  resultBody.textContent = "";
  resultId.textContent = "";

  if (!title || !body) {
    statusText.textContent = "Please enter both a title and content.";
    return;
  }

  const payload = {
    title: title,
    body: body,
    userId: 1
  };

  submitBtn.disabled = true;
  statusText.textContent = "Sending...";

  try {
    const response = await fetch(
      "https://jsonplaceholder.typicode.com/posts",
      {
        method: "POST",
        headers: {
          "Content-Type": "application/json"
        },
        body: JSON.stringify(payload)
      }
    );

    if (!response.ok) {
      throw new Error(`Request failed: ${response.status}`);
    }

    const data = await response.json();

    resultTitle.textContent = data.title;
    resultBody.textContent = data.body;
    resultId.textContent = data.id;
    resultSection.hidden = false;

    statusText.textContent =
      `Practice request succeeded. HTTP status: ${response.status}`;

    output.textContent = JSON.stringify(data, null, 2);
  } catch (error) {
    statusText.textContent = `Error: ${error.message}`;
    console.error(error);
  } finally {
    submitBtn.disabled = false;
  }
});