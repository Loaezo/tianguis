from flask import Flask, render_template, request, redirect, url_for
import pdb

app = Flask(__name__)


@app.route("/")
def home():
    return render_template('home.html')


@app.route("/item/new", methods=["GET", "POST"])
def new_item():
    if request.method == "POST":
        print("Form data: ")
        print("Title: {}, Description: {}".format(
            request.form.get("title"), request.form.get("description")
        ))
        return redirect(url_for('home'))
    return render_template('new_item.html')