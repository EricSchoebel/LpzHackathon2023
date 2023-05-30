from flask import Blueprint, render_template, request, jsonify, redirect, url_for
from api_services import *

api_controller = Blueprint(__name__, "api_controller") #initialize blueprint

#---for Wertevergleich
@api_controller.route("/get/allData")
def get_all_data():
    return jsonify(dataframe_to_dict(clean_df))



#---for Clustering
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

# idea: which rows (orsteile) and columns (kategorien) the kmeans is based on, is delivered via encoded strings,
# e.g. kategorien_string = "111000100111"
@api_controller.route("get/kmeansWithk") # /get/kmeansWithk?param1=value1&param2=value2&param3=value3
def get_kmeansWithk_with_inputs():
    k = int(request.args.get("clusteranzahl")) # just a number
    ortsteile_string = request.args.get("ortsteile_string") # string with exactly 63 characters
    kategorien_string = request.args.get("kategorien_string") # string with exactly 12 characters

    included_ortsteile = string_decoder(ortsteile_string) #tells us which rows (from 0 to 62)
    included_kategorien = [False, False] + string_decoder(kategorien_string) #tells us which columns
    relevant_ortsteile_dataframe = create_partial_rows_dataframe(clean_df, included_ortsteile)

    labels = kmeansWithK(k, included_kategorien, relevant_ortsteile_dataframe)

    # after kmeans because kmeans expects dataframe with all 14 columns
    keep_ortsteil = included_kategorien
    keep_ortsteil[1] = True
    relevant_ortsteile_cols_dataframe = create_partial_cols_dataframe(relevant_ortsteile_dataframe, keep_ortsteil)

    return jsonify(dataframe_to_dict(label_adder(relevant_ortsteile_cols_dataframe, labels)))
    # Test with:
    # http://127.0.0.1:5000/get/kmeansWithk?clusteranzahl=3&ortsteile_string=111111111111101000000000010100000000000000000000000000000000000&kategorien_string=111000010000

@api_controller.route("get/kmeansWithoutk") # /get/kmeansWithoutk?param1=value1&param2=value2
def get_kmeansWithoutk_with_inputs():
    ortsteile_string = request.args.get("ortsteile_string")
    kategorien_string = request.args.get("kategorien_string")

    included_ortsteile = string_decoder(ortsteile_string)  # tells us which rows (from 0 to 62)
    included_kategorien = [False, False] + string_decoder(kategorien_string)  # tells us which columns
    relevant_ortsteile_dataframe = create_partial_rows_dataframe(clean_df, included_ortsteile)

    labels = kmeansWithoutK(included_kategorien, relevant_ortsteile_dataframe)

    # after kmeans because kmeans expects dataframe with all 14 columns
    keep_ortsteil = included_kategorien
    keep_ortsteil[1] = True # because second column is Ortsteil
    relevant_ortsteile_cols_dataframe = create_partial_cols_dataframe(relevant_ortsteile_dataframe, keep_ortsteil)

    return jsonify(dataframe_to_dict(label_adder(relevant_ortsteile_cols_dataframe, labels)))  #hint: hiighest label+1 gives you clusteranzahl for frontend



#---for Anomaly Detection
@api_controller.route("get/lof") # /get/lof?param1=value1&param2=value2
def get_lof_with_inputs():
    ortsteile_string = request.args.get("ortsteile_string") # string with exactly 63 characters
    kategorien_string = request.args.get("kategorien_string") # string with exactly 12 characters

    included_ortsteile = string_decoder(ortsteile_string) #tells us which rows (from 0 to 62)
    included_kategorien = [False, False] + string_decoder(kategorien_string) #tells us which columns
    relevant_ortsteile_dataframe = create_partial_rows_dataframe(clean_df, included_ortsteile)

    labels = detectOutliersLOF(included_kategorien, relevant_ortsteile_dataframe)

    keep_ortsteil = included_kategorien
    keep_ortsteil[1] = True
    relevant_ortsteile_cols_dataframe = create_partial_cols_dataframe(relevant_ortsteile_dataframe, keep_ortsteil)

    return jsonify(dataframe_to_dict(label_adder(relevant_ortsteile_cols_dataframe, labels)))
    # Test with:
    # http://127.0.0.1:5000/get/lof?ortsteile_string=111111111100000000000000000000000000000000000000000000000000000&kategorien_string=100000011000











