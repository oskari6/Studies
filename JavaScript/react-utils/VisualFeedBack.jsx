import { useState } from "react";
import { motion } from "framer-motion";

export function RippleButton({ children, onClick }) {
  const [rippleStyle, setRippleStyle] = useState({});
  const [showRipple, setShowRipple] = useState(false);

  const createRipple = (e) => {
    const rect = e.currentTarget.getBoundingClientRect();
    const size = Math.max(rect.width, rect.height);
    const x = e.clientX - rect.left - size / 2;
    const y = e.clientY - rect.top - size / 2;

    setRippleStyle({ width: size, height: size, top: y, left: x });
    setShowRipple(true);

    setTimeout(() => setShowRipple(false), 500); // Reset ripple after animation
    if (onClick) onClick();
  };

  return (
    <button
      className="relative overflow-hidden bg-blue-500 text-white px-6 py-3 rounded-lg focus:outline-none hover:bg-blue-600"
      onClick={createRipple}
    >
      {showRipple && (
        <span
          className="absolute rounded-full bg-white opacity-50 animate-ping"
          style={rippleStyle}
        />
      )}
      {children}
    </button>
  );
}

export function TapFeedbackButton({ children, onClick }) {
  return (
    <motion.button
      whileTap={{ scale: 0.9 }}
      onClick={onClick}
      className="bg-green-500 text-white px-6 py-3 rounded-lg shadow-lg focus:outline-none hover:bg-green-600"
    >
      {children}
    </motion.button>
  );
}

export function ClickHighLight({ children }) {
  const [circleStyle, setCircleStyle] = useState({});
  const [showCircle, setShowCircle] = useState(false);

  const handleClick = (e) => {
    const rect = e.currentTarget.getBoundingClientRect();
    const size = 50; // Size of the highlight
    const x = e.clientX - rect.left - size / 2;
    const y = e.clientY - rect.top - size / 2;

    setCircleStyle({ width: size, height: size, top: y, left: x });
    setShowCircle(true);

    setTimeout(() => setShowCircle(false), 400); // Remove highlight
  };

  return (
    <div className="relative overflow-hidden" onClick={handleClick}>
      {showCircle && (
        <span
          className="absolute rounded-full bg-yellow-400 opacity-75 animate-pulse"
          style={circleStyle}
        />
      )}
      {children}
    </div>
  );
}
