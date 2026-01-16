import webbrowser
from classes import formatedData
from flask import Flask, render_template, request

app = Flask(__name__)

def areInputsValid(studentID, password, borrowDate): #returns a string message to represent what is wrong or to say inputs are valid
    return "error or no error"#placeholder


#idk what working with the server will look like, but using an array of classes might help with format
def sendInfoToServer():
    print()#placeholder

def retrieveInfoFromServer():
    return 



@app.route('/')
def home():
    return render_template("frontend.html", name="FRONT", enabled=False)

@app.route('/submit', methods=(['POST']))
def submit():
    iConName = request.form["iConName"]
    borrowDate = request.form["borrowDate"]#Guaranteed to be in the correct format of yyyy-mm-dd
    fName = request.form["fName"]
    lName = request.form["lName"]
    borrowedEquipment = request.form["borrowedEquipment"]
    print(iConName)
    print(borrowDate)
    print(fName)
    print(lName)
    print(borrowedEquipment)
    return render_template("frontend.html", name="BACK?", enabled=True)


if(__name__ == '__main__'):
    webbrowser.open("http://127.0.0.1:5000")
    app.run(debug=True)

