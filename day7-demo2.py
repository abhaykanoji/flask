from form2 import Loginform
from flask import Flask, render_template, redirect, url_for, flash, session, request, make_response

app = Flask(__name__)
app.config["SECRET_KEY"]="mysecretkey"

@app.route("/")
@app.route("/home")
def home():
    return render_template("home6.html", title="home")

@app.route("/about",methods=['get','post'])
def about():
    user_name = request.cookies.get("user_name")
    if user_name is None:
        flash("Login Required!")
        return redirect(url_for('login', next=request.url))
    else:
        flash(f"Hi {user_name}, have a good day!")
    return render_template("about6.html", title="about")


@app.route("/contact",methods=['get','post'])
def contact():
    user_name = request.cookies.get("user_name")
    if user_name is None:
        flash("Login Required!")
        return redirect(url_for('login', next=request.url))
    else:
        flash(f"Hi {user_name}, have a good day!")
    return render_template("contact6.html", title="contact")

@app.route("/login",methods=['get','post'])
def login():
    form = Loginform()
    if form.validate_on_submit():
        user_name = form.username.data
        response = make_response("")
        response.set_cookie("user_name", user_name)
        flash(f"Successfully logged in as {user_name.title()}!")
        next_url = request.args.get("next") or url_for("home")
        response.headers["Location"] = next_url
        response.status_code = 302
        return response
    return render_template("login6.html", title="login",form=form)

@app.route('/logout')
def logout():
    if "user_name" in session:
        session.pop('user_name')
    return redirect(url_for('home'))

if __name__ == "__main__":
    app.run(debug=True)