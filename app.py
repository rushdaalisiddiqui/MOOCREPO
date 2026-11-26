from flask import Flask,request,render_template
app=Flask(__name__)
@app.route("/")
def home():
    return "welcome to mooc registration!"
@app.route("/register",methods="return")
def register():
    name=request.name["student name"]
    agency=request.name["agency"]
    duration=request.duration["duration"]
    title=request.title["title"]
if __name__=="__main__":
    app.run(debug==True)