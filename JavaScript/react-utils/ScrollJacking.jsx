import { useState } from "react";
import ScrollWheelHandler from "react-scroll-wheel-handler";

export default function ScrollJacking({ sections }) {
  const [currentSection, setCurrentSection] = useState(0);

  const handleScrollUp = () => {
    if (currentSection > 0) setCurrentSection(currentSection - 1);
  };

  const handleScrollDown = () => {
    if (currentSection < sections.length - 1)
      setCurrentSection(currentSection + 1);
  };

  return (
    <ScrollWheelHandler
      upHandler={handleScrollUp}
      downHandler={handleScrollDown}
      timeout={700} // Prevents fast scrolling
    >
      <div className="h-screen w-full overflow-hidden">
        {sections.map((section, index) => (
          <div
            key={index}
            className={`absolute inset-0 transition-transform duration-700 ${
              currentSection === index
                ? "translate-y-0"
                : currentSection > index
                ? "-translate-y-full"
                : "translate-y-full"
            }`}
            style={{ backgroundColor: section.background }}
          >
            <div className="h-screen w-full flex items-center justify-center">
              {section.content}
            </div>
          </div>
        ))}
      </div>
    </ScrollWheelHandler>
  );
}
