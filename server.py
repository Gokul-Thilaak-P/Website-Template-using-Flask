from flask import Flask, render_template
import datetime as dt

app = Flask(__name__)


@app.route("/")
def home_page():
    today = dt.datetime.now()
    this_year = today.strftime("%Y")
    time_now = today.strftime("%X")
    owner_name = "Gokul Thilaak P"
    return render_template("index.html", time=time_now, year=this_year, name=owner_name)


if __name__ == "__main__":
    app.run(debug=True)
