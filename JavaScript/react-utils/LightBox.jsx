import { useEffect } from "react";

export default function Lightbox({ image, isOpen, onClose }) {
  useEffect(() => {
    const handleKeyDown = (event) => {
      if (event.key === "Escape") onClose();
    };

    if (isOpen) {
      document.addEventListener("keydown", handleKeyDown);
    }

    return () => document.removeEventListener("keydown", handleKeyDown);
  }, [isOpen, onClose]);

  if (!isOpen) return null;

  return (
    <div
      className="fixed inset-0 bg-black bg-opacity-75 flex items-center justify-center z-50 transition-opacity duration-300"
      onClick={onClose}
    >
      <div className="relative max-w-4xl max-h-[90vh]">
        <img
          src={image}
          alt="Lightbox"
          className="w-full h-auto rounded-lg shadow-lg"
        />
        <button
          className="absolute top-4 right-4 text-black text-3xl"
          onClick={onClose}
        >
          ✖
        </button>
      </div>
    </div>
  );
}
