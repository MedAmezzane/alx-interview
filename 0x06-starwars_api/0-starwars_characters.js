#!/usr/bin/node
/**
 * This script fetches and prints character names from a specified Star Wars movie.
 * Usage: Provide a movie ID as a command-line argument.
 */
const request = require('request');
const movieId = process.argv[2];

// Check if a movie ID is provided
if (!movieId) {
  console.log('Enter movie ID');
  process.exit(1);
}

const apiUrl = `https://swapi-api.alx-tools.com/api/films/${movieId}`;

/**
 * Fetches movie data from the API.
 * @param {string} url - The URL of the movie API endpoint.
 * @returns {Promise<Object>} - A promise that resolves to the movie data.
 */
const fetchMovie = (url) => {
  return new Promise((resolve, reject) => {
    request.get(url, (err, res, body) => {
      if (err) {
        reject(err);
      } else {
        const movie = JSON.parse(body);
        resolve(movie);
      }
    });
  });
};

/**
 * Fetches character names from the movie data.
 * @param {Object} movie - The movie object containing character URLs.
 * @returns {Promise<string[]>} - A promise that resolves to an array of character names.
 */
const fetchCharacters = (movie) => {
  return Promise.all(
    movie.characters.map(async (characterUrl) => {
      return new Promise((resolve, reject) => {
        request.get(characterUrl, (err, res, body) => {
          if (err) {
            reject(err);
          } else {
            const character = JSON.parse(body);
            resolve(character.name);
          }
        });
      });
    })
  );
};

/**
 * Main function to fetch movie data and print character names.
 */
const main = async () => {
  try {
    const movie = await fetchMovie(apiUrl);
    const characters = await fetchCharacters(movie);

    characters.forEach((actor) => console.log(actor));
  } catch (err) {
    console.log(err);
  }
};

main();
