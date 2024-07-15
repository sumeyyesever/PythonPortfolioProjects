from flask import Flask, render_template, request, redirect
import smtplib
import os

app = Flask(__name__)

my_email = "sumeysever@gmail.com"
my_password = os.environ["MAIL_PASS"]


@app.route("/", methods=["POST", "GET"])
def home_page():
    if request.method == "GET":
        return render_template("index.html")
    elif request.method == "POST":
        data = request.form
        msg_name = data["name"]
        msg_email = data["email"]
        msg_msg = data["message"]
        send_mail(msg_name, msg_email, msg_msg)
        return redirect("/")


def send_mail(name, mail, message):
    if name != "" and mail != "" and message != "":
        with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
            connection.starttls()
            connection.login(user=my_email, password=my_password)
            connection.sendmail(my_email, my_email, msg=f"Subject:Msg from Portfolio WebSite\n\n{name} - {mail}\n{message}".encode("utf-8"))


if __name__ == "__main__":
    app.run(debug=True)

