from flask import Flask, Response, request
from datetime import datetime
import json
from comment_resource import CommentResource
from post_resource import PostResource
from flask_cors import CORS

# Create the Flask application object.
app = Flask(__name__,
            static_url_path='/',
            static_folder='static/class-ui/',
            template_folder='web/templates')

CORS(app)


@app.route("/comment/<post_id>/post", methods=["GET"])
def get_post(post_id):
    #t = str(datetime.now())
    result = PostResource.get_by_key(post_id)

   
    if result:
        rsp = Response(json.dumps(result,indent=4, sort_keys=True, default=str), status=200, content_type="application.json")
    else:
        rsp = Response("NOT FOUND", status=404, content_type="text/plain")

    return rsp




@app.route("/comment/<comment_id>", methods=["GET"])
def get_comment(comment_id):

    result = CommentResource.get_by_key(comment_id)

    if result:
        rsp = Response(json.dumps(result,indent=4, sort_keys=True, default=str), status=200, content_type="application.json")
    else:
        rsp = Response("NOT FOUND", status=404, content_type="text/plain")

    return rsp

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5011)

