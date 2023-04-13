from flask import Blueprint, render_template, request, jsonify, redirect, url_for

views = Blueprint(__name__, "views") #initialize blueprint

@views.route("/")  #API-call ; views.route because variable in line 3 is views
def home():
    return render_template("index.html")

@views.route("/test/<username>") #in french brackets parameter
def test(username): #refering to the parameter
    args = request.args #dictionary to access query parameters
    return render_template("test.html", name=username)

@views.route("/test2")
def test2():
    #via: .../test2?name=tim
    args = request.args #dictionary to access query parameters
    username2 =args.get("username2")
    return render_template("test.html", name=username2)

#test3: returning json ; basic idea: jsonify a python dictionary
@views.route("/jsontest")
def get_json():
    return jsonify( {'name': 'tim',
                     'coolness': 10
    } )

#test4 access json data
@views.route("/datatest")
def get_data():
    data = request.json
    return jsonify(data)

#redirect to different page
@views.route("/go-to-home")
def go_to_home():
    return redirect(url_for("views.home")) #refers to defined function "home"




