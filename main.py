from flask import Flask, render_template, request, json, abort
from func import *

app = Flask(__name__)

POST_PATH = "data/data.json"
POST_COMMENTS = "data/comments.json"

@app.route('/')
def page_index():
    return render_template('index.html', posts=get_posts())


@app.route('/post/<int:post_id>')
def page_post(post_id):
    return render_template('post.html', post=get_post_by_post_id(post_id), comments=get_comments_by_post_id(post_id))

@app.route('/search/')
def page_search():
    search_string = request.args.get('s')
    if not search_string:
        abort(400)
    return render_template('search.html', posts=search_posts(search_string))


@app.route('/users/<username>')
def user_posts(username):
    return render_template('user-feed.html', user_posts=get_user_posts(username))


if __name__ == "__main__":
    app.run(debug=True)