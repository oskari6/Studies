import { useEffect, useState } from "react";

export const scrollToTop = (animated = true) => {
  window.scrollTo({
    top: 0,
    behavior: animated ? "smooth" : "auto",
  });
};

export const FixedToTopButton = ({ animated = true }) => {
  const [visible, setVisible] = useState(false);

  useEffect(() => {
    const toggleVisiblity = () => {
      if (window.scrollY > 300) {
        setVisible(true);
      } else {
        setVisible(false);
      }
    };

    window.addEventListener("scroll", toggleVisiblity);
    return () => window.removeEventListener("scroll", toggleVisiblity);
  }, []);

  return (
    <button
      onClick={() => scrollToTop(animated)}
      style={{
        position: "fixed",
        bottom: "20px",
        right: "20px",
        padding: "10px 20px",
        fontSize: "16px",
        backgroundColor: "#007bff",
        color: "#fff",
        border: "none",
        borderRadius: "5px",
        cursor: "pointer",
        display: visible ? "block" : "none",
      }}
    >
      ↑ Back to Top
    </button>
  );
};

export const NormalToTopButton = ({ animated = true }) => {
  return <button onClick={() => scrollToTop(animated)}>↑ Back to Top</button>;
};
