import React, {useEffect,useState} from "react";
import "./App.css";

function App(){
  const [page,setPage] = useState("home");
  const [brand,setBrand] = useState("pacific");
  const [content,setContent] = useState("");
  const year = new Date().getFullYear();

  useEffect(() => {

    const url = page === "home" ? "http://127.0.0.1:5000/" : "http://127.0.0.1:5000/contact";

    fetch(url,{

      headers : {
        "X-API-KEY" : "myapikey",
      },

    }).then((res) => res.json())
    .then((data) => {

      setBrand(data.brand);
    setContent(data.content);

    }).catch((err) => {

      console.log(err);

    })
  },[page]);

  return (

    <div className="container">
     
      <header className="header">

        <h1 className="brand"> {brand} </h1>
      </header>


  
      <nav className="nav">

        <button
          className={`nav-btn ${page === "home" ? "active" : ""}`}
          onClick={() => setPage("home")}
        >
          Home

        </button>

        <button
          className={`nav-btn ${page === "contact" ? "active" : ""}`}
          onClick={() => setPage("contact")}
        >
          Contact

        </button>

      </nav>

 
      <main className="main">
        
        <h2 className="page-title">

          {page === "home" ? "Home Page" : "Contact Page"}
          
        </h2>

        <p className="content-text"> {content} </p>

      </main>

      
      <footer className="footer">

        © {year} Harshit Roy, All rights reserved.

      </footer>

    </div>

  );
}

export default App;