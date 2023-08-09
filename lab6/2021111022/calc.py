from crypt import methods
from flask import Flask, redirect, url_for, request, render_template
app = Flask(__name__)

@app.route('/')
def first():
   return render_template('index.html')

@app.route('/calc/<name>', methods=['POST', 'GET'])
def second(name):
   val1=''
   val2=''
   if request.method=='POST' and 'num1' in request.form and 'num2' in request.form:
      Num1=float(request.form.get('num1'))
      Num2=float(request.form.get('num2'))
      val1 = (Num1+Num2)
      val2 = (Num1*Num2)
   if name == 'sum':
      return render_template('sum.html', val=val1)
   return render_template('mult.html', val=val2)

if __name__ == '__main__':
   app.run(debug=True)
