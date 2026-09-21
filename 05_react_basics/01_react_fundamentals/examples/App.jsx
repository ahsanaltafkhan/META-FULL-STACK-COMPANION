import { useState } from "react";

export default function App() {
  const [message, setMessage] = useState("Hello React");

  return (
    <main>
      <h1>{message}</h1>
      <button onClick={() => setMessage("You clicked the button!")}>
        Click
      </button>
    </main>
  );
}
