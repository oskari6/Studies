import { useState } from "react";

export default function ToolTip({ text, position = "top", children }) {
  const [isvVisible, setIsVisible] = useState(false);

  return (
    <div
      className="relative inline-block"
      onMouseEnter={() => setIsVisible(true)}
      onMouseLeave={() => setIsVisible(false)}
    >
      {children}
      {isvVisible && (
        <div
          className={`absolute whitespace-nowrap bg-gray-800 text-white text-sm py-1 px-2 rounded shadow-md
            ${
              position === "top"
                ? "bottom-full left-1/2 transform -translate-x-1/2 mb-2"
                : ""
            }
          ${
            position === "bottom"
              ? "top-full left-1/2 transform -translate-x-1/2 mt-2"
              : ""
          }
          ${
            position === "left"
              ? "right-full top-1/2 transform -translate-y-1/2 mr-2"
              : ""
          }
          ${
            position === "right"
              ? "left-full top-1/2 transform -translate-y-1/2 ml-2"
              : ""
          }
          `}
        >
          {text}
        </div>
      )}
    </div>
  );
}
