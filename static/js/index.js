// Open Single Modal
const openEls = document.querySelectorAll("[data-open]");
const isVisible = "is-visible";

for(const el of openEls) {
  el.addEventListener("click", function() {
    const modalId = this.dataset.open;
    document.getElementById(modalId).classList.add(isVisible);
  });
}

// Close Modal with X
const closeEls = document.querySelectorAll("[data-close]");

for (const el of closeEls) {
  el.addEventListener("click", function() {
    this.parentElement.classList.remove(isVisible);
  });
}

// CLose Modal clicking outside
document.addEventListener("click", e => {
  if (e.target == document.querySelector(".modal.is-visible")) {
    document.querySelector(".modal.is-visible").classList.remove(isVisible);
  }
});

// Close Modal by pressing esc key
document.addEventListener("keyup", e => {
  if (e.key == "Escape" && document.querySelector(".modal.is-visible")) {
    document.querySelector(".modal.is-visible").classList.remove(isVisible);
  }
});

// Play Sounds When Clicked
function play(name) {
  let sound = new Audio("static/sounds/" + name + "-sound.mp3");
  sound.play()
};