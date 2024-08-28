const fullTextout =
  "I am your Commoning ... ";
const fullText =
  "I am your Commoning Interpreter, and you can record your thoughts on topics related to commoning here. I will transcribe them, write a brief reflection, and then assess how well the text aligns with the ideals of commoning.";

const initialText = fullTextout;
text1.innerText = fullTextout;

// Set the initial height to ensure smooth first transition
text1.style.height = "17px";

let timeoutId;

text1.addEventListener("mouseover", () => {
  clearTimeout(timeoutId);
  text1.innerText = fullText;

  // Get the full height of the content
  const fullHeight = text1.scrollHeight + "px";

  // Set the height to the current height first (for smooth animation)
  text1.style.height = text1.offsetHeight + "px";

  // Trigger a reflow to apply the current height before changing it
  text1.offsetHeight; // This forces a reflow, necessary for the transition

  // Now, set the height to the full height, which will trigger the transition
  text1.style.height = fullHeight;
});

text1.addEventListener("mouseout", () => {
  // Set the height back to the initial height
  text1.style.height = "17px";

  timeoutId = setTimeout(() => {
    text1.innerText = initialText;
  }, 725);
});
