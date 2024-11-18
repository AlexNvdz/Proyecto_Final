let currentReservaId = null;

// Mostrar el modal de detalles
function showDetailsModal(button) {
  const modalOverlay = document.getElementById("detailsModal");

  // Campos del modal
  const modalUsuario = document.getElementById("modalUsuario");
  const modalEvento = document.getElementById("modalEvento");
  const modalFecha = document.getElementById("modalFecha");
  const modalHora = document.getElementById("modalHora");
  const modalInvitados = document.getElementById("modalInvitados");
  const modalDuracion = document.getElementById("modalDuracion");
  const modalCorreo = document.getElementById("modalCorreo");

  // Obtener datos del atributo data-reserva
  const reservaData = JSON.parse(button.getAttribute("data-reserva"));

  // Llenar los datos en el modal
  modalUsuario.textContent = button.parentElement.parentElement.querySelector("td:nth-child(3)").textContent;
  modalEvento.textContent = button.parentElement.parentElement.querySelector("td:nth-child(2)").textContent;
  modalCorreo.textContent = button.parentElement.parentElement.querySelector("td:nth-child(4)").textContent;
  modalFecha.textContent = reservaData.fecha || "N/A";
  modalHora.textContent = reservaData.hora || "N/A";
  modalInvitados.textContent = reservaData.invitados || "N/A";
  modalDuracion.textContent = reservaData.duracion || "N/A";

  // Mostrar el modal
  modalOverlay.style.display = "flex";
}

// Cerrar el modal
function closeDetailsModal() {
  document.getElementById("detailsModal").style.display = "none";
}

// Detectar clic en los botones de detalles
const botonesDetalles = document.querySelectorAll('.btn-detalles');
botonesDetalles.forEach(function (boton) {
  boton.addEventListener('click', function () {
    showDetailsModal(boton);
  });
});
