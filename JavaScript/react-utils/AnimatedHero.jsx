import { motion } from "framer-motion";

export default function AnimatedHero() {
  return (
    <div className="relative h-screen flex items-center justify-center bg-gradient-to-br from-blue-500 to-purple-600 text-white overflow-hidden">
      {/* Animated Background */}
      <motion.div
        className="absolute inset-0"
        animate={{ opacity: [0.5, 0.8, 0.5] }}
        transition={{ duration: 10, repeat: Infinity }}
        style={{
          background:
            "radial-gradient(circle, rgba(255,255,255,0.2), transparent)",
        }}
      />

      {/* Hero Content */}
      <div className="text-center z-10">
        <motion.h1
          className="text-5xl font-extrabold mb-4"
          initial={{ opacity: 0, y: -50 }}
          animate={{ opacity: 1, y: 0 }}
          transition={{ duration: 1 }}
        >
          Welcome to Our World
        </motion.h1>

        <motion.p
          className="text-lg mb-6"
          initial={{ opacity: 0, y: 50 }}
          animate={{ opacity: 1, y: 0 }}
          transition={{ duration: 1, delay: 0.5 }}
        >
          Discover endless possibilities with stunning designs.
        </motion.p>

        <motion.a
          href="#explore"
          className="inline-block bg-white text-blue-500 px-6 py-3 rounded-full font-semibold hover:bg-blue-100 transition-all duration-300"
          whileHover={{ scale: 1.1 }}
          whileTap={{ scale: 0.95 }}
        >
          Get Started
        </motion.a>
      </div>

      {/* Animated Image */}
      <motion.img
        src="https://source.unsplash.com/random/800x600"
        alt="Hero Illustration"
        className="absolute bottom-0 right-0 w-64 h-auto opacity-75 z-0"
        initial={{ x: 100, opacity: 0 }}
        animate={{ x: 0, opacity: 1 }}
        transition={{ duration: 1.5 }}
      />
    </div>
  );
}
