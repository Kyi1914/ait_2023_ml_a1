from flask import Flask, render_template, request
import carprice_prediction

app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template('index.html')

@app.route('/predict',methods=['POST'])
def predict():
    input_features = [float(request.form['engine']),
                      float(request.form['year'])]
    prediction = carprice_prediction.fn_predict(input_features)
    return render_template('index.html',prediction=prediction)

if __name__ == '__main__':
    app.run()