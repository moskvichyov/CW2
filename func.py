import json
import pprint


POST_PATH = "data/data.json"
COMMENTS_PATH = "data/comments.json"


def read_json(filename):
    with open(filename, encoding='utf=8') as f:
        return json.load(f)


def get_comments_by_post_id(post_id):
    all_comments = []
    for comment in read_json(COMMENTS_PATH):
        if comment["post_id"] == post_id:
            all_comments.append(comment)
    return all_comments


def get_posts():
    results = []
    for post in read_json(POST_PATH):
        comments = get_comments_by_post_id(post["pk"])
        post["comments_count"] = len(comments)
        results.append(post)
    return results


def get_post_by_post_id(post_id):
    one_post = []
    for post in read_json(POST_PATH):
        if post['pk'] == post_id:
            one_post.append(post)
        return one_post

