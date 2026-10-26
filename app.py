from flask import Flask,render_template,request,jsonify
import pandas as pd

app=Flask(__name__)


#defining endpoints

@app.route('/',methods=['GET'])
def home():
    return render_template('form.html')


##after hitting submit button this endpoint will be triggered
@app.route('/upload',methods=['POST'])
def get_data():
    file=request.files['file'] # contains all the files data

    print("this is what it contains: ",request.files)
    print("file :",file)

    if file.filename.endswith('.csv'): ##file.filename >>employees salary dataset.csv get extracted
        path="userfile/"+file.filename 
        file.save(path)

        ##read file
        df=pd.read_csv("userfile/employee salary dataset.csv")
        print(df.head())

        ##basic stats:min,max
        min_salary=float(df['salary'].min())
        max_salary=float(df['salary'].max())
        total_Employee=float(df['salary'].count())
        avg_salary=float(df['salary'].mean())

        response={"Min salary":min_salary,
                "Max_salary":max_salary,
                "Toatal Employees":total_Employee,
                "Average Salary":avg_salary}

        return jsonify(response)



    else:

        return "Upload a CSV file only" 

if __name__=='__main__':
    app.run(debug=True)