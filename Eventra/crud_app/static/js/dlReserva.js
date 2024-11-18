// archivo static/js/eliminar_evento.js
let currentReservaId = null;

// Función para mostrar el modal
function showModal(reservaId) {
  currentReservaId = reservaId;
  document.getElementById('confirmModal').style.display = 'flex';
}

// Función para cerrar el modal
function closeModal() {
  document.getElementById('confirmModal').style.display = 'none';
}

// Función para manejar la eliminación del evento
function handleDelete() {
  if (currentReservaId) {
    const url = "/reserva/eliminar/" + currentReservaId + "/";  // Aquí la URL se genera dinámicamente
    window.location.href = url;
  }
}

// Agregar el listener al botón de eliminar
document.addEventListener('DOMContentLoaded', function () {
  const deleteBtn = document.getElementById('deleteBtn');
  if (deleteBtn) {
    deleteBtn.addEventListener('click', handleDelete);
  }
});
