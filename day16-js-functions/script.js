/* Day 16 — JavaScript functions and cleaner app logic */

const form = document.getElementById("postForm");
const titleInput = document.getElementById("title");
const bodyInput = document.getElementById("body");
const submitBtn = document.getElementById("submitBtn");
const clearBtn = document.getElementById("clearBtn");
const statusText = document.getElementById("status");
const output = document.getElementById("output");

const resultSection = document.getElementById("resultSection");
const resultTitle = document.getElementById("resultTitle");
const resultBody = document.getElementById("resultBody");
const resultId = document.getElementById("resultId");

const titleError = document.getElementById("titleError");
const bodyError = document.getElementById("bodyError");

function clearFieldErrors() {
  titleError.textContent = "";
  bodyError.textContent = "";
  titleInput.removeAttribute("aria-invalid");
  bodyInput.removeAttribute("aria-invalid");
}

function validateForm(title, body) {
  let hasError = false;

  if (title === "") {
    titleError.textContent = "Please enter a post title.";
    titleInput.setAttribute("aria-invalid", "true");
    hasError = true;
  }

  if (body === "") {
    bodyError.textContent = "Please enter post content.";
    bodyInput.setAttribute("aria-invalid", "true");
    hasError = true;
  }

  return hasError;
}

function clearResults() {
  statusText.textContent = "";
  output.textContent = "";
  resultSection.hidden = true;
  resultTitle.textContent = "";
  resultBody.textContent = "";
  resultId.textContent = "";
}

function buildPayload(title, body) {
  return {
    title: title,
    body: body,
    userId: 1
  };
}

function displaySuccess(data, responseStatus) {
  resultTitle.textContent = data.title;
  resultBody.textContent = data.body;
  resultId.textContent = data.id;
  resultSection.hidden = false;

  statusText.textContent =
    `Practice request succeeded. HTTP status: ${responseStatus}`;

  output.textContent = JSON.stringify(data, null, 2);
}

function displayError(error) {
  statusText.textContent = `Error: ${error.message}`;
  console.error(error);
}

form.addEventListener("submit", async (event) => {
  event.preventDefault();

  const title = titleInput.value.trim();
  const body = bodyInput.value.trim();

  clearResults();
  clearFieldErrors();

  const hasError = validateForm(title, body);

  if (hasError) {
    statusText.textContent = "Please correct the highlighted fields.";
    return;
  }

  const payload = buildPayload(title, body);

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

    displaySuccess(data, response.status);
  } catch (error) {
    displayError(error);
  } finally {
    submitBtn.disabled = false;
  }
});

clearBtn.addEventListener("click", () => {
  if (submitBtn.disabled) {
    return;
  }

  titleInput.value = "";
  bodyInput.value = "";

  clearResults();
  clearFieldErrors();

  titleInput.focus();
});