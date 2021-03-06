from flask import Flask, request
import os
import logging
import time

app = Flask(__name__, static_url_path='/static') 

# なくてもよい
app.config['UPLOAD_FOLDER'] = './uploaded_files'

app.logger.setLevel(logging.DEBUG)

@app.route('/upload', methods=['POST'])
def upload():
    print('call upload....')
    file = request.files['my_file']
    # メモリ上に全部持っている？500KBより大きいとファイルに出力するようだ
    print(vars(file))
    print(vars(file.stream))
    print(vars(file.stream._file))

    # 小さいファイルのときはfilenoでエラーになる io.UnsupportedOperation: fileno
    #print(file.stream._file.fileno())
    
    #print(file.stream._file.getbuffer().nbytes)
    # C:\\Users\\<OS user name>\\AppData\\Local\\Temp\\tmppky6kkvb みたいな一時ファイルが出力されている
    # Dockerの場合どうなるか
    #print(file.stream._file.name)
    #print(os.stat(file.stream._file.name).st_size)
    #print(file.stream._file.file)
    return 'OK!', 200

@app.route('/hello') 
def hello_world(): 
    return 'Hello to the World of Flask!' 

