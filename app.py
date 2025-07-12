from flask import Flask, render_template
import api

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")
api.main()
if __name__ == "__main__":
    app.run()