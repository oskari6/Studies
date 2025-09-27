export default function ProgressBar({ progress }) {
  return (
    <div className="w-full bg-gray-200 rounded-full h-4 overflow-hidden">
      <div
        className="h-full bg-blue-500 transition-all duration-300"
        style={{ width: `${progress}%` }}
      ></div>
    </div>
  );
}
