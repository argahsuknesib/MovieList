import "./App.css";
import React, { useEffect, useState } from "react";
import { Movies } from "./components/Movies";

function App() {

  const [movies, setMovies] = useState([]);


  useEffect(
    () =>
      fetch("http://localhost:8080/movie").then((response) =>
        response.json().then((data) => {
          setMovies(data.movies);
        })
      ),
    []
  );

  return <div className="App">
    <Movies movies={movies} />

  </div>;
}

export default App;
