fetch('https://www.googleapis.com/books/v1/volumes?q=programming')
  .then(response => response.json())
  .then(data => {
    const booksContainer = document.getElementById('books-suggestions');
    data.items.forEach(book => {
      const card = document.createElement('div');
      card.className = 'col-md-4 mb-4';
      card.innerHTML = `
        <div class="card shadow-lg">
          <img src="${book.volumeInfo.imageLinks?.thumbnail || 'https://via.placeholder.com/150'}" class="card-img-top" alt="${book.volumeInfo.title}">
          <div class="card-body">
            <h5 class="card-title">${book.volumeInfo.title}</h5>
            <p class="card-text">${book.volumeInfo.description || 'Sin descripción disponible.'}</p>
          </div>
        </div>
      `;
      booksContainer.appendChild(card);
    });
  })
  .catch(error => {
    console.error('Error al cargar los libros:', error);
  });

  
