from flask import Flask, render_template
import datetime as dt

app = Flask(__name__)


@app.route("/")
def home_page():
    this_year = dt.datetime.now().strftime("%Y")
    owner_name = "Gokul Thilaak P"
    return render_template("index.html", year=this_year, name=owner_name)


if __name__ == "__main__":
    app.run(debug=True)
