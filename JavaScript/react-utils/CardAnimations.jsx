export function ZoomCard({ children }) {
  return (
    <div className="flex justify-center items-center h-screen bg-gray-100">
      <div className="w-64 h-40 bg-white shadow-lg rounded-lg overflow-hidden transition-transform duration-300 hover:scale-105 flex justify-center items-center">
        <p className="text-lg font-semibold">{children}</p>
      </div>
    </div>
  );
}
export function SlideTextCard({ children }) {
  return (
    <div className="flex justify-center items-center h-screen bg-gray-100">
      <div className="relative w-64 h-40 bg-white shadow-lg rounded-lg overflow-hidden flex justify-center items-center">
        <p className="text-lg font-semibold transition-all duration-300 transform hover:-translate-y-3">
          {children}
        </p>
      </div>
    </div>
  );
}
export function RotateCard({ children }) {
  return (
    <div className="flex justify-center items-center h-screen bg-gray-100">
      <div className="w-64 h-40 bg-white shadow-lg rounded-lg overflow-hidden transition-transform duration-300 hover:rotate-6 flex justify-center items-center">
        <p className="text-lf font-semibold">{children}</p>
      </div>
    </div>
  );
}
export function TiltCard({ children }) {
  return (
    <div className="flex justify-center items-center h-screen bg-gray-100">
      <div className="w-64 h-40 bg-white shadow-lg rounded-lg overflow-hidden transition-transform duration-300 hover:rotate-2 hover-scale-105 flex justify-center items-center">
        <p className="text-lg font-semibold">{children}</p>
      </div>
    </div>
  );
}
