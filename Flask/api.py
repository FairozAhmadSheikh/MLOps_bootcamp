# Lets now work with api's 
# building a todo list

from flask import Flask,jsoinfy,request

app=Flask(__name__)

items=[
    {"id":1,"Name":"Item Name 1","description":"item1 description"},
    {"id":2,"Name":"Item Name 2","description":"item2 description"},
]

@app.route('/')
def home():
    return "Welcome to the todo app"






if __name__=="__main__":
    app.run()