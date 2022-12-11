from flask import Flask, Response, request, jsonify
from datetime import datetime
import json
from comment_resource import CommentResource
from flask_cors import CORS
import shortuuid

# Create the Flask application object.
app = Flask(__name__,
            static_url_path='/',
            static_folder='static/class-ui/',
            template_folder='web/templates')

CORS(app)


@app.route("/comment", methods=["POST"])
def post_comment():
    try:
        # request json from frontend
        comment = request.get_json()
        # generate comment_id,likes and date
        cid = str(shortuuid.ShortUUID().random(length=5))
        likes = 0
        date = str(datetime.now())
        ## post_id = comment['post_id']
        ## poster_id = comment['poster_id']
        ## text = comment['text']
        ## username = comment['username']
        result = CommentResource.post_by_input(comment, cid, date, likes)
        return jsonify({'Success': True})
    except Exception as e:
        print("An error occurred:", e)
        return jsonify({'Failure': True})


@app.route("/comment/<post_id>", methods=["GET"])
def get_comment(post_id):
    result = CommentResource.get_by_key(post_id)

    if result:
        rsp = Response(json.dumps(result, indent=4, sort_keys=True, default=str), status=200,
                       content_type="application.json")
    else:
        rsp = Response("NOT FOUND", status=404, content_type="text/plain")

    return rsp


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5012)
