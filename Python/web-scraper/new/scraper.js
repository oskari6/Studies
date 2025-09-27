window.onload = async () => {
  getImages();
  getOtherElements();
};

async function getImages() {
  try {
    const response = await fetch("http://localhost:3000/scrape/images");
    const data = await response.json();

    if (!response.ok) {
      console.log("failed fetch: ", data);
      return;
    }
    const container = document.getElementById("container");
    if (container) {
      const response = await fetch("http://localhost:3000/images");
      if (!response.ok) {
        console.error("failed to fetch images");
        return;
      }
      const images = await response.json();
      images.forEach((image) => {
        const imgElement = document.createElement("img");
        imgElement.src = `http://localhost:3000/${image}`; // Path to the image file
        container.appendChild(imgElement); // Append to the container div
      });
    }
  } catch (error) {
    console.error("Error fetching scraped data: ", error.message);
  }
}

async function getOtherElements() {
  try {
    const response = await fetch("http://localhost:3000/scrape/all");
    const data = await response.json();
    if (!response.ok) {
      console.log("failed fetch: ", data);
      return;
    }
    const container = document.getElementById("container");
    if (container) {
      const elements = data.data;

      const elementIterator = {
        data: elements,
        *[Symbol.iterator]() {
          for (const [key, items] of Object.entries(this.data)) {
            if (key === "titles") {
              yield { key, items, tag: "h1" };
            } else if (key === "links") {
              yield { key, items, tag: "a" };
            } else if (key === "texts") {
              yield { key, items, tag: "p" };
            } else if (key === "lists") {
              yield { key, items, tag: "li" };
            }
          }
        },
      };

      for (const { key, items, tag } of elementIterator) {
        let section;
        key === "lists"
          ? (section = document.createElement("ul"))
          : (section = document.createElement("div"));

        items.forEach((item) => {
          const element = document.createElement(tag);
          if (tag === "a") {
            element.href = item;
            element.textContent = "Link";
            section.innerHTML += "<br>";
          } else {
            element.textContent = item;
          }
          section.appendChild(element);
        });
        container.appendChild(section);
      }
    }
  } catch (error) {
    console.error("Error fetching scraped data: ", error.message);
  }
}

function goBack() {
  window.location.href = "/robot";
}
