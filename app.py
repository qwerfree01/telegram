import telebot
from telebot.types import Message
from telebot.types import InlineKeyboardMarkup
from telebot.types import InlineKeyboardButton
import json
#chat gpt
#import openai
#import requests,time,random
from flask import Flask,render_template,request
#from threading import Thread
import os
app=Flask(__name__)

@app.route("/")
def ref():
	
	return render_template("index.html")
	
@app.route("/send_text",methods=["GET"])
def text():
	key=request.args.get("keys")
	value=request.args.get("value")
	
	file=open("message.json","r")

	file_json=(json.load(file))
	file_json.update({str(key):str(value)})
	#print(file_json)
	
	js=json.dumps(file_json)
	save_file=open("message.json","w")
	file_out=save_file.write(js)
	#print(f"\n{file_json}")
	return render_template("index.html",success="success")

if __name__=="__main__":
			ip=os.environ.get("ip","0.0.0.0")
			port=os.environ.get("port",8080)
			app.run(debug=True,host=ip,port=port)




token="6404262445:AAHD_JvcVN3SHunDMv9EzuoPwKr698YvF74"

bot=telebot.TeleBot(token)

# هنا يمكنك تعريف أوامر البوت
@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, "أهلا بك! كيف يمكنني مساعدتك؟")





@bot.message_handler(func=lambda message: True)
def echo_all(message):
	
	file=open("message.json","r")
	file_json=(json.load(file))
	#file_json.update({"ho":"wel"})
	#print(file_json)
	
	
	bot.reply_to(message,file_json[message.text])
	
	
bot.infinity_polling()