function register() {
  document.getElementById("register-message").innerText = "";
  const userData = {
    firstname: document.getElementById("firstname").value,
    lastname: document.getElementById("lastname").value,
    email: document.getElementById("email").value,
    username: document.getElementById("reg-username").value,
    password: document.getElementById("reg-password").value,
  };
  handleRequest("http://localhost:8080/register", "POST", userData)
    .then((data) => {
      clearFields([
        "firstname",
        "lastname",
        "email",
        "reg-username",
        "reg-password",
      ]);
      closeModal();
      setTimeout(() => {
        updateBanner(data);
      }, 1000);
    })
    .catch((error) => {
      document.getElementById("register-message").innerText = error.message;
    });
}

function login() {
  document.getElementById("login-message").innerText = "";
  const loginData = {
    username: document.getElementById("login-username").value,
    password: document.getElementById("login-password").value,
  };
  handleRequest("http://localhost:8080/login", "POST", loginData)
    .then((data) => {
      updateUILogin();
      clearFields(["login-username", "login-password"]);
      closeModal();
      setTimeout(() => {
        updateBanner(data);
      }, 1000);
    })
    .catch((error) => {
      document.getElementById("login-message").innerText = error.message;
    });
}

function logout() {
  handleRequest("http://localhost:8080/logout", "POST")
    .then((data) => {
      closeModal();
      updateUILogout();
      setTimeout(() => {
        updateBanner(data);
      }, 1000);
    })
    .catch((error) => console.error("Error loggin out: ", error));
}
function updateBanner(newText) {
  const banner = document.getElementById("bannerText");
  banner.classList.remove("show");
  banner.classList.add("hide");

  setTimeout(() => {
    banner.innerHTML = newText;
    banner.classList.remove("hide");
    banner.classList.add("show");
  }, 700);
}
function updateUILogin() {
  document.getElementById("registerButton").style.display = "none";
  document.getElementById("loginButton").style.display = "none";
  document.getElementById("logoutButton").style.display = "flex";
}
function updateUILogout() {
  document.getElementById("registerButton").style.display = "flex";
  document.getElementById("loginButton").style.display = "flex";
  document.getElementById("logoutButton").style.display = "none";
}
function clearFields(fields) {
  fields.forEach((field) => {
    document.getElementById(field).value = "";
  });
}

function handleRequest(url, method, body = null) {
  return fetch(url, {
    method: method,
    headers: { "Content-Type": "application/json" },
    body: body ? JSON.stringify(body) : null,
  }).then((response) => {
    if (response.status === 200) {
      return response.text();
    } else {
      throw new Error("Fix the information");
    }
  });
}

function openModal(modalId) {
  const scrim = document.getElementById("scrim");
  const modals = document.querySelectorAll(".modal-content, .modal-content-2");

  modals.forEach((modal) => {
    modal.style.display = "none";
  });

  const modal = document.getElementById(modalId);
  if (modal) {
    console.log(modal.className);
    scrim.classList.remove("hide");
    scrim.style.display = "flex";
    scrim.classList.add("show");

    history.pushState({ modalOpen: true }, "", "#modal");

    modal.style.display = "flex";
    modal.style.opacity = "0";
    setTimeout(() => {
      modal.style.opacity = "1";
    }, 10);
  }
}

function closeModal() {
  const scrim = document.getElementById("scrim");
  const modals = document.querySelectorAll(".modal-content, .modal-content-2");

  scrim.classList.remove("show");
  scrim.classList.add("hide");

  modals.forEach((modal) => {
    modal.style.opacity = "0";
  });

  setTimeout(() => {
    scrim.style.display = "none";
    modals.forEach((modal) => {
      modal.style.display = "none";
    });
    if (history.state && history.state.modalOpen) {
      history.back();
    }
  }, 2000);
}

function openRegister() {
  openModal("registerContainer");
}
function openLogin() {
  openModal("loginContainer");
}
function openLogout() {
  openModal("logoutContainer");
}
function openIgluModal() {
  openModal("iglu-modal");
}
function openHuskyModal() {
  openModal("husky-modal");
}
function openSantasModal() {
  openModal("santas-modal");
}
function openMountainModal() {
  openModal("mountain-modal");
}
