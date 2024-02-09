from flask import *
from flask_wtf import FlaskForm, RecaptchaField
from wtforms import SubmitField
import json,random,string,os
app = Flask(__name__)
dir_file=(os.getcwd())
try:
	open(dir_file+"/data.json","x")
	open(dir_file+"/code.text","x")
	file=open("data.json","w")
	file.write("{}")
	file.close()
	
	print("file created successfully")
except:
	print("The data was previously saved")
	
app.config['SECRET_KEY'] = 'your_secret_key'
app.config['RECAPTCHA_PUBLIC_KEY'] = '6LdhgGspAAAAAJ1epubkBPbVmoxDkuS0IjVS1j5r'
app.config['RECAPTCHA_PRIVATE_KEY'] = '6LdhgGspAAAAACa4HIeoKE9wio9IKoSUOsQCkU6c'

class CaptchaForm(FlaskForm):
    submit = SubmitField('Submit')
    recaptcha = RecaptchaField()

@app.route('/', methods=['GET', 'POST'])
def index():
    form = CaptchaForm()
    print(form)
    if form.validate_on_submit():
    	name = request.form['name']
    	number = request.form['number']
    	phone = request.form['phone']
    	backage = request.form['backage']
    	date = request.form['data']
    	
    	if len(number) == 11 and len(phone) == 11:
    	       file=open("data.json","r")
    	       js=json.load(file)
    	       add=(len(js.keys()))
    	       js.update({number:[name,phone,backage,date]})
    	       p=json.dumps(js)
    	       #print(p)
    	       file=open("data.json","w")
    	       file.write(str(p))
    	       #return redirect('/')
    	       def i_d(s):
    	       	return "".join(random.choice(string.digits+string.ascii_letters+string.punctuation)for i in range(s))
    	       code=(i_d(8))
    	       with open("code.text",mode="a")as f:
    	       	f.write(str(code+"\n"))
    	       	
    	       	
    	       return render_template_string('''
    	       <center><br>
    	       <h1><font color="green">تم الحجز بنجاح سوف  يتم التواصل بك </font></h><br><br><b>
    	       <h2><i>انسخ الكود واذهب الي بيانات الحجز للتحقق </i></h2><br><br>
    	       {{id}}
    	       <br><br><br><br>
    	       <form action="/">
    	       <input type="submit" id="/" value="اذهب الي الصفحة الرئيسية">
    	       
    	       </form>
    	       
    	       </center>''',id=str(code))
    	else:
        	return '''<center><font color="red"><h1>هناك خطاء في إدخال بيانات الحجز</h1></font></center>'''
    
    
    return render_template("index.html",string="حجز باقات اورانج",form=form)

@app.route("/data",methods=["GET","POS"])
def data():
        if request.method=="GET":
        	number=request.args.get("number")
        	code=request.args.get("code")
        	file=open("code.text","r")
        	f=file.read().splitlines()
        	
        	file=open("data.json","r")
        	js=json.load(file)
        	if code in f and number in js:
        		
        		#return number+str(js[number])
        		return render_template_string('''
        		
        		<!DOCTYPE html>
				<html lang="en">
				<head>
				    <meta charset="UTF-8">
				    <meta name="viewport" content="width=device-width, initial-scale=1.0">
				    <title>Popup Example</title>
				    <link rel="stylesheet" href="/css/styles.css">
				</head>
				<body dir="rtl"><br>
        		<center>
        		{{number}}<br>
        		<div>
        		
				  <table border="1" dir="rtl">
				    <tr><th colspan="2">{{data[0]}}</th></r>
				    <tr><td>رقم حجز الباقة</td><td>{{number}}</td></tr>
				    <tr><td>حجم الباقة</td><td>{{data[2]}}</td></tr>
				    <tr><td>التاريخ</td><td>{{data[3]}}</td></tr>
				    <tr><td>رقم التواصل</td><td>{{data[1]}}</td></tr>
				    
				  </table>
        		</div>
        		
        		<br><br>
        		<form action="/delete" method="post">
        		<h4>الغاء الحجز</h4>
        		<input type="number" name="delete" placeholder="enter number">
        		<br><br>
        		<button type="submit">الغاء الحجز</button>
        		
        		</form>
        		<br><br>
        		<form action="/">
        		
        		<input type="submit" id="/" value="اذهب الي الصفحة الرئيسية">
        		</form>
        		</center>
        		</body>
        		</html>
        		''',number=number,data=js[number])
        	else:
        		return "لا يوجد حجز مسبقا"
        		
@app.route("/delete",methods=["GET","POST"])
def delete():
    if request.method=="POST":
    	delete=request.form["delete"]
    	file=open("data.json","r")
    	js=json.load(file)
    	
    	if delete in js:
    		js.pop(delete)
    		
    		#print(js)
    		file=open("data.json","w")
    		file.write(str(json.dumps(js)))
    		
    		return '''<center><h2>تم الحذف بنجاح</h2></center>'''
    	else:
    		return "<center>لايوجد حجز بهذا الرقم</center>"


@app.route("/control")
def control():
	return render_template("control.html")
	
@app.route("/data_all",methods=["GET","POST"])
def data_all():
	if request.method=="POST":
		user=request.form["username"]
		password=request.form["password"]
		if user == "sherif" and password == "s1h1e1r1i1f1":
			file=open("data.json","r")
			js=json.load(file)
			
			return render_template_string('''
			<!DOCTYPE html>
			<html lang="en">
			<head>
			    <meta charset="UTF-8">
			    <meta name="viewport" content="width=device-width, initial-scale=1.0">
			</head>
			<body align="center" dir="rtl">
			{%for i in data.items()%}
			<div>
			{{i[0]}}<br>
			{{i[1][0]}}<br>
			{{i[1][2]}}<br>
			{{i[1][3]}}<br>
			{{i[1][1]}}
			<hr>
			<div>
			{%endfor%}
			</body>
			</html>
			''',data=js)
			
		else:
			return "<center>error user or password</center>"



if __name__ == '__main__':
    app.run(debug=True)
