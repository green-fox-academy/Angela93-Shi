from flask import Flask
from flask import request
from flask import render_template
from deal_and_clean_data import *
app = Flask(__name__)

@app.route('/')
def welcome():
    return render_template('welcome.html')

@app.route('/assignment',methods=['GET'])
def assigenment():
    return render_template('assignment.html')

@app.route('/data',methods=['GET'])
def data_page():
    return render_template('data.html')

@app.route('/analysis',methods=['GET'])
def analysis_page():
    return render_template('analysis.html')

@app.route('/model',methods=['GET'])
def model_page():
    return render_template('model.html')

@app.route('/base',methods=['GET'])
def base():
    return render_template('base.html')

@app.route("/result", methods=['GET','POST'])
def estate_result():
    if request.method == 'GET':
        holdType = request.args.get("holdType")
        homeType = request.args.get("homeType")
        bedroom = request.args.get("bedroom")
        usage = request.args.get("usage")
        postcode = request.args.get("postcode")
        predict_num = deal_with_result(holdType,homeType,bedroom,usage,postcode)
        return render_template("result.html", result=predict_num,holdType =holdType,homeType=homeType,noBed=bedroom,usage=usage,postcode=postcode)

    elif request.method == 'POST':
        pass

def deal_with_holdType(holdType):
    if holdType == 'Freehold':
        return 1  
    elif holdType == 'Leasehold':
        return 2

def deal_with_homeType(homeType):
    if homeType == 'Semi-Detached':
        return 1
    elif homeType == 'Detached':
        return 2
    elif homeType == 'Terraced':
        return 3
    elif homeType == 'Flat':
        return 4

def deal_with_bedroom(bedroom):
    bedroom = int(bedroom)
    return bedroom

def deal_with_usage(usage):
    if usage == 'Residential':
        return 1
    elif usage == 'Residential(New Build)':
        return 2

def deal_with_postcode(postcode):
    latitude = data_df[data_df['postcode'] == postcode]['latitude'].values[0]
    longitude = data_df[data_df['postcode'] == postcode]['longitude'].values[0]
    return latitude,longitude


def deal_with_result(holdType,homeType,bedroom,usage,postcode):
    holdType = deal_with_holdType(holdType)
    homeType = deal_with_homeType(homeType)
    bedroom = deal_with_bedroom(bedroom)
    usage = deal_with_usage(usage)
    tude = deal_with_postcode(postcode)
    lititude = tude[0]
    longitude = tude[1]
    result = [holdType,homeType,bedroom,usage,lititude,longitude]
    predict_num_init = linear_regression.predict([result])
    predict_num = math.exp(predict_num_init)
    return round(predict_num)


if __name__ == "__main__":
    app.run(debug = True,use_reloader = True)