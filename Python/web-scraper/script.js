function loadNewPage() {
  window.location.href = "/robot/new";
}
function Submit() {
  let username = document.getElementById("username_field").value;
  let password = document.getElementById("password_field").value;
  if (username === "demo" && password == "mode") {
    window.location.href = "/robot/welcome.html";
  }
}
