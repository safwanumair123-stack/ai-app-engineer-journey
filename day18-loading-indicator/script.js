/* Day 18 — Loading indicator and submit button state */

const form = document.getElementById("postForm");
const titleInput = document.getElementById("title");
const bodyInput = document.getElementById("body");
const submitBtn = document.getElementById("submitBtn");
const clearBtn = document.getElementById("clearBtn");
const statusText = document.getElementById("status");
const spinner = document.getElementById("spinner");
const output = document.getElementById("output");

const resultSection = document.getElementById("resultSection");
const resultTitle = document.getElementById("resultTitle");
const resultBody = document.getElementById("resultBody");
const resultId = document.getElementById("resultId");

const titleError = document.getElementById("titleError");
const bodyError = document.getElementById("bodyError");

const SUBMIT_BUTTON_DEFAULT_TEXT = "Send practice post";
const SUBMIT_BUTTON_LOADING_TEXT = "Sending...";

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

function setLoading(isLoading) {
  submitBtn.disabled = isLoading;

  if (isLoading) {
    submitBtn.textContent = SUBMIT_BUTTON_LOADING_TEXT;
    submitBtn.setAttribute("aria-busy", "true");
    spinner.hidden = false;
    statusText.textContent = "Sending...";
  } else {
    submitBtn.textContent = SUBMIT_BUTTON_DEFAULT_TEXT;
    submitBtn.removeAttribute("aria-busy");
    spinner.hidden = true;
  }
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

  if (submitBtn.disabled) {
    return;
  }

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

  setLoading(true);

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
    setLoading(false);
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