import React from "react";

const LinkInput: React.FC = () => {
  return (
    <>
      <h1>Enter a video link to check:</h1>
      <input
        type="text"
        className="bg-gray-800 border-none focus:outline-none p-2 rounded-md"
        placeholder="https://youtube..."
        required
      ></input>
    </>
  );
};

export default LinkInput;
