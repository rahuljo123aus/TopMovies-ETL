document.addEventListener('DOMContentLoaded', function () {
    const coverPage = document.getElementById('cover-page');
    const movieList = document.getElementById('movie-list');
    let searchInput;
    let movieItems;

    // Function to filter movies based on search input
    function filterMovies() {
        const searchTerm = searchInput.value.toLowerCase();

        movieItems.forEach(function(movieItem) {
            const movieTitle = movieItem.querySelector('h2').textContent.toLowerCase();

            if (movieTitle.includes(searchTerm)) {
                movieItem.style.display = 'block';
            } else {
                movieItem.style.display = 'none';
            }
        });
    }

    // Hide the cover page and transform it into the header after 3 seconds
    setTimeout(function() {
        coverPage.classList.add('hide');

        // Create page header with search bar
        const header = document.createElement('header');
        header.classList.add('page-header');

        searchInput = document.createElement('input');
        searchInput.setAttribute('type', 'text');
        searchInput.setAttribute('placeholder', 'Search for movies...');

        header.appendChild(searchInput);
        movieList.insertAdjacentElement('beforebegin', header);

        // Initialize the movie items after the cover page is hidden
        movieItems = document.querySelectorAll('.movie-item');

        // Add event listener for input changes in the search bar
        searchInput.addEventListener('input', filterMovies);
    }, 3000);


    fetch('output/movies.json')
        .then(response => {
            if (!response.ok) {
            throw new Error('Network response was not ok');
            }
            console.log(`status: ${response.status}`);
            return response.json();
        })
        .then(data => {
            console.log(data); // Do something with the JSON data
            console.log(typeof data);
            Object.values(data).forEach(movie => {
                const movieItem = document.createElement('div');
                movieItem.classList.add('movie-item');

                movieItem.innerHTML = `
                    <h2>${movie.title}</h2>
                    <p>Director: ${movie.director}</p>
                    <p>Writer: ${movie.writer}</p>
                    <p>Rating: ${movie.rating}</p>
                    <p>Genre: ${movie.genre}</p>
                    <p>Year: ${movie.year}</p>
                    <p>Language: ${movie.language}</p>
                `;

                movieList.appendChild(movieItem);
            });
        })
        .catch(error => {
            console.error('There was a problem with your fetch operation:', error);
        });

});
