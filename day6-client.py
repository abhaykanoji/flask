from form2 import Loginform
from flask import Flask, render_template, redirect, url_for, flash, session, request

app = Flask(__name__)
app.config["SECRET_KEY"]="mysecretkey"

@app.route("/")
@app.route("/home")
def home():
    return render_template("home6.html", title="home")

@app.route("/about",methods=['get','post'])
def about():
    if "user_name" not in session:
        flash("please login.")
        return redirect(url_for("login",next=request.url))
    else:
        flash(f"hi {session['user_name']}, how are you ?")
    return render_template("about6.html", title="about")


@app.route("/contact",methods=['get','post'])
def contact():
    if "user_name" not in session:
        flash("please login.")
        return redirect(url_for('login',next=request.url))
    else:
        flash(f"hi {session['user_name']}, how are you ?")
    return render_template("contact6.html", title="contact")

@app.route("/login",methods=['get','post'])
def login():
    form = Loginform()
    if form.validate_on_submit():
        session['user_name'] = form.username.data
        flash(f"login {session['user_name'].title()}")
        next_url = request.args.get('next')
        return redirect(next_url or url_for('home'))
    return render_template("login6.html", title="login",form=form)

@app.route('/logout')
def logout():
    if "user_name" in session:
        session.pop('user_name')
    return redirect(url_for('home'))

if __name__ == "__main__":
    app.run(debug=True)