import { ParallaxProvider, Parallax } from "react-scroll-parallax";
import Counter from "../animations/Counter";
import FlipCard from "../animations/FlipCard";
import ReactionButton from "../animations/ReactionButton";
import ScrollJacking from "../animations/ScrollJacking";

export default function ParallaxScrollingEffects() {
  const sections = [
    {
      content: (
        <h1 className="text-4xl font-bold text-white">
          Welcome to Scroll-Jacking!
        </h1>
      ),
      background: "#1E90FF",
    },
    {
      content: (
        <h1 className="text-4xl font-bold text-white">This is Section 2</h1>
      ),
      background: "#32CD32",
    },
    {
      content: (
        <h1 className="text-4xl font-bold text-white">Scroll to Section 3</h1>
      ),
      background: "#800080",
    },
    {
      content: (
        <h1 className="text-4xl font-bold text-white">
          Thank You for Scrolling!
        </h1>
      ),
      background: "#FF4500",
    },
  ];
  return (
    <ParallaxProvider>
      <div className="h-screen w-full bg-gray-100 text-center">
        <div className="h-screen flex flex-col justify-center items-center bg-blue-500 text-white">
          <h1 className="text-4xl font-bold">Welcome to parallax page</h1>
          <p className="text-lg">Scroll down for effects</p>
          <div className="flex space-x-6">
            <FlipCard frontContent="Front 1" backContent="Back 1" />
            <FlipCard frontContent="Front 2" backContent="Back 2" />
            <FlipCard frontContent="Front 3" backContent="Back 3" />
          </div>
        </div>
        <div className="flex justify-center items-center h-screen space-x-8 bg-gray-100">
          <ReactionButton icon="👍" label="Like" />
          <ReactionButton icon="❤️" label="Love" />
          <ReactionButton icon="😂" label="Haha" />
          <ReactionButton icon="😮" label="Wow" />
        </div>
        <Parallax speed={-20}>
          <div
            className="h-[50vh] flex items-center justify-center bg-cover bg-center"
            style={{ backgroundImage: "pix.jpg" }}
          >
            <h2 className="text-3xl font-bold bg-white/60 px-4 py-2 rounded">
              Company statistics
              <div>
                <Counter end={5000} suffix="+" />
                <p className="text-gray-600">Customers</p>
              </div>
            </h2>
          </div>
        </Parallax>
        <div className="h-screen flex flex-col justify-center items-center px-6">
          <p className="text-lg max-w-2xl">
            This section stays still while the background moves at a different
            speed.
          </p>
        </div>

        <div className="h-screen flex justify-center items-center relative">
          <Parallax translateX={[-100, 0]}>
            <div className="bg-white p-6 shadow-lg rounded-lg text-xl font-semibold">
              🚀 This element slides in from the **left**!
            </div>
          </Parallax>
        </div>

        <div className="h-screen flex justify-center items-center relative">
          <Parallax translateX={[100, 0]}>
            <div className="bg-white p-6 shadow-lg rounded-lg text-xl font-semibold">
              🎉 This element slides in from the **right**!
            </div>
          </Parallax>
        </div>
        <div className="h-screen flex justify-center items-center relative">
          <Parallax translateX={[100, -100]}>
            <div className="bg-white p-6 shadow-lg rounded-lg text-xl font-semibold">
              🎉 This element slides in from the **right**!
            </div>
          </Parallax>
        </div>

        <Parallax speed={-40}>
          <div
            className="h-[50vh] flex items-center justify-center bg-cover bg-center"
            style={{
              backgroundImage:
                "url('https://source.unsplash.com/random/1600x900?space')",
            }}
          >
            <h2 className="text-3xl font-bold bg-white/60 px-4 py-2 rounded">
              Parallax Section 2
            </h2>
          </div>
        </Parallax>

        <div className="h-screen flex flex-col justify-center items-center bg-gray-800 text-white">
          <h2 className="text-2xl font-bold">Thanks for Scrolling!</h2>
        </div>
        <ScrollJacking sections={sections} />
      </div>
    </ParallaxProvider>
  );
}
