from flask import *
from flask_wtf import FlaskForm, RecaptchaField
from wtforms import SubmitField
import json,random,string,os
app = Flask(__name__)
dir_file=(os.getcwd())
try:
	open(dir_file+"/data.json","x")
	#open(dir_file+"/code.text","x")
	open(dir_file+"/stop.text","x")
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
    if form.validate_on_submit():
    	name = request.form['name']
    	number = request.form['number']
    	phone = request.form['phone']
    	backage = request.form['backage']
    	date = request.form['data']
    	file=open("stop.text","r")
    	stop=file.read()
    	
    	if "stop" == stop:
    		return render_template_string("""
    		<!DOCTYPE html>
				<html lang="en">
				<head>
				    <meta charset="UTF-8">
				    <meta name="viewport" content="width=device-width, initial-scale=1.0">
				    <title>Orange backage</title>
				</head>
				<body dir="rtl"><br>
				<h4><i>تم ايقاف الحجز عند توفير الباقات سوف يتم فتح الحجز</i></h4>
				
				</body>
				</html>
    		
    		
    		
    		""")
    	else:
    		
    		if len(number) == 11 and len(phone) == 11:
	    	       file=open("data.json","r")
	    	       js=json.load(file)
	    	       add=(len(js.keys()))
	    	       def i_d(s):
	    	       	return "".join(random.choice(string.digits+string.ascii_letters+string.punctuation)for i in range(s))
	    	       code=(i_d(10))
	    	       
	    	       js.update({number:[name,phone,backage,date,code]})
	    	       p=json.dumps(js)
	    	       #print(p)
	    	       file=open("data.json","w")
	    	       file.write(str(p))
	    	       #return redirect('/')
	    	       
	    	       return render_template_string('''
	    	       <center><br>
	    	       <h2><font color="green">تم الحجز بنجاح سوف  يتم التواصل بك </font></h1><br><br><b>
	    	       <h2><i>انسخ الكود واذهب الي بيانات الحجز للتحقق </i></h1><br><br>
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
        	try:
        		file=open("data.json","r")
	        	js=json.load(file)
	        	if code in js[number] and  number in js:
	        		return render_template("data.html",number=number,data=js[number])
	        	else:
	        		return "<center><h2>لا يوجد حجوزات بهذا الرقم</h2></center>"
        		
        	except:
        		return "<center><h2>لا يوجد حجوزات بهذا الرقم</h2></center>"
        		
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
		if user == "sherif" or user == "ahmed" and password == "ahmed@#$&":
			file=open("data.json","r")
			js=json.load(file)
			
			file=open("stop.text","r")
			reed=file.read()
			return render_template("data_all.html",data=js,len=(len(js.keys())),stop=str(reed))
			
		else:
			return "<center>error user or password</center>"
@app.route("/stop",methods=["GET","POST"])
def stop():
	if request.method=="POST":
		stop=request.form["stop"]
		if stop == "stop" or stop== "open":
			file=open("stop.text","w")
			file.write(str(stop))
			file=open("data.json","r")
			js=json.load(file)
			file=open("stop.text","r")
			reed=file.read()
			return render_template("data_all.html",data=js,len=(len(js.keys())),stop=str(reed))
		else:
			pass
		


if __name__ == '__main__':
    app.run(debug=True)
