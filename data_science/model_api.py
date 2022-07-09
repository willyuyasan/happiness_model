#imports the python model to process data
from happiness_model import happiness_model

#Creating the API
from flask import Flask, render_template, request
from flask_cors import CORS, cross_origin

app = Flask(__name__)
CORS(app) #Prevent of CORS error when you work from the same server

@cross_origin #Prevent of CORS error when you work from the same server
@app.route('/happiness_model', methods=["GET",'POST'])
def results():
    output = request.get_json()

    print(output)

    if len(output.keys()) < 6:
        return {'status':'Bad input'}
    
    else:
        name = output["name"]
        words = output["words"]
        age = output["age"]
        genre = output["genre"]
        labor_status = output["labor_status"]
        check = output["check"]

        #Uses the python model
        happiness_probability = happiness_model(name,words,age)

        return {'happiness_probability':happiness_probability}

if __name__ == '__main__':
    app.run(host="0.0.0.0",port="5000",debug=True)


