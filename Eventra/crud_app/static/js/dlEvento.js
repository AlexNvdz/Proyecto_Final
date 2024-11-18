// archivo static/js/eliminar_evento.js
let currentEventoId = null;

// Función para mostrar el modal
function showModal(eventoId) {
  currentEventoId = eventoId;
  document.getElementById('confirmModal').style.display = 'flex';
}

// Función para cerrar el modal
function closeModal() {
  document.getElementById('confirmModal').style.display = 'none';
}

// Función para manejar la eliminación del evento
function handleDelete() {
  if (currentEventoId) {
    const url = "/evento/eliminar/" + currentEventoId + "/";  // Aquí la URL se genera dinámicamente
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
