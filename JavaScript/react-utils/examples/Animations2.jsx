import { useState, useEffect } from "react";
import Skeleton from "../animations/Skeleton";
import ScrollIndicator from "../animations/ScrollIndicator";
import LazyLoadContent from "../animations/LazyLoadContent";
import LightBox from "../animations/LightBox";

export default function Animations2() {
  const [loading, setLoading] = useState(true);
  const [isOpen, setIsOpen] = useState(true);
  const imageUrl = "pix.jpg";

  useEffect(() => {
    setTimeout(() => setLoading(false), 3000);
  }, []);

  return (
    <div className="p-6 max-w-md mx-auo space-y-4">
      <div className="flex flex-col items-center justify-center h-screen bg-gray-100">
        <h1 className="text-xl font-bold mb-4">Lightbox</h1>
        <img
          src={imageUrl}
          alt="thumbnail"
          className="w-48 h-32 rounded-lg shadow-md cursor-pointer transition-transform duration-300 hover:scale-105"
          onClick={() => setIsOpen(true)}
        />
        <LightBox
          image={imageUrl}
          isOpen={isOpen}
          onClose={() => setIsOpen(false)}
        />
      </div>
      {loading ? (
        <>
          <Skeleton width="w-32" height="h-8" />
          <Skeleton />
          <Skeleton width="w-48" />
          <Skeleton width="w-full" height="h-40" rounded="rounded-lg" />
        </>
      ) : (
        <div className="h-screen overflow-y-auto">
          <div className="p-4 bg-white shadow rounded-lg">
            <h2 className="text-lg font-bold">Loaded Content</h2>
            <p className="text-gray-700">This content has finished loading!</p>
          </div>
          <ScrollIndicator />
          <div>
            <h1 className="h-[200vh] p10 space-y-6"></h1>
            <p className="text-gray-700">
              This is a long page with a scroll indicator.
            </p>
            <p className="text-gray-700">
              Keep scrolling to see the progress bar at the top!
            </p>
          </div>
        </div>
      )}
      <div className="min-h-screen flex flex-col items-center space-y-12 p-12 bg-gray-100">
        <h1 className="text-2xl font-bold mt-100">
          Scroll Down to see lazy loaded content
        </h1>

        <LazyLoadContent animation="fade-in">
          <div className="w-80 h-40 bg-white shadow-lg rounded-lg flex justify-center items-center">
            <p className="text-lg font-semibold">Fade-in Effect</p>
          </div>
        </LazyLoadContent>

        <LazyLoadContent animation="slide-left">
          <div className="w-80 h-40 bg-white shadow-lg rounded-lg flex justify-center items-center">
            <p className="text-lg font-semibold">Slide Left Effect</p>
          </div>
        </LazyLoadContent>

        <LazyLoadContent animation="slide-right">
          <div className="w-80 h-40 bg-white shadow-lg rounded-lg flex justify-center items-center">
            <p className="text-lg font-semibold">Slide Right Effect</p>
          </div>
        </LazyLoadContent>

        <LazyLoadContent animation="zoom-in">
          <div className="w-80 h-40 bg-white shadow-lg rounded-lg flex justify-center items-center">
            <p className="text-lg font-semibold">Zoom-in Effect</p>
          </div>
        </LazyLoadContent>
      </div>
    </div>
  );
}
