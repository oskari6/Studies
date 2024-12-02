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
          return reject(error.message);
        }
        if (stderr) {
          return reject(stderr);
        }
        try {
          const parsedOutput = JSON.parse(stdout);
          resolve(parsedOutput);
        } catch (parsedError) {
          reject(
            "Error parsing JSON from Python script: " + parseError.message
          );
        }
      }
    );
  });
}
