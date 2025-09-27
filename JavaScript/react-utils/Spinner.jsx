export default function Spinner({
  size = "w-12 h-12",
  color = "border-blue-500",
}) {
  return (
    <div
      className={`border-4 border-gray-200 border-t-${color} rounded-full animate-spin ${size}`}
    ></div>
  );
}
