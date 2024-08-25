from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_bootstrap import Bootstrap5
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Boolean
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, BooleanField
from wtforms.validators import DataRequired

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
Bootstrap5(app)


class Base(DeclarativeBase):
    pass


# initialize the database
db = SQLAlchemy(model_class=Base)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///cafes.db"
db.init_app(app)


# define model
class Cafe(db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String(250), unique=True, nullable=False)
    map_url: Mapped[str] = mapped_column(String(500), nullable=False)
    img_url: Mapped[str] = mapped_column(String(500), nullable=False)
    location: Mapped[str] = mapped_column(String(250), nullable=False)
    seats: Mapped[str] = mapped_column(String(250), nullable=False)
    has_toilet: Mapped[bool] = mapped_column(Boolean, nullable=False)
    has_wifi: Mapped[bool] = mapped_column(Boolean, nullable=False)
    has_sockets: Mapped[bool] = mapped_column(Boolean, nullable=False)
    can_take_calls: Mapped[bool] = mapped_column(Boolean, nullable=False)
    coffee_price: Mapped[str] = mapped_column(String(250), nullable=True)

    def to_dict(self):
        return {column.name: getattr(self, column.name) for column in self.__table__.columns}


# create the model
with app.app_context():
    db.create_all()


class MyForm(FlaskForm):
    name = StringField(label="Cafe Name", validators=[DataRequired()])
    location = StringField(label="Cafe Location", validators=[DataRequired()])
    map_url = StringField(label="Cafe Map URL", validators=[DataRequired()])
    img_url = StringField(label="Cafe Image URL", validators=[DataRequired()])
    coffee_price = StringField(label="Coffee Price", validators=[DataRequired()])
    seats = StringField(label="Cafe Seats Number", validators=[DataRequired()])
    has_toilet = BooleanField('Restrooms')
    has_wifi = BooleanField('Wifi')
    has_sockets = BooleanField('Sockets')
    can_take_calls = BooleanField('Take Calls')
    submit = SubmitField("Submit Cafe")


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/cafes")
def show_cafes():
    result = db.session.execute(db.select(Cafe).order_by(Cafe.name)).scalars()
    all_cafes_list = result.all()
    return render_template("cafes.html", cafes=all_cafes_list)


@app.route("/cafe/<int:cafe_id>")
def show_single_cafe(cafe_id):
    requested_cafe = db.get_or_404(Cafe, cafe_id)
    return render_template("cafe.html", cafe=requested_cafe)


@app.route("/new-cafe", methods=["GET", "POST"])
def add_new_cafe():
    form = MyForm()
    if request.method == "POST":

        new_cafe = Cafe(name=form.name.data, location=form.location.data, img_url=form.img_url.data,
                        map_url=form.map_url.data, coffee_price=form.coffee_price.data, seats=form.seats.data,
                        has_toilet=form.has_toilet.data, has_sockets=form.has_sockets.data, has_wifi=form.has_wifi.data,
                        can_take_calls=form.can_take_calls.data)
        db.session.add(new_cafe)
        db.session.commit()
        return redirect(url_for("show_cafes"))
    return render_template("add-cafe.html", form=form)


@app.route("/delete-cafe/<int:delete_cafe_id>")
def delete_cafe(delete_cafe_id):
    the_cafe = db.get_or_404(Cafe, delete_cafe_id)
    db.session.delete(the_cafe)
    db.session.commit()
    return redirect(url_for("show_cafes"))


if __name__ == "__main__":
    app.run(debug=True)
