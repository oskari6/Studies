function Draw() {
  //for loop tree shape
  let field = document.getElementById("field"),
    whiteSpace = "",
    outputField = document.getElementById("outputField"),
    height = document.getElementById("height").value;

  field.innerHTML = "";
  outputField.innerHTML = "";

  if (isNaN(height) || height < 1) {
    alert("Vääränlainen numero tai ei numeroa");
    return;
  }

  for (i = 0; i < height; i++) whiteSpace += "&nbsp;";

  for (i = 0; i <= height; i++) {
    field.innerHTML += whiteSpace;
    for (j = 0; j < i; j++) {
      field.innerHTML += "*";
    }
    whiteSpace = whiteSpace.slice(0, -6);
    field.innerHTML += "<br>";
  }
  let lines = field.innerHTML.split("<br>");
  lines.forEach((line, index) => {
    if (index % 2 === 0) {
      outputField.innerHTML +=
        '<span style="color: red; margin:0">' + line + "</span><br>";
    } else {
      outputField.innerHTML +=
        '<span style="color: blue; margin:0">' + line + "</span><br>";
    }
  });
}
