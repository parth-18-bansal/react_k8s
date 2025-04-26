import React, { useEffect, useState } from "react";
import PersonalInfoForm from './PersonalInfoForm';
import './index.css';

function App() {
  //const [message, setMessage] = useState("Loading...");

  // useEffect(() => {
  //   fetch("/api/")
  //     .then((res) => res.text())
  //     .then((data) => setMessage(data))
  //     .catch((err) => console.error(err));
  // }, []);

  return (
    <div>
      {/* <h1>Frontend Connected to Flask APIs</h1>
      <p>Flask says: {message}</p> */}
      <PersonalInfoForm />
    </div>
  );
}

export default App;
