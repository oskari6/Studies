import { useState, useEffect } from "react";
import FloatActionButton from "../animations/FloatActionButton";
import {
  ClickHighLight,
  RippleButton,
  TapFeedbackButton,
} from "../animations/VisualFeedBack";
import AnimatedHero from "../animations/AnimatedHero";
import {
  GlowText,
  InteractiveSpotlight,
  SpotlightText,
} from "../animations/TextAnimation";

export default function Animations3() {
  const handleFabClick = () => {
    alert("Fab clicked");
  };

  return (
    <div className="bg-gray-100 p-6 space-y-16 flex flex-col">
      <AnimatedHero />
      <GlowText text="test" />
      <SpotlightText text="test" />
      <InteractiveSpotlight text="test" />
      <FloatActionButton icon="📄" onClick={handleFabClick} />
      <RippleButton onClick={() => alert("test")}>Click me</RippleButton>
      <TapFeedbackButton onClick={() => alert("test")}>
        Tap me
      </TapFeedbackButton>
      <ClickHighLight>
        <div className="b-purple-500 text-white px-6 py-3 rounded-lg shadow-lg">
          Click Anywhere
        </div>
      </ClickHighLight>
    </div>
  );
}
