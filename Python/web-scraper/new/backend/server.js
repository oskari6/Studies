const express = require("express");
const { exec } = require("child_process");
const cors = require("cors");
const app = express();
app.use(cors());
const path = require("path");
const fs = require("fs");

const pythonInterpeter = path.resolve(
  "C:\\Temp\\Python\\Webscraper\\.venv\\Scripts\\python.exe"
);
const pythonScript = path.resolve(
  "C:\\Temp\\Python\\Webscraper\\web_scraper.py"
);

app.get("/scrape/:element", async (req, res) => {
  const saveDir = "C:\\xampp\\htdocs\\robot\\new";
  const element = req.params.element;
  if (element === "all") {
    try {
      const elements = await getAllElements();
      if (elements) {
        res.status(200).json({ message: "ok!", data: elements });
      }
    } catch (error) {
      res.status(500).json({ data: error.message });
    }
  } else {
    exec(
      `${pythonInterpeter} ${pythonScript} ${saveDir} ${element}`,
      (error, stdout, stderr) => {
        if (error) {
          res.status(500).send({ error: error.message });
          return;
        }
        if (stderr) {
          res.status(500).send({ error: stderr });
          return;
        }
        res.status(200).json({ message: "ok!" });
      }
    );
  }
});

const currentFolder = "C:\\xampp\\htdocs\\robot\\new";

app.use(express.static(currentFolder));
app.get("/images", (req, res) => {
  fs.readdir(currentFolder, (err, files) => {
    if (err) {
      console.error("failed to get files");
      res.status(500).send("Failed to read");
      return;
    }

    const imageFiles = files.filter((file) =>
      /\.(jpg|jpeg|png|gif|webp)$/i.test(file)
    );
    res.json(imageFiles);
  });
});
app.listen(3000, () => {
  console.log("running");
});

const getAllElements = async () => {
  let elements = {
    titles: [],
    links: [],
    texts: [],
    lists: [],
  };
  const tasks = ["titles", "links", "texts", "lists"].map((element) => {
    return executer(element);
  });
  const results = await Promise.all(tasks);
  elements.titles = results[0];
  elements.links = results[1];
  elements.texts = results[2];
  elements.lists = results[3];
  return elements;
};

function executer(element, elements) {
  return new Promise((resolve, reject) => {
    exec(
      `${pythonInterpeter} ${pythonScript} ${null} ${element}`,
      (error, stdout, stderr) => {
        if (error) {
          console.error(error.message);
          return reject(error.message);
        }
        if (stderr) {
          console.error("1");
          return reject(stderr);
        }
        try {
          const parsedOutput = JSON.parse(stdout);
          resolve(parsedOutput);
        } catch (parseError) {
          console.error(parseError);
          reject(
            "Error parsing JSON from Python script: " + parseError.message
          );
        }
      }
    );
  });
}
