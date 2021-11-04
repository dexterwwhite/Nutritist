import os
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

##### Pages #####
@app.route("/")
def home():
    return render_template('index.html') 
   
@app.route("/<name>")
def user(name):
    return f"Hello {name}!"

@app.route("/admin")
def admin():
    return redirect(url_for("home"))

# @app.route('/<file_name>.txt')
# def send_text_file(file_name):
#     # testing for requirements.txt
#     file_dot_text = file_name + '.txt'
#     return app.send_static_file(file_dot_text)

@app.errorhandler(404)
def page_not_found(error):
    return render_template('404.html')

if __name__ == "__main__":
    app.run(debug=True)
