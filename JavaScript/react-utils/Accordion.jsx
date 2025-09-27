import { useState } from "react";

export default function Accordion({ items }) {
  const [openIndex, setOpenIndex] = useState(null);

  const handleToggle = (index) => {
    setOpenIndex(openIndex === index ? null : index);
  };

  return (
    <div className="w-full max-w-lg">
      {items.map((item, index) => (
        <div key={index} className="border-b">
          <button
            onClick={() => handleToggle(index)}
            className="w-full flex justify-between items-center py-3 px-4 text-left bg-gray-100 hover:bg-gray-200"
          >
            <span>{item.title}</span>
            <span>{openIndex === index ? "▲" : "▼"}</span>
          </button>
          {openIndex == index && (
            <div className="px-4 py-2 bg-white border-l border-r">
              {item.content}
            </div>
          )}
        </div>
      ))}
    </div>
  );
}
