const request = require('request');

const movieId = process.argv[2];

if (!movieId) {
  console.log('Usage: node 0-starwars_characters.js <movie_id>');
  process.exit(1);
}

const movieUrl = `https://swapi.dev/api/films/${movieId}/`;

request.get(movieUrl, (error, response, body) => {
  if (error) {
    console.error('Error fetching movie data:', error);
    return;
  }

  if (response.statusCode !== 200) {
    console.error('Failed to fetch movie data. Status code:', response.statusCode);
    return;
  }

  const movieData = JSON.parse(body);
  const characterUrls = movieData.characters;

  characterUrls.forEach(characterUrl => {
    request.get(characterUrl, (charError, charResponse, charBody) => {
      if (charError) {
        console.error('Error fetching character data:', charError);
        return;
      }

      if (charResponse.statusCode !== 200) {
        console.error('Failed to fetch character data. Status code:', charResponse.statusCode);
        return;
      }

      const characterData = JSON.parse(charBody);
      console.log(characterData.name);
    });
  });
});
