import { useState, useEffect, useRef } from "react";

export default function SidePanel({ isOpen, onClose, children }) {
  const panelRef = useRef(null);

  useEffect(() => {
    function handleClickOutside(event) {
      if (panelRef.current && !panelRef.current.contains(event.target)) {
        onClose();
      }
    }
    if (isOpen) {
      document.addEventListener("mousedown", handleClickOutside);
    } else {
      document.removeEventListener("mousedown", handleClickOutside);
    }
    return () => document.removeEventListener("mousedown", handleClickOutside);
  }, [isOpen, onClose]);
  return (
    <div
      className={`fixed top-0 left-0 h-full w-64 bg-gray-800 text-white shadow-lg transiton-transform duration-300 
        ${isOpen ? "translate-x-0" : "-translate-x-full"}`}
      ref={panelRef}
    >
      <button className="absolutetop-4 right-4 text-black" onClick={onClose}>
        ✖
      </button>
      <div className="p-4">{children}</div>
    </div>
  );
}
