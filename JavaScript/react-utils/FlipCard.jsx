import { useState } from "react";

export default function FlipCard({ frontContent, backContent }) {
  const [isFlipped, setIsFlipped] = useState(false);
  return (
    <div
      className="group perspective"
      onMouseEnter={() => setIsFlipped(true)}
      onMouseLeave={() => setIsFlipped(false)}
    >
      <div className="relative w-64 h-40 transition-transform duration-700 transform-style-3d group-hover:rotate-y-180">
        <div className="absolute inset-0 flex items-center justify-center bg-red-200 text-white rounded-lg shadow-lg backface-hidden">
          <p
            className={`text-lg font-semibold ${
              isFlipped ? "rotate-y-180" : ""
            }`}
          >
            {frontContent}
          </p>
        </div>
      </div>

      <div className="absolute inset-0 flex items-center justify-center bg-gray-800 text-white rounded-lg shadow-lg rotate-y-180 backface-hidden">
        <p className="text-lg font-semibold rotate-y-180">{backContent}</p>
      </div>
    </div>
  );
}
