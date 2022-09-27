from flask import Flask, render_template, redirect, url_for
import os


app = Flask(__name__)

@app.get("/")
def home():
    return redirect(url_for("en"))

@app.get("/en")
def en():
    return render_template("home.html")

@app.get('/ru')
def ru():
    return render_template("home_ru.html")

if __name__ == "__main__":
    app.run(debug = False, host='0.0.0.0', port = int(os.environ.get('PORT', 8080)))