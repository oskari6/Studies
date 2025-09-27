import { useState } from "react";

export function GlowText({ text }) {
  return (
    <h1 className="text-5xl font-bold text-white text-center">
      <span className="relative glow-effect">{text}</span>
      <style>
        {`
                .glow-effect {
                position:relative;
                color: #ffffff;
                text-shadow: 0 0 5px #ffffff, 0 0 10px #00ffff, 0 0 20px #00ffff, 0 0 40px #00ffff;
                }`}
      </style>
    </h1>
  );
}
export function SpotlightText({ text }) {
  return (
    <div className="relative group w-full text-center">
      <h1 className="text-5xl font-bold text-gray-300 group-hover:text-white transition duration-500">
        {text}
      </h1>
      <div className="absolute inset-0 bg-gradient-to-r from-transparent via-white to-transparent opacity-0 group-hover:opacity-100 transition duration-500 blur-lg"></div>
    </div>
  );
}

export function InteractiveSpotlight({ text }) {
  const [spotlightStyle, setSpotlightStyle] = useState({});

  const handleMouseMove = (e) => {
    const rect = e.currentTarget.getBoundingClientRect();
    const x = e.clientX - rect.left;
    const y = e.clientY - rect.top;

    setSpotlightStyle({
      background: `radial-gradient(circle at ${x}px ${y}px, rgba(255, 255, 255, 0.8), transparent 80%)`,
    });
  };

  return (
    <div
      className="relative w-full h-full text-center text-5xl font-bold text-gray-300"
      onMouseMove={handleMouseMove}
      style={spotlightStyle}
    >
      {text}
    </div>
  );
}
