const carrosel_filmes = document.querySelector('#js-carrosel-filmes');
const apiHost = 'http://localhost:9007';

fetch(`${apiHost}/images`)
  .then(response => {
    if (!response.ok) {
      throw new Error(`HTTP error! status: ${response.status}`);
    }
    return response.json();
  })
  .then(data => {
    data.forEach(image => {
      const item = document.createElement('div');
      item.className = 'item';
      const img = document.createElement('img');
      img.className = 'box-filme';
      img.src = `${apiHost}${image}`;
      item.appendChild(img);
      carrosel_filmes.appendChild(item);
    });

    $('.owl-carousel').owlCarousel({
      loop: true,
      margin: 10,
      nav: false,
      responsive: {
          0: {
              items: 1
          },
          600: {
              items: 3
          },
          1000: {
              items: 5
          }
      }
    })
  })
  .catch(error => {
    console.error('Error fetching images:', error);
  });

