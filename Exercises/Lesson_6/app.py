from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index_with_button.html", message="Bienvenue sur mon site web!")

@app.route("/about")
def about():
    return render_template("about_with_button.html")

if __name__ == "__main__":
    app.run(debug=True)

