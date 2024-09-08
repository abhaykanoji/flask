from flask import Flask, render_template, redirect, url_for, flash
from forms import Signupform, Loginform

app = Flask(__name__)
app.config["SECRET_KEY"] = "this_is_a_secret_key"

@app.route("/",methods=["get", "post"])
@app.route("/home",methods=["get", "post"])
def home():
    return render_template("home.html",title="home")

@app.route("/signup",methods=["get","post"])
def signup():
    form = Signupform()
    if form.validate_on_submit():
        flash(f"successfully registerd {form.username.data}!")
        return redirect(url_for("home"))
    return render_template("signup.html", title="signup",form=form)

@app.route("/login",methods=["get","post"])
def login():
    form = Loginform()
    email = form.email.data
    pw = form.password.data
    if form.validate_on_submit():
        # if email == "a@b.com" and pw == "12345":
            # flash("Logged in Successfully!")
        #     return redirect(url_for("home"))
        # else:
        #     flash("Incorrect email or password")
        flash(f"Succesfully login {form.email.data}!")
        return redirect(url_for("home"))
    return render_template("login.html", title="login",form=form)

if __name__ == "__main__":
    app.run(host="0.0.0.0",debug=True)
