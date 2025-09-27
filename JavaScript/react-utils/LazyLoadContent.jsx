import { useInView } from "react-intersection-observer";

export default function LazyLoadContent({ children, animation = "fade-in" }) {
  const { ref, inView } = useInView({ triggerOnce: true, threshold: 0.2 });

  const animations = {
    "fade-in": "opacity-0 translate-y-4",
    "slide-left": "opacity-0 -translate-x-6",
    "slide-right": "opacity-0 translate-x-6",
    "zoom-in": "opacity-0 scale-90",
  };

  return (
    <div
      ref={ref}
      className={`transition-all duration-700 ease-out ${
        inView
          ? "opacity-100 translate-y-0 translate-x-0 scale-100"
          : animations[animation]
      }`}
    >
      {children}
    </div>
  );
}
