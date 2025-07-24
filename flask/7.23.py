from flask import Flask,request
app = Flask(__name__)
@app.route('/get')
def get():
    name_get = request.args.get("name")
    age_get = request.args.get("age")
    print("get名字是：",name_get)
    print("get年龄是：",age_get)
    return "GET参数为name，age"

@app.route('/post',methods=['POST','get'])
def post():
    name_post = request.form.get("name")
    age_post = request.form.get("age")
    print("post名字是：",name_post)
    print("post年龄是：",age_post)
    return "post参数为name，age"


if __name__ == '__main__':
    app.run()