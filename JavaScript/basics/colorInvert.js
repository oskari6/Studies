window.onload = function () {
  const canvas = document.getElementById("canvas");
  const context = canvas.getContext("2d");
  const redBtn = document.getElementById("red");
  const blueBtn = document.getElementById("blue");

  const img = new Image();
  img.src = "1.jpg";
  let originalImageData;

  img.onload = () => {
    canvas.width = img.width;
    canvas.height = img.height;

    context.drawImage(img, 0, 0);

    originalImageData = context.getImageData(0, 0, canvas.width, canvas.height);

    function changeColor(targetColor) {
      let imageData = context.createImageData(originalImageData);
      imageData.data.set(originalImageData.data);

      let data = imageData.data;

      for (let i = 0; i < data.length; i += 4) {
        let r = data[i];
        let g = data[i + 1];
        let b = data[i + 2];

        let grayscale = 0.3 * r + 0.59 * g + 0.11 * b;

        if (
          Math.abs(r - grayscale) > 20 ||
          Math.abs(g - grayscale) > 20 ||
          Math.abs(b - grayscale) > 20
        ) {
          if (targetColor === "blue") {
            data[i] = Math.max(0, r - 150);
            data[i + 1] = Math.max(0, g - 10);
            data[i + 2] = Math.min(150, b + 100);
          } else if (targetColor === "red") {
            data[i] = r;
            data[i + 1] = g;
            data[i + 2] = b;
          }
        }
      }
      context.putImageData(imageData, 0, 0);
    }

    redBtn.addEventListener("click", function () {
      changeColor("red");
    });

    blueBtn.addEventListener("click", function () {
      changeColor("blue");
    });
  };
};
