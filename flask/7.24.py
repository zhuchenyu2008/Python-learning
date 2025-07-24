from flask import Flask,request
app=Flask(__name__)
@app.route('/index',methods=["get","POST"])
def index():

    name=request.json.get("name")
    print(name)
    return "json please"

if __name__== '__main__':
    app.run()