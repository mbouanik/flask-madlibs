const form = document.querySelector("#form");
const stories = document.querySelector("div .story");

form.addEventListener("submit", (evt) => {
  evt.preventDefault();
  checked = document.querySelectorAll("input[type=checkbox]:checked");
  if (checked.length == 1) {
    form.submit();
  } else if (checked.length > 1) {
    alert("Only one story at the time.");
    for (check of checked) {
      check.checked = false;
    }
  } else {
    alert("You must select at least one Story.");
  }
});

form.addEventListener("click", (evt) => {
  if (evt.target.tagName === "DIV") {
    const checked = document.querySelectorAll("input[type=checkbox]");
    for (let check of checked) {
      check.checked = false;
      check.nextSibling.nextSibling.style.backgroundColor = "#4682b4";
    }
    if (evt.target.previousSibling.previousSibling.checked) {
      evt.target.previousSibling.previousSibling.checked = false;
      evt.target.style.backgroundColor = "#4682b4";
    } else {
      evt.target.previousSibling.previousSibling.checked = true;
      evt.target.style.backgroundColor = "rgb(52, 97, 221)";
    }
  }
});
