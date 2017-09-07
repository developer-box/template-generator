#!/usr/bin/env python3
from flask import Flask, Response, request, send_file
from json import dumps
from os import listdir, path

PORT_NUMBER = 8000
MD_TEMPLATE_DIR = "tpls"
SCRIPTS_DIR = "scripts"

app = Flask(__name__, static_folder=SCRIPTS_DIR)


@app.route('/')
def index():
    return send_file("index.html")


@app.route("/list.php")
def list_templates():
    template_content = ""
    requested_file = request.args.get("id")
    md_template_files = sorted([f for f in listdir(MD_TEMPLATE_DIR) if f.endswith(".md")])
    if requested_file in md_template_files:
        try:
            full_path = path.join(MD_TEMPLATE_DIR, requested_file)
            template_content = open(full_path, "r").read()
        except Exception as e:
            print("Failed to read file:", e)
    json_data = dumps({"list": md_template_files, "data": template_content})
    return Response(json_data, mimetype="application/json")


if __name__ == '__main__':
    try:
        # Start the Flask server
        app.run(port=PORT_NUMBER)
    except KeyboardInterrupt:
        pass
