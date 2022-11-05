from flask import Flask, Response, request
from datetime import datetime
import json
from comment_resource import CommentResource
from flask_cors import CORS

# Create the Flask application object.
app = Flask(__name__,
            static_url_path='/',
            static_folder='static/class-ui/',
            template_folder='web/templates')

CORS(app)


@app.get("/post/a0001")
def get_post():
    #t = str(datetime.now())
    msg = {
        "photo id": "a0001",
        "user id": "a0001",
        "comment id": "a0001"
    }

    # DFF TODO Explain status codes, content type, ... ...
    result = Response(json.dumps(msg), status=200, content_type="application/json")

    return result


@app.route("/post/a0001/comment/", methods=["GET"])
def get_comment(comment_id):

    result = CommentResourceResource.get_by_key(comment_id)

    if result:
        rsp = Response(json.dumps(result), status=200, content_type="application.json")
    else:
        rsp = Response("NOT FOUND", status=404, content_type="text/plain")

    return rsp

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5011)

