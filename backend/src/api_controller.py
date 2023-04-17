from flask import Blueprint, render_template, request, jsonify, redirect, url_for
from api_services import *

api_controller = Blueprint(__name__, "api_controller") #initialize blueprint

@api_controller.route("/get/allData")
def get_all_data():
    return jsonify(dataframe_to_dict(clean_df))

@api_controller.route("/get/kmeansAllData")
def get_kmeans_all_data():
    everything = [False, False] + [True]*12 #include all 12 meaningful columns
    labels = kmeansWithoutK(everything, clean_df)
    return jsonify(dataframe_to_dict(label_adder(clean_df,labels)))

@api_controller.route("/get/kmeansAllDataTwoClusters")
def get_kmeans_all_data_two_clusters():
    everything = [False, False] + [True]*12 #include all 12 meaningful columns
    labels = kmeansWithK(2, everything, clean_df)
    return jsonify(dataframe_to_dict(label_adder(clean_df,labels)))



@api_controller.route("/")  #API-call ; api_controller.route because variable in line 4 is api_controller
def home():
    return render_template("index.html")

@api_controller.route("/test/<username>") #in french brackets parameter
def test(username): #refering to the parameter
    args = request.args #dictionary to access query parameters
    return render_template("test.html", name=username)

@api_controller.route("/test2")
def test2():
    #via: .../test2?name=tim
    args = request.args #dictionary to access query parameters
    username2 =args.get("username2")
    return render_template("test.html", name=username2)

#test3: returning json ; basic idea: jsonify a python dictionary
@api_controller.route("/jsontest")
def get_json():
    return jsonify( {'name': 'tim',
                     'coolness': 10
    } )

#test4 access json data
@api_controller.route("/datatest", methods=['GET']) #you can add the information about "method is GET"
def get_data():
    data = request.json
    return jsonify(data)

#redirect to different page
@api_controller.route("/go-to-home")
def go_to_home():
    return redirect(url_for("api_controller.home")) #refers to defined function "home"




