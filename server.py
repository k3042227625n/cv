from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template('index.html')

@app.route("/picture.html")
def picture():
    return render_template('picture.html')


@app.route("/contact.html")
def contact():
    return render_template('contact.html')

if __name__ == "__main__":
    app.run(debug=True)
