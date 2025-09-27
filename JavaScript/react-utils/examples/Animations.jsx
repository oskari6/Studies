import DropDownMenu from "../animations/DropDownMenu";
import ToolTip from "../animations/ToolTip";
import Accordion from "../animations/Accordion";
import ProgressBar from "../animations/ProgressBar";
import NotificationBanner from "../animations/NotificationBanner";

import {
  ZoomCard,
  TiltCard,
  SlideTextCard,
  RotateCard,
} from "../animations/CardAnimations";
import { useState } from "react";
import {
  FixedToTopButton,
  NormalToTopButton,
} from "../animations/BackToTopButton";

export default function Adnimations() {
  const [progress, setProgress] = useState(30);
  const [notification, setNotification] = useState(null);

  const showNotification = (type, message) => {
    setNotification({ type, message });
  };

  const handleSelect = (item) => {
    alert(`Selected: ${item}`);
  };

  const accordionItems = [
    {
      title: "What is React?",
      content: "React is a JavaScript library for building UI components.",
    },
    {
      title: "What is Vite?",
      content: "Vite is a fast build tool for modern web projects.",
    },
    {
      title: "Why use React?",
      content:
        "React allows building dynamic web apps with reusable components.",
    },
  ];
  return (
    <>
      <div className="flex justify-center items-center h-screen flex-col gap-2">
        {notification && (
          <NotificationBanner
            message={notification.message}
            type={notification.type}
            onClose={() => setNotification(null)}
          />
        )}
        <h1>Animations Page</h1>
        <ZoomCard>test</ZoomCard>
        <SlideTextCard>test</SlideTextCard>
        <RotateCard>test</RotateCard>
        <TiltCard>test</TiltCard>

        <div>
          <button
            className="px-4 py-2 bg-green-500 text-black rounded"
            onClick={() => showNotification("success", "Operation successful!")}
          >
            Show Success
          </button>

          <button
            className="px-4 py-2 bg-red-500 text-black rounded"
            onClick={() => showNotification("error", "Something went wrong!")}
          >
            Show Error
          </button>

          <button
            className="px-4 py-2 bg-yellow-500 text-black rounded"
            onClick={() => showNotification("warning", "This is a warning!")}
          >
            Show Warning
          </button>

          <button
            className="px-4 py-2 bg-blue-500 text-black rounded"
            onClick={() => showNotification("info", "Here's some info!")}
          >
            Show Info
          </button>
        </div>
        <div className="flex flex-col items-center justify-center h-screen gap-4">
          <ProgressBar progress={progress} />
          <button
            className="px-4 py-2 bg-blue-500 text-black rounded"
            onClick={() => setProgress((prev) => (prev >= 100 ? 0 : prev + 10))}
          >
            Increase Progress
          </button>
        </div>
        <Accordion items={accordionItems} />
        <ToolTip text="Tooltip here" position="top">
          <button>Hover me</button>
        </ToolTip>
        <DropDownMenu
          title="Select an Option"
          items={["Profile", "Settings", "Logout"]}
          onSelect={handleSelect}
        />
      </div>
      <div className="bg-gray-200 h-[900px] flex justify-end items-end">
        <NormalToTopButton />
        <NormalToTopButton animated={false} />
      </div>
      <div className="bg-gray-200 h-[900px] flex justify-end items-end">
        <FixedToTopButton />
      </div>
    </>
  );
}
