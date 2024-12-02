const options = Array.from({ length: 40 }, (_, i) => i + 1);
const container = document.getElementById("result");
const selects = [
  document.getElementById("select-1"),
  document.getElementById("select-2"),
  document.getElementById("select-3"),
  document.getElementById("select-4"),
  document.getElementById("select-5"),
  document.getElementById("select-6"),
  document.getElementById("select-7"),
];
const winningNumbers = new Set();
const numbers = new Set();

selects.forEach((select) => {
  const empty = document.createElement("option");
  empty.value = "";
  empty.textContent = "Select a number";
  select.appendChild(empty);

  options.forEach((number) => {
    const option = document.createElement("option");
    option.value = number;
    option.textContent = number;
    select.appendChild(option);
  });
});

function generateNumbers() {
  winningNumbers.clear();
  while (winningNumbers.size < 7) {
    let random = Math.floor(Math.random() * 40) + 1;
    winningNumbers.add(random);
  }
}

function checkNumbers() {
  numbers.clear();
  let hasAll = true,
    duplicates = false;
  selects.forEach((select) => {
    let num = select.value;
    console.log(num);
    if (num === "") {
      hasAll = false;
    } else if (numbers.has(num)) {
      duplicates = true;
    } else numbers.add(Number(num));
  });
  if (!hasAll || duplicates) {
    container.innerHTML =
      "Please provide all numbers and ensure no duplicates.";
    return false;
  }

  return true;
}
function compareNumbers() {
  container.innerHTML = "";
  event.preventDefault();
  if (!checkNumbers()) return;

  generateNumbers();
  const winning = Array.from(winningNumbers).join(", ");
  const input = Array.from(numbers).join(", ");
  container.innerHTML += `Winning numbers: ${winning}<br>`;
  container.innerHTML += `Your numbers: ${input}<br>`;
  let count = 0;
  numbers.forEach((num) => {
    if (winningNumbers.has(num)) {
      count++;
    }
  });
  if (count === 7) container.innerHTML += "You won the lottery";
  else container.innerHTML += `You got ${count} of 7 correct`;
}
