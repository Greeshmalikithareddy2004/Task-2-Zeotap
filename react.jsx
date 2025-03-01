import { useState } from "react";

function ChatWindow() {
  const [question, setQuestion] = useState("");
  const [response, setResponse] = useState("");

  const handleAsk = async () => {
    const res = await fetch(`/ask?question=${question}`);
    const data = await res.json();
    setResponse(data.answer);
  };

  return (
    <div className="chat-container">
      <input 
        type="text" 
        value={question} 
        onChange={(e) => setQuestion(e.target.value)} 
        placeholder="Ask a CDP question..."
      />
      <button onClick={handleAsk}>Ask</button>
      <p>Response: {response}</p>
    </div>
  );
}

export default ChatWindow;
