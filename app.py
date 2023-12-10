from flask import Flask, render_template,request
import pickle
model = pickle.load(open('model.pkl','rb'))
app = Flask(__name__)
@app.route("/home")
def home():
    return render_template('home.html')
@app.route("/pred", methods=['POST'])
def make_predict():
    Administrative = request.form['Administrative']
    Administrative_Duration = request.form['Administrative_Duration']
    Informational = request.form['Informational']
    Informational_Duration = request.form['Informational_Duration']
    ProductRelated = request.form['ProductRelated']
    ProductRelated_Duration = request.form['ProductRelated_Duration']
    BounceRates = request.form['BounceRates']
    ExitRates = request.form['ExitRates']
    PageValues = request.form['PageValues']
    SpecialDay = request.form['SpecialDay']
    Month = request.form['Month']
    OperatingSystems = request.form['OperatingSystems']
    Browser = request.form['Browser']
    Region = request.form['Region']
    TrafficType = request.form['TrafficType']
    VisitorType = request.form['VisitorType']
    Weekend = request.form['Weekend']
    total=[[int(Administrative),float(Administrative_Duration),int(Informational),float(Informational_Duration),
           int(ProductRelated),float(ProductRelated_Duration),float(BounceRates),float(ExitRates),float(PageValues),
           float(SpecialDay),int(Month),int(OperatingSystems),int(Browser),int(Region),int(TrafficType),int(VisitorType),
           int(Weekend)]]
    print(total)
    prediction = model.predict(total)
    print(prediction)
    if prediction == 0:
        prediction_txt = 'The visitor is not interested in buying.'
    else:
        prediction_txt = 'The visitor is interested in buying goods.'
    
    print(prediction_txt)
    
    return render_template('submit.html', prediction_txt=prediction_txt)
if __name__ == "__main__":
    app.run(debug=False)