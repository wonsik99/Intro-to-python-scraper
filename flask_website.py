from flask import Flask, render_template, request


app = Flask("JobScrapper")

@app.route("/")
def home():
    return render_template("home.html", name="nico")

@app.route("/search")
def search():
    keyword = request.args.get("keyword")
    return render_template("search.html", keyword=keyword)

app.run("0.0.0.0", port=5001)
