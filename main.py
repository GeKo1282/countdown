make_fg = lambda c: f"\033[31;1;{c}m"

import os
try:
    from flask import Flask, render_template, send_from_directory
except:
    print("Could not import flask! Do you want to install it automatically [y/n]?")
    if input().lower()[0] == "y":
        os.system("pip install flask")
        print(f"{make_fg(93)}Flask installed successfully!{make_fg(0)}")

app = Flask(__name__, template_folder="files")

@app.get("/")
def index():
    return render_template("index.html")

@app.get("/file/<file>")
def file(file):
    return send_from_directory("files", file, mimetype="audio/mp3")

def main():
    app.run(port=5001, debug=True)

if __name__ == "__main__":
    main()