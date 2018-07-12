from flask import Flask, render_template, request, redirect, url_for
import search

app = Flask(__name__)

app.vars={}

@app.route('/')
def main():
    return redirect('/index')

@app.route('/index', methods=['GET','POST'])
def index():
    if request.method == 'GET':
        return render_template('index.html')
    elif request.method == 'POST':
        app.vars['q'] = request.form["query"]
        if app.vars['q']!=None:
            return redirect('/result')
        else:
            return render_template('index.html')

@app.route('/result', methods=['GET','POST'])
def result():
    if request.method == 'GET':
        return render_template("result.html", table = search.reranking(search.searching(app.vars['q'])))
    elif request.method == 'POST':
        app.vars['q'] = request.form["query"]
        if app.vars['q']!=None:
            return render_template("result.html", table = search.reranking(search.searching(app.vars['q'])))
        else:
            return redirect('/index')

if __name__ == "__main__":
    app.run(debug=True)
