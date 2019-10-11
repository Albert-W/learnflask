from flask import Flask
from flask import jsonify
from flask import request 
from flask import render_template
import json

app = Flask(__name__)

@app.route('/')
def hello():
    # return 'Hello, It is Titan!'
    return render_template('index.html')

# {{url}}/join?id=id4
@app.route('/join', methods=['POST'])
def join():   
    id = request.args.get('id','')
    print(id) 
    return jsonify(request.args)

# {{url}}/join
@app.route('/join1', methods=['POST'])
def join1():
    id = request.form['id']
    print(id)
    return jsonify(id)


# {{url}}/join
@app.route('/join2', methods=['POST'])
def join2():
    print(request)
    id = request.data
    print(id)
    return id

# {{url}}/join
@app.route('/upload', methods=['POST'])
def upload():
    # print(request)
    # print(request.__dict__)
    data = request.files.get('file')
    print(data)
    data.save('receive.txt')
    # abort(404)
    # return jsonify(request.__dict__)
    return 'file is saved'


@app.route('/upload1', methods=['POST'])
def upload1():
    data = request.get_data()
    # data = request.stream.read()
    f = open('receive.md','wb')
    f.write(data)
    f.close()
    # print(data)
    # data.save('receive.ics')
    return "file is stored"
    # return jsonify(data)

@app.route('/upload2', methods=['POST'])
def upload2():
    id = request.form['id']
    return id 




# 路由传递参数,整数
@app.route('/user/<int:user_id>')
def user_info(user_id):
    return 'the num is %d' % user_id

# 路由传递参数,字符串,不指定path默认就是字符串
@app.route('/user/<path:user_id>')
def user_id(user_id):
    return 'hello %s' % user_id    


#异常捕获
@app.errorhandler(404)
def page_not_found(e):
    print(e)
    return "Can't get this resources."


if __name__ == '__main__':
    app.debug = True 
    app.run()