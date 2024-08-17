from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def films():
    context = {
        "link": "Перейти в кинотеатр"
    }
    return render_template("index.html", **context)

@app.route('/person/')
def person():
    context = {
        "link": "Перейти в кинотеатр"
    }
    return render_template("geroi.html", **context)

if __name__ == '__main__':
    app.run()