from flask import Flask, render_template, request, json
from func import get_tags, read_post_json

app = Flask(__name__)

POST_PATH = "data/data.json"
POST_COMMENTS = "data/comments.json"

@app.route('/')
def page_index():
    # posts = read_post_json(POST_PATH)
    # comments = read_post_json(POST_COMMENTS)
    #
    # comments_count=[]
    # for post in posts:
    #     for comment in comments:
    #         if comment.get('post_id') == post.get('pk'):
    #             comments_count.append(comment)

    return render_template('index.html', posts=read_post_json(POST_PATH), comments=read_post_json(POST_COMMENTS))


if __name__ == "__main__":
    app.run(debug=True)