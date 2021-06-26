from flask import Flask, render_template
import requests

posts= requests.get("https://api.npoint.io/43644ec4f0013682fc0d").json()


app=Flask(__name__)

@app.route('/')
def bget_all_posts():
    return render_template("index.html", all_posts=posts)
@app.route('/about')
def about():
    return render_template("about.html")
@app.route('/contact')
def contact():
    return render_template("contact.html")

@app.route('/post/<int:index>')
def show_post(index):
    requested_post=None
    for post in posts:
        if post['id']==index:
            requested_post=post['id']
    return render_template("post.html", post=requested_post)

if __name__=="__main__":
    app.run(debug=True)   


# export FLASK_APP=main.py
# flask run
