from flask import Flask,render_template,request

app=Flask(__name__)

@app.route("/")
def home():
    return "Welcome to home page"

# using html tags 

@app.route("/homepage")
def homepage():
    return "<html><h1>This is a web page </h1></html>"


# Using Templates
@app.route("/load_from_template")
def load_temp():
    return render_template("loaded.html")

# GET VS POST
@app.route("/form",methods=["GET",'POST'])
def form():
    if request.method=='POST':
        name=request.form['name']
        return f"Hello {name} "
    else:
        return render_template("form.html")

# Building URL Dynamically JinjA 2 Template engine and variable rule


# variable rules
@app.route("/sucess/<score>")
def score(score):
    return f'You got the '+score+" Marks"


if __name__=="__main__":
    app.run(debug=True)

