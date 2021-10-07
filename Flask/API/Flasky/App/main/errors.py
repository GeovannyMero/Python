from flask import Flask, request
from flask.json import jsonify
from flask.templating import render_template
from werkzeug.wrappers import response

main = Flask(__name__)

@main.app_errorhandler(404)
def page_not_found():
    if request.accept_mimetypes.accept_json and \
        not request.accept_mimetypes.accept_html:
        response = jsonify({'error': 'not found'})
        response .status_code = 404
        return response
    return render_template("404.html"), 404