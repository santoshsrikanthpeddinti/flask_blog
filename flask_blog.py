from flask import Flask, render_template, url_for

app = Flask(__name__)

posts = [
    {'name': "Blog post1",
     'Author': "santosh",
     'Date': "10/23/2019",
     'Article': "This is introduction to flask"
     },
    {'name': "Blog post2",
     'Author': "santosh",
     'Date': "10/24/2019",
     'Article': "I'm still learning flask"
     }
]


@app.route('/')
@app.route('/home')
def hello():
    return render_template('home.html', posts=posts)


@app.route('/about')
def about():
    return render_template('about.html', title="this is about the blog", details="this is about the details and specs about the blog")
