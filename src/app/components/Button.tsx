"use client";
import React from "react";

interface ButtonProps {
  label: string;
  handleClick: () => void;
}

const Button: React.FC<ButtonProps> = ({
  label,
  handleClick = () => {},
}: ButtonProps) => {
  return (
    <>
      <button
        onClick={() => {
          handleClick();
        }}
      >
        {label}
      </button>
    </>
  );
};

export default Button;
