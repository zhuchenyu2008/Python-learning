from flask import Flask,request,jsonify
app = Flask(__name__)
@app.route('/',methods=["GET","POST"])
def index():
    name=request.json.get("name")
    print("name is:",name)

    return jsonify({"name":name})

if __name__ == '__main__':
    app.run()

