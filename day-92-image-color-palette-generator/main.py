from flask import Flask, render_template, request, url_for
import os
from PIL import Image
from collections import Counter

app = Flask(__name__)

UPLOAD_FOLDER = os.path.join(os.path.dirname(__file__), 'static/uploads/')
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER  # is this necessary?


if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)


@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        if "image" not in request.files:
            return "There is no image file"
        file = request.files["image"]
        if file.filename == "":
            return "No selected file"
        if file:
            file_path = os.path.join(app.config["UPLOAD_FOLDER"], file.filename)
            file.save(file_path)
            hex_color_array = process_image(file.filename)
            image_url = url_for('static', filename='uploads/' + file.filename)
            return render_template("index.html", img_url=image_url, hex_array=hex_color_array)
    if request.method == "GET":
        return render_template("index.html", img_url=None)


def process_image(filename):
    image_path = os.path.join(UPLOAD_FOLDER, filename)
    image = Image.open(image_path)
    image = image.convert("RGB")
    image = image.quantize(colors=10, method=0, kmeans=3)
    image = image.convert("RGB")
    pixels = list(image.getdata())

    color_counts = Counter(pixels)
    top_ten_colors = color_counts.most_common(10)
    most_common_hex_colors = ['#{:02x}{:02x}{:02x}'.format(r, g, b) for (r, g, b), _ in top_ten_colors]
    return most_common_hex_colors


if __name__ == "__main__":
    app.run(debug=True)