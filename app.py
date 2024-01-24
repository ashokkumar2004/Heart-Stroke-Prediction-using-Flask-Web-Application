from flask import Flask, redirect, url_for, request, render_template
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
app = Flask(__name__)

@app.route('/success/<m1>/<m2>/<m3>/<m4>/<m5>/<m6>/<m7>/<m8>/<m9>/<m10>')
def success(m1,m2,m3,m4,m5,m6,m7,m8,m9,m10):
    DS=pd.read_csv(r'C:\Users\Ashok Kumar\Desktop\HeartStrokeFlask\heart.csv')
    DS=DS.replace('Male',0)
    DS=DS.replace('Female',1)
    DS=DS.replace("Other",2)
    DS=DS.replace('Yes',3)
    DS=DS.replace('No',4)
    DS=DS.replace('Urban',5)
    DS=DS.replace('Rural',6)
    DS=DS.replace('Private',7)
    DS=DS.replace('Self-employed',8)
    DS=DS.replace('Govt_job',9)
    DS=DS.replace('children',10)
    DS=DS.replace('Never_worked',11)
    DS=DS.replace('formerly smoked',12)
    DS=DS.replace('never smoked',13)
    DS=DS.replace('smokes',14)
    DS=DS.replace('Unknown',15)
    DS=DS.dropna()
    g=['not Stroke','Stroke']
    li1 = ['Male', 'Female', 'Other', 'Yes', 'No', 'Urban', 'Rural', 'Private', 'Self-employed', 'Govt_job', 'children', 'Never_worked', 'formerly smoked', 'never smoked', 'smokes', 'Unknown']
    li2 = [m1, m2, m3, m4, m5, m6, m7, m8, m9, m10]
    # Create a dictionary to map variable names to their values
    variables = {'m1': m1, 'm2': m2, 'm3': m3, 'm4': m4, 'm5': m5, 'm6': m6, 'm7': m7, 'm8': m8, 'm9': m9, 'm10': m10}
    # Replace values in the dictionary with their corresponding indices from li1
    for var_name, var_value in variables.items():
        if var_value in li1:
            variables[var_name] = li1.index(var_value)
    # Now, update the original variables with the modified values
    m1, m2, m3, m4, m5, m6, m7, m8, m9, m10 = variables.values()
    print(m1, m2, m3, m4, m5, m6, m7, m8, m9, m10)
    y=DS['stroke']  
    x=DS.drop(['stroke','id'],axis=1)  
    x_train, x_test, y_train, y_test = train_test_split(x,y,train_size=0.70,random_state=0)
    DT = RandomForestClassifier()
    DT.fit(x_train,y_train)
    y_pred2 = DT.predict([[m1,m2,m3,m4,m5,m6,m7,m8,m9,m10]]) 
    value=g[y_pred2[0]]
    k=["https://cpr.heart.org/-/media/Images/News/2019/May-2019/0531StrokeSymptoms.jpg?h=601&w=800&hash=13E9AC96B5DBA6F71CDECE67DD04C6A8","https://images.ctfassets.net/pxcfulgsd9e2/articleImage101563/05e291b80b72bf6332662e6fa39d1f9d/Stroke-prevention-HN1410-iStock-1249957366-Cover-Sized.jpg?f=top&fit=fill&fl=progressive&fm=jpg&h=786&q=85&w=1396"]
    g=k[y_pred2[0]]
    return render_template("index.html",value=value,g=g)
    

@app.route('/',methods = ['POST', 'GET'])
def login():
   if request.method == 'POST':
      v1= str(request.form['n1'])
      v2= float( request.form['n2'])
      v3= int(request.form['n3'])
      v4= int(request.form['n4'])
      v5= str(request.form['n5'])
      v6= str(request.form['n6'])
      v7= str(request.form['n7'])
      v8= float(request.form['n8'])
      v9= float(request.form['n9'])
      v10= str(request.form['n10'])
      return redirect(url_for('success',m1=v1,m2=v2,m3=v3,m4=v4,m5=v5,m6=v6,m7=v7,m8=v8,m9=v9,m10=v10))
  

if __name__ == '__main__':
   app.run(debug = True)
