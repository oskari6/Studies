import { useState, useEffect } from "react";
import Check from "./Check.jsx";
import Eye from "./Eye.jsx";
import EyeClosed from "./EyeClosed.jsx";
import Cross from "./Cross.jsx";

export default function Home() {
  const [show, setShow] = useState(false);
  const [showPassword, setShowPassword] = useState(false);
  const [password, setPassword] = useState("");
  const userName = "username6";
  const fullName = "oskari sulkakoski";
  const [requirements, setRequirements] = useState([
    { name: "At least 12 characters", status: 0 },
    { name: "A lowercase letter", status: 0 },
    { name: "An uppercase letter", status: 0 },
    { name: "A number", status: 0 },
    { name: "A symbol", status: 0 },
    { name: "No parts of your username", status: 0 },
    { name: "Does not include your first name", status: 0 },
    { name: "Does not include your last name", status: 0 },
  ]);

  useEffect(() => {
    passwordChecker(password);
  }, [password]);

  const passwordChecker = (password) => {
    setRequirements((prev) =>
      prev.map((req, index) => {
        if (index === 5) {
          return {
            ...req,
            status: password.includes(userName) ? 1 : 0,
          };
        }
        return req;
      })
    );
    if (password.includes(userName)) {
      requirements[5]["status"] = 1;
    } else {
      requirements[5]["status"] = 0;
    }
  };
  return (
    <>
      <div className="flex flex-col gap-4">
        <input className="bg-gray-200 rounded p-2" placeholder="name" />
        <input className="bg-gray-200 rounded p-2" placeholder="password" />
        <button>Sign in</button>
      </div>
      <button onClick={() => setShow(!show)} className="mt-4">
        Change password
      </button>
      {show && (
        <div className="fixed left-0 top-0 w-full h-full bg-black/50 flex justify-center items-center overflow-auto">
          <div id="modal" className="bg-white rounded-xl h-[600px] w-[500px]">
            <h2 className="font-bold mt-5">Setup password</h2>
            <div className="h-[70px] flex justify-center items-center">
              <span className="font-semibold">Password requirements</span>
            </div>
            <ul className="flex-1 overflow-auto pl-10 pr-10 pb-10">
              {requirements.map((entry, index) => (
                <>
                  <li key={index} className="ml-20 mb-2">
                    <div className="flex items-center space-x-2">
                      {entry.status == 0 ? <Check /> : <Cross />}
                      <span>{entry.name}</span>
                    </div>
                  </li>
                </>
              ))}
            </ul>
            <label className="font-bold">Enter password</label>
            <div className="flex justify-center items-center pt-2">
              <input
                type={showPassword ? "text" : "password"}
                onChange={(event) => setPassword(event.target.value)}
                className="bg-gray-200 rounded p-3 mr-2"
              />
              <button
                onClick={() => setShowPassword(!showPassword)}
                aria-label="Toggle password visibility"
              >
                <div>{showPassword ? <EyeClosed /> : <Eye />}</div>
              </button>
            </div>
            <button onClick={() => setShow(!show)}>close</button>
          </div>
        </div>
      )}
    </>
  );
}
