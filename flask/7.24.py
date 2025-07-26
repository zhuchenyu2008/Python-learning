from flask import Flask,request
app=Flask(__name__)
@app.route('/index',methods=["GET","POST"])
def index():

    name=request.json.get("name")
    print("接受到的name是：",name)
    return "json please"

if __name__== '__main__':
    app.run()