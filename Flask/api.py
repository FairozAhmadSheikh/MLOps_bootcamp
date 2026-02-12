# Lets now work with api's 
# building a todo list

from flask import Flask,jsonify,request

app=Flask(__name__)

items=[
    {"id":1,"Name":"Item Name 1","description":"item1 description"},
    {"id":2,"Name":"Item Name 2","description":"item2 description"},
]

@app.route('/')
def home():
    return "Welcome to the todo app"

# Get :all items at once
@app.route('/items')
def items():
    return jsonify(items)

# Get :items at  using id
@app.route('/items/<int:item_id>')
def get_score(item_id):
    item=next((item for item in items if item["id"]==item_id  ),None)
    if item is None:
        return jsonify({"error":"item not found"})
    else:
        return jsonify(items)

# POST: Create a new Task 
@app.route('/items',methods=['POST'])
def create_item():
    if not request.json or not 'name' in request.json:
        return jsonify({"error":"item not found"})
    else:
        new_item={
            "id":items[-1]["id"]+1 ,
            "name":request.json["name"],
            "description":request.json['description']
        }
        items.append(new_item)
        return jsonify(new_item)
    
#PUT:
@app.route('/items/<int:item_id>',methods=['PUT'])
def update_item(item_id):
    item=next((item for item in items if item['id']==item_id),None)
    if item==None:
        return jsonify({"error":"Item not found"})
    else:
        item['name']=request.json('name',item['name'])
        item['description']=request.json('description',item['description'])
        return jsonify({"result":"Item Updated"})
    
# Delete 
@app.route('/items/<int:item_id>',methods=['DELETE'])
def delete_item(item_id):
    global items
    items=[item for item in items if item['id'] != item_id]
    return jsonify({"result":"Item Deleted"})


if __name__=="__main__":
    app.run()