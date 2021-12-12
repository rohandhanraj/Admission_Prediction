
# importing the necessary dependencies
from flask import Flask, render_template, request
from flask_cors import CORS,cross_origin
import pickle


app = Flask(__name__) # initializing a flask app

@app.route('/',methods=['GET'])  # route to display the home page
@cross_origin()
def homePage():
    return render_template("index.html")


@app.route('/predict',methods=['POST','GET']) # route to show the predictions in a web UI
@cross_origin()
def index():
    if request.method == 'POST':
        try:
            #  reading the inputs given by the user
            gre_score = float(request.form['gre_score'])
            toefl_score = float(request.form['toefl_score'])
            university_rating = float(request.form['university_rating'])
            sop = float(request.form['sop'])
            lor = float(request.form['lor'])
            cgpa = float(request.form['cgpa'])
            is_research = 1 if request.form['research'] == 'yes' else 0
            
            filename = 'model.sav'
            # loading the model file from the storage
            loaded_model = pickle.load(open(filename, 'rb'))
            # predictions using the loaded model file
            prediction = loaded_model.predict([[
                gre_score,
                toefl_score,
                university_rating,
                sop,
                lor,
                cgpa,
                is_research
                ]])
            print('Prediction is', prediction)
            # showing the prediction results in a UI
            return render_template('results.html', prediction=round(100*prediction[0]))
        except Exception as e:
            print('The Exception message is: ',e)
            return 'something is wrong'
    # return render_template('results.html')
    else:
        return render_template('index.html')



if __name__ == "__main__":
	app.run(debug=True, host='0.0.0.0') # running the app
    #app.run(host='0.0.0.0', port=9089, debug=True)
    #app.run(debug=True)

