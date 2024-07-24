from flask import Flask
from flask import render_template as renderHTML
import os
import sys
import logging

app = Flask(__name__, template_folder = "", static_folder = "resources")

localPath = os.getcwd() + "\\"
disableLog = False

set = 1
index = 1
data = {}
maxIndexOfSets = {}
sets = os.listdir(localPath + "resources\\panels")
for i in range(len(sets)):
    maxIndexOfSets[str(i + 1)] = len(os.listdir(localPath + f"resources\\panels\\set{i + 1}"))

def loadImages():
    directory = localPath + f"resources\\panels\\set{set}\\{index}"
    imagePaths = sorted(os.listdir(directory), key = lambda imageFile: int(imageFile.split(".")[0]))
    content = ""
    for i in range(len(imagePaths)):
        content = content + f"<img src=\"/resources/panels/set{set}/{index}/{imagePaths[i]}\">"
    return content

@app.route("/")
def main():
    try:
        data["images"] = loadImages()
    except FileNotFoundError:
        sys.exit("No inital images were found! Put some images in suggested path(s).")
    data["info"] = f"set{set} - {index}"
    return renderHTML("index.html", **data)

@app.route("/previousPage")
def previousPage():
    global index, set
    index = index - 1
    if index == 0:
        index = 1
    try:
        data["images"] = loadImages()
    except FileNotFoundError:
         index = index + 1
    data["info"] = f"set{set} - {index}"
    return data

@app.route("/nextPage")
def nextPage():
    global index, set
    index = index + 1
    if index == maxIndexOfSets[str(set)] + 1:
        index = maxIndexOfSets[str(set)]
    try:
        data["images"] = loadImages()
    except FileNotFoundError:
         index = index - 1
    data["info"] = f"set{set} - {index}"
    return data

@app.route("/setChange")
def setChange():
    global index, set
    set = set + 1
    if set == len(maxIndexOfSets) + 1:
        set = 1
    index = 1
    data["info"] = f"set{set} - {index}"
    data["images"] = loadImages()
    return data

if __name__ == "__main__":
    if disableLog:
        log = logging.getLogger("werkzeug")
        log.setLevel(logging.ERROR)
    app.run()
