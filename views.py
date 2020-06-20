"""
Routes and views for the flask application.
"""
from datetime import datetime
from flask import render_template, request
from FoodCourt import app
import os
import glob
#import Process
import webbrowser
import Controller
#import order
from Model import stalls
from shutil import copyfile


#Route
#_____________________________________________________________________________
@app.route('/')
@app.route('/home')
@app.route('/index')
def home():
    """Renders the home page."""
    return render_template(
        'index.html',
        title='Home Page',
        year=datetime.now().year,
    )

@app.route('/menu')
def menu():
    """Renders the menu page."""
@app.route('/account')
def account():
    """Renders the account page."""
    # return render_template(
    #     'menu.html',
    #     'account.html',
    #     # title='Menu Page',
    #     year=datetime.now().year,
    # )

# @app.route('/about')
# def about():
#     """Renders the about page."""
#     return render_template(
#         'about.html',
#         title='About',
#         year=datetime.now().year,
#         message='Your application description page.'
#     )

#kduy fixing
@app.route('/order')
def orderMainIU():
    """Renders the order page."""
    i=0
    tmp = stalls.head
    lst=[]
    while i<2:
        lst.append(tmp)
        tmp=tmp.next
        i+=1
    return render_template(
        'order.html',
        stall = lst,
        year=datetime.now().year,
    )
@app.route('/order<name>')
def stallIU(name):
    """Renders the order page."""
    stall = stalls.findbyName(name)[0]
    files = glob.glob('/images/stall/*')
    for f in files:
        os.remove(f)
    copyfile('static/images/%s' %stall.img,'static/images/stall/stall.jpg')
    food = stall.foodlist
    for f in food:
        copyfile('static/images/%s' %f.img,'static/images/stall/food%d.jpg' %food.index(f))
    return render_template(
        'stall.html',
        stall = stall,
        food = food,
        year=datetime.now().year,
    )

@app.route("/test" , methods=['GET', 'POST'])
def test():
    select = request.form.get('comp_select')
    return(str(select)) # just to see what select is


@app.route('/select', methods = ['POST'])
def pay():
    # webbrowser.open_new('http://127.0.0.1:5000/table')
    v = PayView()
    controller = Controller.Payment(None,None,None,v)
    controller.startPay()
    return render_template('index.html')

#Duy's part_________________________________________________________________________
@app.route('/stallorder')
def stallorder():
    """Renders the order page."""
    return render_template(
        'stallorder.html',
        # title='Menu Page',
        year=datetime.now().year,
        state= "Chua nhan"
        
    )
@app.route('/status')
def status():
    """Renders the order page."""
    return render_template(
        'status.html',
        # title='Menu Page',
        year=datetime.now().year,
    )
@app.route('/detailorder')
def detailorder():
    """Renders the order page."""
    return render_template(
        'detailorder.html',
        # title='Menu Page',
        year=datetime.now().year,
    )
#Duy's end_________________________________________________________________________
#View
#___________________________________________________________________________________

class MainUI:
    pass #Do nothing

class PayView:
    def showPaymentUI(self):
        return render_template('pay.html')
    def showResult(self):
        pass
    def showThirdServiceUI(self):
        pass
    def showQRCode(self,qr):
        return render_template(
            'pay.html',
            qrCode = qr
        )

class OrderView:
    pass #Do nothing