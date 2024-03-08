#code start here--------->
import telebot

bot = telebot.TeleBot('6214968103:AAFwHN0dK2_o_MWYqLnEjZGsOIK72NDRiS4')

 

#commands starts here------------>

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, '''welcome to perso bot!
    /help 
    /learn
    ''')

@bot.message_handler(commands=['learn'])
def learn(message):
    bot.send_message(message.chat.id, ''' Here are the popular topics:
    /python
    /java
    /WebDevelopment
    ''')

@bot.message_handler(commands=['python'])
def python(message):
    bot.send_message(message.chat.id,"""
    --> https://www.youtube.com/watch?v=XKHEtdqhLK8""")

@bot.message_handler(commands=['java'])
def java(message):
    bot.send_message(message.chat.id,""" 
    -->  https://youtu.be/hBh_CC5y8-s""")

@bot.message_handler(commands=['WebDevelopment'])
def WebDevelopment(message):
    bot.send_message(message.chat.id,""" Great! WebDevelopment includes languages like HTML,CSS,JS
    -->  https://youtu.be/6mbwJ2xhgzM""")

#certificate commands start here----------->

@bot.message_handler(commands=['certificates'])
def certificates(message):
    bot.send_message(message.chat.id,''' select the course of certificate you want..
    /Python_beg --> Python - Begineer
    /Python_int --> Python-Intermediate
    /Web_Development
    /Java_beg --> Java - Begineer
    /Java_int --> Java - Intermediate
    /C_Programming1 --> Begineer
    /C_Programming2 --> Intermediate
    
    ''')

#python_beg command ------------>

@bot.message_handler(commands=['Python_beg'])
def Python_beg(message):
    bot.send_message(message.chat.id,''' Here is what you asked!
    https://www.sololearn.com/learn/courses/python-introduction''')

#python_int command ------------>

@bot.message_handler(commands=['Python_int'])
def Python_int(message):
    bot.send_message(message.chat.id,''' Here is what you asked!
    https://www.sololearn.com/learn/courses/python-intermediate''')

#WebDevelopment command --------->

@bot.message_handler(commands=['Web_Development'])
def Web_Development(message):
    bot.send_message(message.chat.id,''' Here is what you asked!
    https://www.sololearn.com/learn/courses/web-development''')

#java_beg command ----------------->

@bot.message_handler(commands=['Java_beg'])
def Java_beg(message):
    bot.send_message(message.chat.id,''' Here is what you asked!
    https://www.sololearn.com/learn/courses/java-introduction''')

@bot.message_handler(commands=['Java_int'])
def Java_int(message):
    bot.send_message(message.chat.id,''' Here is what you asked!
    https://www.sololearn.com/learn/courses/java-intermediate''')


@bot.message_handler(commands=['C_Programming1'])
def C_Programming1(message):
    bot.send_message(message.chat.id,''' Here is what you asked!
    https://www.sololearn.com/learn/courses/c-introduction''')



@bot.message_handler(commands=['C_Programming2'])
def C_Programming2(message):
    bot.send_message(message.chat.id,''' Here is what you asked!
    https://www.sololearn.com/learn/courses/c-intermediate''')




    

#help command starts here------------>

@bot.message_handler(commands=['help'])
def help(message):
    bot.send_message(message.chat.id,""" 
    Hi there!

Welcome to perso bot. I'm here to help you with anything you need, from adding more content to our bot to getting help with your existing content.

Here are some things you can do with my bot:
   
1.Add more content.
2.Get help with your existing content.
3.Report a bug.

   I'm always happy to help, so please don't hesitate to contact me if you have any questions or need any assistance.

   contact:@gamervicky456@gmail.com""")

#syllabus starts here!----------->

@bot.message_handler(commands=['first_year'])
def first_year(message):
    bot.send_message(message.chat.id,''' Sorry! we are Still working on it.We will let you know once it is done ''')

@bot.message_handler(commands=['second_year'])
def second_year(message):
    bot.send_message(message.chat.id,''' Sorry! we are Still working on it.We will let you know once it is done ''')

@bot.message_handler(commands=['third_year'])
def third_year(message):
    bot.send_message(message.chat.id,''' Sorry! we are Still working on it.We will let you know once it is done ''')





bot.polling()