export default function FloatActionButton({ icon, onClick }) {
  return (
    <button
      onClick={onClick}
      className="fixed bottom-8 right-8 bg-blue-500 text-white w-16 h-16 rounded-full shadow-lg flex items-center justify-center hover:bg-blue-600 transition-transform duration-300 hover:scale-110 focus:outline-none focus:ring-4 focus:ring-blue-300"
    >
      {icon || "+"}
    </button>
  );
}
