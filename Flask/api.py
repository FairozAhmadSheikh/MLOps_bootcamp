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

# Get all items at once
@app.route('/items')
def items():
    return jsoinfy(items)

# Get items at  using id
@app.route('/items/<int:item_id>')
def get_score(item_id):
    item=next((item for item in items if item["id"]==item_id  ),None)
    if item is None:
        return jsoinfy({"error":"item not found"})
    else:
        return jsoinfy(items)




if __name__=="__main__":
    app.run()