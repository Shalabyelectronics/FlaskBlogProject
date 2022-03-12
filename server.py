from flask import Flask, render_template, url_for, flash, redirect
from forms import RegistrationForm, LoginForm
import requests
import os

app = Flask(__name__)

app.config["SECRET_KEY"] = os.environ.get("flask_blog_token")

response = requests.get("https://api.npoint.io/bdc8bdc56678a468c5cd")
posts = response.json()


@app.route('/home')
@app.route("/")
def home_page():
    return render_template('index.html', posts=posts)


@app.route('/about')
def about_page():
    return render_template('about.html', title="about")


@app.route('/register', methods=["POST", "GET"])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'Account created for {form.username.data}!', 'success')
        return redirect(url_for('home_page'))
    # if form.errors != {}:
    #     for err_msg in form.errors.values():
    #         print(f'There was an error with creating a user: {err_msg}')
    return render_template('register.html', title='Register', form=form)


@app.route('/login', methods=["POST", "GET"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == "shalaby@m.com" and form.password.data == "123":
            flash("You have been logged in!", "success")
            return redirect(url_for('home_page'))
        else:
            flash("Login Unsuccessful. Please check username and password", "danger")
    return render_template("login.html", title='Log In', form=form)


if __name__ == '__main__':
    app.run(debug=True)
