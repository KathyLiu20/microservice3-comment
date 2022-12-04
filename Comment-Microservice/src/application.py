from flask import Flask, Response, request
from datetime import datetime
import json
from comment_resource import CommentResource
from post_resource import PostResource
from flask_cors import CORS
import uuid

# Create the Flask application object.
app = Flask(__name__,
            static_url_path='/',
            static_folder='static/class-ui/',
            template_folder='web/templates')

CORS(app)


@app.route("/comment/<post_id>/post", methods=["GET"])
def get_post(post_id):
    # t = str(datetime.now())
    result = PostResource.get_by_key(post_id)

    if result:
        rsp = Response(json.dumps(result, indent=4, sort_keys=True, default=str), status=200,
                       content_type="application.json")
    else:
        rsp = Response("NOT FOUND", status=404, content_type="text/plain")

    return rsp


@app.route("/comment/<content>", methods=["POST"])
def post_comment(content):
    date = str(datetime.now())

    cid = uuid.uuid1()
    result = CommentResource.post_by_input(cid, date, likes=0, text=content, user='zw2781')
    pid = 'p0001'
    p = PostResource.post_by_info(pid,cid)
    return str(cid)


@app.route("/comment/<comment_id>", methods=["GET"])
def get_comment(comment_id):
    result = CommentResource.get_by_key(comment_id)

    if result:
        rsp = Response(json.dumps(result, indent=4, sort_keys=True, default=str), status=200,
                       content_type="application.json")
    else:
        rsp = Response("NOT FOUND", status=404, content_type="text/plain")

    return rsp


@app.route("/commentlist/<string>", methods=["GET"])
def get_comment_list(string):
    result = string.strip().split(',')
    comment_list = []
    for s in result:
        info = CommentResource.get_by_key(s)
        comment_list.append(info)

    return comment_list


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5011)
