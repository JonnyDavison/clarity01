import os
import json
from flask import Flask, render_template, request, flash, redirect


app = Flask(__name__)


@app.before_request
def before_request():
    scheme = request.headers.get('X-Forwarded-Proto')
    if scheme and scheme == 'http' and request.url.startswith('http://'):
        url = request.url.replace('http://', 'https://', 1)
        code = 301
        return redirect(url, code=code)


@app.before_request
def before_request():
    scheme = request.headers.get('X-Forwarded-Proto')
    if scheme and scheme == '.co.uk' and request.url.endswith('.co.uk'):
        url = request.url.replace('.co.uk', '.com', 1)
        code = 301
        return redirect(url, code=code)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/about")
def about():
    return render_template("about.html", page_title="About")


@app.route("/services")
def services():
    return render_template("services.html", page_title="Services")


@app.route("/contact")
def contact():
    return render_template("contact.html", page_title="Contact")


@app.route("/more")
def more():
    return render_template("more.html", page_title="More")


@app.route("/team")
def team():
    return render_template("team.html", page_title="Team")


@app.route("/testimonials")
def testimonials():
    data = []
    with open("data/testimonials.json", "r") as json_data:
        data = json.load(json_data)
    return render_template('testimonials.html',
                           page_title="Testimonials", testimonials=data)


if __name__ == "__main__":
    app.run(
        host=os.environ.get("IP", "0.0.0.0"),
        port=int(os.environ.get("PORT", "5000")),
        debug=False)
