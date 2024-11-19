function searchEvents() {
    let query = document.getElementById("search-input").value;
  
    if (query.length < 3) {  // Solo buscar si hay 3 o más caracteres
      document.getElementById("search-results").innerHTML = '';
      return;
    }
  
    $.ajax({
      url: '/search-events/',  // Ruta para buscar eventos
      data: {
        'query': query,
      },
      dataType: 'json',
      success: function (data) {
        let resultsContainer = document.getElementById("search-results");
        resultsContainer.innerHTML = '';  // Limpiar resultados anteriores
  
        if (data.results.length < 2) {
          data.results.forEach(function (evento) {
            let resultItem = document.createElement("div");
            resultItem.className = "search-result-item";
            resultItem.innerHTML = `
              <a href="/sala/${evento.id}/">${evento.nombre}</a>
            `;
            resultsContainer.appendChild(resultItem);
          });
        } else {
          resultsContainer.innerHTML = '<p>No se encontraron resultados.</p>';
        }
      }
    });
  }
  