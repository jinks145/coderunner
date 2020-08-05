from flask import Flask, render_template
coderunner = Flask(__name__)



@coderunner.route('/')
@coderunner.route('/index')
def main():
    return render_template("index.html")