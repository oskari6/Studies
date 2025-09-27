import { useState } from "react";
import { motion } from "framer-motion";

export default function ReactionButton({ icon, label }) {
  const [count, setCount] = useState(0);
  const [isAnimating, setIsAnimating] = useState(false);

  const handleClick = () => {
    setCount(count + 1);
    setIsAnimating(true);
    setTimeout(() => setIsAnimating(false), 500);
  };

  return (
    <div className="flex flex-col items-center space-y-2">
      <motion.button
        className="text-4xl cursor-pointer"
        onClick={handleClick}
        whileTap={{ scale: 1.2 }}
      >
        <motion.div
          className="relative"
          animate={{ scale: isAnimating ? 1.2 : 1 }}
          transition={{ type: "spring", stiffness: 300 }}
        >
          {icon}
        </motion.div>
      </motion.button>
      <span className="text-sm text-gray-500">{label}</span>
      <motion.div
        className="text-xl font-bold text-blue-500"
        key={count}
        initial={{ scale: 0, opacity: 0 }}
        animate={{ cale: 1, opacity: 1 }}
        transition={{ type: "spring", stiffness: 200 }}
      >
        {count}
      </motion.div>
    </div>
  );
}
