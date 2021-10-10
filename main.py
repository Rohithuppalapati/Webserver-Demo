from flask import render_template,Flask,request,redirect
import csv
app=Flask(__name__)

@app.route('/')
def link1():
    return render_template('index.html')

@app.route('/<string:website>')
def link(website):
    return render_template(website)

def write_to_database(data):
    database=open('database.csv','a',newline='')
    email=data['mail']
    sub=data['subject']
    msg=data['message']
    file = csv.writer(database, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
    file.writerow([email,sub,msg])


@app.route('/submit_form',methods=['POST','GET'])
def submit():
    if request.method == 'POST':
        data=request.form.to_dict()
        write_to_database(data)
        return redirect('/project.html')
    else :
        return "something went wrong"


