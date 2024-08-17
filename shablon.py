from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def films():
    context = {
        "caption" : "Фильмы про Хоббита Бильбо",
        "list" : ["Nina", "Anton", "Anna", "Karina", "Olga"]
    }
    return render_template("shablon.html", **context)

@app.route('/shablon/')
def films2():
    context = {
        "caption": "Фильмы",
        "link": "Перейти в кинотеатрм"
    }
    return render_template("index.html", **context)
@app.route('/person/')
def person():
    return render_template("geroi.html")

if __name__ == '__main__':
    app.run()