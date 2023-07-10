post = {}
from flask import Flask,jsonify,request

app = Flask(__name__)

@app.route("/")
def welcome():
    return "Hello, World!"

@app.route("/create",methods = ["POST"])
def create_post():
    try:
        data = request.get_json()
        post[data["name"]] = data["caption"]
        post["likes"] = 0
        return jsonify({"msg":"Post has been added successfully"})
    except:
        return jsonify({"msg" : "adding post has been failed"})
    
@app.route("/read",methods = ["GET"])
def READ_post():
    try:
        return jsonify({"msg": post})
    except:
        return jsonify({"msg" : "READING post has been failed"})
    
@app.route("/update",methods = ["PATCH"])
def READ_post():
    try:
        data = request.get_json()
        name = data["name"]
        caption = data["caption"]
        for i in post:
            if name == i:
                post[name] = caption
                break
        return jsonify({"msg": "post is updated successfully"})
    except:
        return jsonify({"msg" : "post is not updated"})
    
@app.route("/delete",methods = ["DELETE"])
def READ_post():
    try:
        data = request.get_json()
        name = data["name"]
        for i in post:
            if name == i:
                del post[name]
                break
        return jsonify({"msg": "post is deleted successfully"})
    except:
        return jsonify({"msg" : "post is not deleted"})

if __name__ == "__main__":
    app.run()