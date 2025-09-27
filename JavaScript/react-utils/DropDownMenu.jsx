import { useState, useRef, useEffect } from "react";
export default function DropDownMenu({ title, items = [], onSelect }) {
  const [isOpen, setIsOpen] = useState(false);
  const dropdownRef = useRef(null);

  useEffect(() => {
    function handleClickOutside(event) {
      if (dropdownRef.current && !dropdownRef.current.contains(event.target)) {
        setIsOpen(false);
      }
    }
    document.addEventListener("mousedown", handleClickOutside);
    return () => document.removeEventListener("mousedown", handleClickOutside);
  }, []);

  return (
    <div className="relative inline-block" ref={dropdownRef}>
      <button
        className="px-4 py-2 bg-blue-500 text-black rounded hover:bg-blue-600"
        onClick={() => setIsOpen(!isOpen)}
      >
        {title}
      </button>
      {isOpen && (
        <ul className="absolute mt-2 w-40 bg-white border rounded shadow-lg">
          {items.map((item, index) => (
            <li
              key={index}
              className="px-4 -py-2 hover:bg-gray-100 cursor-pointer"
              onClick={() => {
                onSelect(item);
                setIsOpen(false);
              }}
            >
              {item}
            </li>
          ))}
        </ul>
      )}
    </div>
  );
}
