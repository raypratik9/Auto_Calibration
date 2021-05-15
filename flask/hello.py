from flask import render_template,Flask,request
app = Flask(__name__)

@app.route("/", methods=["POST", "GET"])
def index():
    if request.method == "POST":
        value = request.form["value"]
        print(value)
    return render_template("index.html")


@app.route('/about')
def about():
    return render_template("about.html")
    
if __name__ == '__main__':
    app.run()