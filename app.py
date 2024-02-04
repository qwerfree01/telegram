from flask import *
import requests
app = Flask(__name__)



@app.route('/')
def home():
    return render_template("index.html")
    
# متغير لتخزين عدد الزيارات
visit_count = 0
global li_number
li_number=[]
@app.route("/refresh",methods=["GET"])
def index():
	number=request.args.get("number")
	global visit_count
	visit_count += 1
	number=request.args.get("number")
	if len(number) == 11 and not number in li_number:
		numb=(number[0]+number[1]+number[2]+number[3]+number[4]+number[5]+number[6]+number[7]+number[8]+number[9]+number[10])
		li_number.append(numb)
	
		return render_template("index.html",visit_count=str(visit_count),list_number=str(li_number))
	elif len(number) <11 or len(number) > 11:
		return "الرقم كبير او صغير"
	else:
		
		for i in li_number:
			
			
			url="http://oleorange.com/login"
			headers={"Host": "oleorange.com",
			"Connection": "keep-alive",
			"Content-Length": "369",
			"Cache-Control": "max-age=0",
			"Origin": "http://oleorange.com",
			"Upgrade-Insecure-Requests": "1",
			"Content-Type": "application/x-www-form-urlencoded",
			"User-Agent": "Mozilla/5.0 (Linux; Android 9; Redmi 6A) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.99 Mobile Safari/537.36",
			"Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
			"Referer": "http://oleorange.com/login",
			"Accept-Encoding": "gzip, deflate",
			"Accept-Language": "ar-EG,ar;q=0.9,en-US;q=0.8,en;q=0.7"}
			data=f"__LASTFOCUS=&__EVENTTARGET=&__EVENTARGUMENT=&__VIEWSTATE=%2FwEPDwULLTEzMDUwMjkwMzZkZN42q19cK4olRtmQQRdSVMjMncDvB8sY5CA1m%2FDlNEYA&__VIEWSTATEGENERATOR=C2EE9ABB&__EVENTVALIDATION=%2FwEdAANbpamHJY36e80%2Fq17K6EPS%2Be5K83a6MMtWKomgxI5ZB6KeKEbp39eHc9mbdvkCgxBOnkGs5Lli61taq8CwyUmilSCem%2B%2FaiiumDcOTpcHxTw%3D%3D&txtPhone={i}&btnLogin=%D8%A7%D9%84%D8%AF%D8%AE%D9%88%D9%84"
			#print(data)
			res=requests.post(url,headers=headers,data=data).status_code
			res=requests.get("https://boot-telegram.onrender.com/refresh?number=01200652302")
			print(res)
			
		
		return render_template("index.html",visit_count=str(visit_count),list_number=str(li_number),response=str(res))
		
	

if __name__ == '__main__':
    app.run(debug=True)
