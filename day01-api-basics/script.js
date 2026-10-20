console.log("Day 1 script loaded");

const loadBtn = document.getElementById("loadBtn");
const output = document.getElementById("output");

loadBtn.addEventListener("click", async () => {
  console.log("Button clicked");
  output.textContent = "Loading...";

  try {
    const response = await fetch(
      "https://jsonplaceholder.typicode.com/posts/1"
    );

    console.log("Response status:", response.status);

    if (!response.ok) {
      throw new Error(`Request failed: ${response.status}`);
    }

    const data = await response.json();
    output.textContent = JSON.stringify(data, null, 2);
  } catch (error) {
    console.error(error);
    output.textContent = `Error: ${error.message}`;
  }
});