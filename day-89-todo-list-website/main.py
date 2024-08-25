from flask import Flask, render_template, redirect, url_for, request
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, BooleanField
from flask_bootstrap import Bootstrap5
from wtforms.validators import DataRequired, URL
from datetime import datetime
import unicodedata
import os

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
Bootstrap5(app)

now_date = datetime.now()
format_time = now_date.strftime("%Y-%m-%d")

TODO_FILE = f"{format_time}.txt"


class TodoForm(FlaskForm):
    new_task = StringField('New Task', validators=[DataRequired()])
    submit = SubmitField('Add Task')


def normalize_entry(user_entry):
    # Create a dictionary for specific character replacements
    replacements = {
        'ı': 'i',  # Replace 'ı' with 'i'
        # Add more replacements if needed
    }

    # Normalize the input to remove accents and diacritics
    normalized = unicodedata.normalize('NFKD', user_entry)

    # Replace characters according to the dictionary
    for key, value in replacements.items():
        normalized = normalized.replace(key, value)

    # Remove any remaining non-ASCII characters
    normalized = normalized.encode('ascii', 'ignore').decode('utf-8')

    return normalized


@app.route("/", methods=["GET", "POST"])
def home():

    form = TodoForm()
    title = now_date.strftime("%A, %B %d, %Y")

    # read current tasks from the file
    tasks = []
    if os.path.exists(TODO_FILE):
        with open(TODO_FILE, "r") as file:
            tasks = [line.strip() for line in file.readlines()]

    if request.method == "POST":
        new_task = form.new_task.data
        new_task = normalize_entry(new_task)

        if new_task not in tasks:
            tasks.append(new_task)

        with open(TODO_FILE, "w") as file:
            for task in tasks:
                file.write(task + "\n")

        return redirect(url_for("home"))

    return render_template("index.html", form=form, title=title, tasks=tasks)


@app.route("/delete/<task>")
def delete_task(task):
    tasks = []
    if os.path.exists(TODO_FILE):
        with open(TODO_FILE, "r") as file:
            tasks = [line.strip() for line in file.readlines()]

    if task in tasks:
        tasks.remove(task)

    with open(TODO_FILE, "w") as file:
        for task in tasks:
            file.write(f"{task}\n")

    return redirect(url_for("home"))


if __name__ == "__main__":
    app.run(debug=True)