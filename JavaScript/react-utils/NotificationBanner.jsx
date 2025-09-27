import { useEffect, useState } from "react";

export default function NotificationBanner({
  message,
  type = "info",
  onClose,
}) {
  useEffect(() => {
    const timer = setTimeout(() => {
      onClose();
    }, 3000);
    return () => clearTimeout(timer);
  }, [onClose]);

  const typeStyles = {
    success: "bg-green-500 text-white",
    error: "bg-red-500 text-white",
    warning: "bg-yellow-500 text-black",
    info: "bg-blue-500 text-white",
  };

  return (
    <div
      className={`fixed top-4 left-1/2 transform -translate x-1/2 px-4 py-2 rounded shadow-md ${typeStyles[type]}`}
    >
      <div className="flex justify-between items-center">
        <span>{message}</span>
        <button className="ml-4 text-black" onClick={onClose}>
          ✖
        </button>
      </div>
    </div>
  );
}
