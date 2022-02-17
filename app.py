from flask import Flask, jsonify

app = Flask(__name__)


# Some in-memory database as a list of dicts (each dict is a row)
empDB=[
 {
 'id':'101',
 'name':'Saravanan S',
 'title':'Technical Leader'
 },
 {
 'id':'201',
 'name':'Rajkumar P',
 'title':'Sr Software Engineer'
 }
 ]

# Get all employees
@app.route('/empdb/employee',methods=['GET'])
def getAllEmp():
    return jsonify({'emps':empDB})


# Get employee by employee id
@app.route('/empdb/employee/<empId>',methods=['GET'])
def getEmp(empId):
    usr = [ emp for emp in empDB if (emp['id'] == empId) ] 
    return jsonify({'emp':usr})

# Update 
@app.route('/empdb/employee/<empId>',methods=['PUT'])
def updateEmp(empId): 
    print(f'request.json = {request.json}')
    em = [ emp for emp in empDB if (emp['id'] == empId) ] 
    if 'name' in request.json : 
        em[0]['name'] = request.json['name'] 
    if 'title' in request.json:
        em[0]['title'] = request.json['title'] 
    return jsonify({'emp':em[0]})
    

@app.route("/")
def hello():
    return "Hello World!"


if __name__ == '__main__':
    app.run(debug=True)
