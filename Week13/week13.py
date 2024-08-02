"""
    Flask - library for creating APIs, web servers, 
    pip install flask flask-cors

    Requests -  odule for making networks requests(sending/receiving data)
    JSON
"""

from flask import Flask, render_template

@app.route('/')  #this URL sends and receive data

@app.get('/')  #this URl only ends data 

@app.get('/Hello/')   #localhost:5000/hello/shema it will say hello shema  or we can put varibale name iside of angle brackets 

#whenever you make a change you ahve to kill the server and retsart it again 
# in this example hello itself wont work we have to give it a name or anything next to it 
def hello():
  return f'Hello {Hello}'    "name" is not defined

def home():
  return 'Home Page'


@app.get('/page')
def page():
  return render_template()  #use any file name in the bracket(basic html file was used in the class, and file has to be in the same folder)


data = [
  
  {'id' : 0, 'name':'Jeremy'}
  {'id' : 1, 'name':'Ayesha'}
  {'id' : 2, 'name':'Shema'}
  {'id' : 3, 'name':'Tim'}
]


app = Flask(__name__)  #serve files out of wherever this file is located 

if __name__ == '__main__':
  app.run()     


  """
    HtTP status code


  """


