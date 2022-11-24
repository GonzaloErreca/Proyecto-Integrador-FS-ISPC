"use strict";
"use strict";
const formulario = document.getElementById("form");
const nombre = document.getElementById("nombre");
const asunto = document.getElementById("asunto");
const email = document.getElementById("email");
const mensaje = document.getElementById("mensaje");
const parrafo = document.getElementById("msjAdvertencia");

const validacionForm = function (e) {
  e.preventDefault();
  let msjAdvertencia;
  let mostrarMsj = false;
  let expRegEmail = /^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$/;
  parrafo.innerHTML = "";
  if (nombre.value.length < 3) {
    msjAdvertencia = `Debes ingresar un nombre real <br />`;
    mostrarMsj = true;
  } else if (asunto.value.length < 3) {
    msjAdvertencia = `Por favor, ingresa el asunto <br />`;
    mostrarMsj = true;
  } else if (!expRegEmail.test(email.value)) {
    msjAdvertencia += `El correo no es valido <br />`;
    mostrarMsj = true;
  } else if (mensaje.value.length < 3) {
    msjAdvertencia = `Por favor, dejanos un mensaje <br />`;
    mostrarMsj = true;
  }
  if (mostrarMsj) {
    parrafo.innerHTML = msjAdvertencia;
  } else {
    parrafo.innerHTML = "Enviado...";
    setTimeout(function () {
      parrafo.innerHTML = "";
    }, 1200);
  }
};

formulario.addEventListener("submit", validacionForm);
