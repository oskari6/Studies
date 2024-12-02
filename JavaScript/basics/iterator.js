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
