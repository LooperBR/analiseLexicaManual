from flask import Flask,render_template,request
from index import lexer
app = Flask(__name__)

#rendering the HTML page which has the button
@app.route('/')
def json():
    return render_template('main.html')

#background process happening without any refreshing
@app.route('/lexShit',methods = ['GET', 'POST', 'DELETE'])
def lexShit():
    codigo = request.form['text']
    print("codigo: ",codigo)
    result = lexer(codigo)
    return (result)