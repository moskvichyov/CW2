import json
import pprint


POST_PATH = "data/data.json"
POST_COMMENTS = "data/comments.json"


def read_json(filename):
    with open(filename, encoding='utf=8') as f:
        return json.load(f)


def get_comments_by_post_id(post_id):
    all_comments = []
    for comment in read_json(POST_COMMENTS):
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


def get_post_by_post_id(post_id: int):
    for post in read_json(POST_PATH):
        if post['pk'] == post_id:
            comments = get_comments_by_post_id(post["pk"])
            post["comments_count"] = len(comments)
            one_post = post
    return one_post


def search_posts(s: str, limit: int = 10):
    results = []
    for post in read_json(POST_PATH):
        if s in post['content']:
            comments = get_comments_by_post_id(post["pk"])
            posts = get_post_by_post_id(post["pk"])
            post["comments_count"] = len(comments)
            post["posts_count"] = len(posts)
            results.append(post)
            if len(results) == limit:
                break
    return results

def get_user_posts(username):
    user_posts = []
    for post in read_json(POST_PATH):
        if post['poster_name'] == username:
            comments = get_comments_by_post_id(post["pk"])
            post["comments_count"] = len(comments)
            user_posts.append(post)
    return user_posts