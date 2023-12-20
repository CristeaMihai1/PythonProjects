from flask import Flask, render_template, redirect, request, url_for,flash
from werkzeug.security import generate_password_hash

from forms import *
from flask_bootstrap import Bootstrap5
from database import *

app = Flask(__name__)
app.config['SECRET_KEY'] = 'MyKey'
Bootstrap5(app)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/contact", methods=["GET", "POST"])
def get_contact():
    form_message = MessageForm()
    if request.method == "POST":
        new_message = MessageForm(
            name=form_message.name.data,
            email=form_message.email.data,
            phone_number=form_message.phone_number.data,
            message=form_message.message.data
        )
        db.session.add(new_message)
        db.session.commit()
        return redirect(url_for(" "))
    return render_template("contact.html", form=form_message)


@app.route("/create-user",methods=["GET", "POST"])
def get_admin():
    form_create_user = CreateAdmin()
    if form_create_user.validate_on_submit():
        password_hash = generate_password_hash(
            form_create_user.password.data,
            method='pbkdf2:sha256',
            salt_length=8)
        new_admin = Admin(
        email=form_create_user.email.data,
        password=form_create_user.password.data)
        db.session.add(new_admin)
        db.session.commit()
        return ("<h1>Is added</h1>")
    return render_template("create_admin.html", form=form_create_user)

@app.route("/about")
def get_about():
    return render_template("about.html")


@app.route("/service")
def get_service():
    return render_template("service.html")


@app.route("/secret", methods=["GET", "POST"])
def secret_page():
    form_auth = LoginAdmin()
    if form_auth.validate_on_submit():
        email = form_auth.email.data
        password = form_auth.password.data
        result = db.session.executa(db.select(Admin).where(Admin.email == email))
        admin = result.scalar()
        if not admin:
            flash("This email does not exixts")
            return redirect(url_for('secret_page'))

    return render_template("authentication.html",form=form_auth)



if __name__ == "__main__":
    app.run(debug=True)