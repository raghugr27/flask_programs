# importing libraries
from flask import Flask
from flask_mail import Mail, Message
   
app = Flask(__name__)
mail = Mail(app) # instantiate the mail class
   
# configuration of mail
app.config['MAIL_SERVER']='smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = 'raghutheperfect@gmail.com'
app.config['MAIL_PASSWORD'] = '$Ram@6399$'
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True
mail = Mail(app)
   
# message object mapped to a particular URL ‘/’
@app.route("/")
def index():
   msg = Message(
                'Hello',
                sender ='raghutheperfect@gmail.com',
                recipients = ['raghu27.ramakrishna@gmail.com']
               )
   msg.body = 'hi raghu'
   mail.send(msg)
   return 'Sent'
   
if __name__ == '__main__':
   app.run(debug = True)