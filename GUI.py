
from tkinter import *
from tkinter import font
import json
import serial



x=320
y=20
try:
    f = open('keyinfo.json')
    jsondata = json.load(f)
except Exception:
    print("no JSON")
try:
    usb_serial = serial.Serial(jsondata['port_name'],9600)
except Exception:
    print("no Serial")


def keypad(passcode):

    def goback():
        global pin
        root.destroy()
        pin = ''
        start()
        print('back')

    def code(value):
        global pin



        # inform function to use external/global variable


        if value == 'Delete':
            # remove last number from `pin`
            pin = pin[:-1]
            # remove all from `entry` and put new `pin`
            e.delete('0', 'end')
            e.insert('end', pin)

        elif value == 'Enter':
            # check pin

            if pin == passcode:
                pin=''
                root.destroy()
                adminPanal()
            else:

                print("PIN ERROR!", pin)
                # clear `pin`
                pin = ''
                # clear `entry`
                e.delete('0', 'end')

        else:

            # add number to pin

            pin += value
            print(pin)
            # add number to `entry`
            e.insert('end', value)



    # --- main ---

    keys = [
        ['1', '2', '3'],
        ['4', '5', '6'],
        ['7', '8', '9'],
        ['Delete', '0', 'Enter'],
    ]

    # create global variable for pin
      # empty string

    root = Tk()
    root.geometry("800x480")

    # place to display pin
    e = Entry(root)
    e.grid(row=0, column=0, columnspan=3, ipady=5)

    backB = Button(root, text="back", command=goback, height=5, width=60)
    backB.grid(row=5, column=0,ipadx=10, ipady=10,columnspan=3)
    # create buttons using `keys`
    for y, row in enumerate(keys, 1):
        for x, key in enumerate(row):
            # `lambda` inside `for` has to use `val=key:code(val)`
            # instead of direct `code(key)`
            b = Button(root, text=key, height=5, width=20, command=lambda val=key: code(val))
            b.grid(row=y, column=x, ipadx=10, ipady=10)
    root.overrideredirect(True)
    root.mainloop()
result=0
pin = ''
num = ''
def keypadset():
    global result
    if result !=0:
        return result
        root.destroy()
    result=0
    def goback():
        global num
        root.destroy()
        num = ''
        start()
        print('back')

    def code(value):

        global num



        # inform function to use external/global variable


        if value == 'Delete':
            # remove last number from `pin`
            num = num[:-1]
            # remove all from `entry` and put new `pin`
            e.delete('0', 'end')
            e.insert('end', num)

        elif value == 'Enter':
            jsondata['Max_distance']=int(num)
            print(jsondata)







        else:

            # add number to pin

            num += value
            print(int(num))
            # add number to `entry`
            e.insert('end', value)



    # --- main ---

    keys = [
        ['1', '2', '3'],
        ['4', '5', '6'],
        ['7', '8', '9'],
        ['Delete', '0', 'Enter'],
    ]

    # create global variable for pin
      # empty string

    root = Tk()
    root.geometry("800x480")

    # place to display pin
    e = Entry(root)
    e.grid(row=0, column=0, columnspan=3, ipady=5)

    backB = Button(root, text="back", command=goback, height=5, width=60)
    backB.grid(row=5, column=0,ipadx=10, ipady=10,columnspan=3)
    # create buttons using `keys`
    for y, row in enumerate(keys, 1):
        for x, key in enumerate(row):
            # `lambda` inside `for` has to use `val=key:code(val)`
            # instead of direct `code(key)`
            b = Button(root, text=key, height=5, width=20, command=lambda val=key: code(val))
            b.grid(row=y, column=x, ipadx=10, ipady=10)
    root.overrideredirect(True)
    root.mainloop()




def adminPanal():


    ws = Tk()
    ws.geometry("800x480")


    def goback():
        ws.destroy()

        start()
        print('back')

    def maxdistance():
        keypadset()




    def printjson():
        print(jsondata['port_name'])


    def killclose():
        ws.destroy()

    maxDistanceButton = Button(ws, text="Set Max Distance", height=5, width=20,command=maxdistance)
    maxDistanceButton.grid(row=0,column=2)
    distanceSpaceButton = Button(ws, text="Set Max Distance", height=5, width=20)
    distanceSpaceButton.grid(row=1,column=2)

    backB = Button(ws, text="back", command=goback, height=5, width=20)
    backB.grid(row=0, column=0)

    printj = Button(ws, text="print json", command=printjson, height=5, width=20)
    printj.grid(row=0, column=1)

    kill = Button(ws, text="close", command=killclose, height=5, width=20)
    kill.grid(row=1, column=0)

    """
    def printInput():
        inp = inputtxt.get(1.0, "end-1c")
        jsondata['port_name'] = inp


    # TextBox Creation
    inputtxt = Text(ws, height=5, width=20, bg='orange')

    inputtxt.grid(row=2, column=1)

    # Button Creation
    
    printButton = Button(ws, text="Change Serial Port", command=printInput, height=5, width=20)
    printButton.grid(row=2, column=0)
    """
    ws.overrideredirect(True)
    ws.mainloop()


'''
def keypad():

    def main():
    root = tkinter.Tk()
    numpad = NumPad(root)
    root.mainloop()


    btn_list = [
    '7',  '8',  '9',
    '4',  '5',  '6',
    '1',  '2',  '3', '0']


    class NumPad(ttk.Frame):
    def __init__(self, root):
        ttk.Frame.__init__(self, root)
        self.grid()
        self.numpad_create()

    def numpad_create(self):
        r = 1
        c = 0
        for b in btn_list:
            cmd= lambda: print(b)
            self.b= ttk.Button(self, text=b,width=5,command=cmd).grid(row=r,column=c)
            print(b)
            c += 1
            if c > 4:
                c = 0
                r += 1


'''










slide_value = 0







#GUIsettings.GetButtonColor()
row0=0


def start():

    root = Tk()
    root.geometry("800x480")

    info_var = StringVar()
    info_var.set("0")

    max_distance = jsondata['Max_distance']

    def SendToUno(distance):

        info_var.set(str(distance))
        print(int(distance*jsondata['rp_multiplier']))
        usb_serial.write(str(distance*jsondata['rp_multiplier']).encode())




    def nextPage():
        root.destroy()
        keypad(jsondata["Passcode"])



    def slide_update(slid_val):
        global slide_value
        slide_value = slid_val



    def senddata():
        global slide_value
        SendToUno(int(slide_value))


    canvis = Canvas(root,width=800,height=480)
    canvis.pack(fill="both",expand=True)




    bg = PhotoImage(file="asset/background.gif")

    canvis.create_image(0,0,image=bg,anchor="nw")

    ft10b = PhotoImage(file= r'asset/10ft.gif')
    ft15b = PhotoImage(file= r'asset/15ft.gif')
    ft20b = PhotoImage(file= r'asset/20ft.gif')
    ft25b = PhotoImage(file= r'asset/25ft.gif')
    ft30b = PhotoImage(file= r'asset/30ft.gif')
    ftMaxb = PhotoImage(file= r'asset/Maxft.gif')

    def f0():
        slider.set(0)
        SendToUno(0)

    def f10():
        slider.set(10)
        SendToUno(10)

    def f15():
        slider.set(15)
        SendToUno(15)

    def f20():
        slider.set(20)
        SendToUno(20)

    def f25():
        slider.set(25)
        SendToUno(25)

    def f30():
        slider.set(30)
        SendToUno(30)

    def fmax():
        slider.set(max_distance)
        SendToUno(max_distance)


    homepic= PhotoImage(file = r"asset/homebutton.gif",)

    """labelPhoto= Label(canvis,image=bg)
    labelPhoto.place(x=0,y=0)"""
    '''
    b10 = Button(canvis,text="10ft",width=10,height=4,command=f10,bg=GUIsettings.GetButtonColor())
    b15 = Button(canvis,text="15ft",bg=GUIsettings.GetButtonColor(),width=10,height=4,command=f15)
    b20 = Button(canvis,text="20ft",bg=GUIsettings.GetButtonColor(),width=10,height=4,command=f20)
    b25 = Button(canvis,text="25ft",bg=GUIsettings.GetButtonColor(),width=10,height=4,command=f25)
    b30 = Button(canvis,text="30ft",bg=GUIsettings.GetButtonColor(),width=10,height=4,command=f30)
    bMax = Button(canvis,text="Max",bg=GUIsettings.GetButtonColor(),width=200,height=4,command=fmax)
    '''
    b10 = Button(canvis,image=ft10b,bg='#C2C2C2',width=200,height=60,command=f10,borderwidth=0, highlightthickness=0)
    b15 = Button(canvis,image=ft15b,bg='#C2C2C2',width=200,height=60,command=f15,borderwidth=0, highlightthickness=0)
    b20 = Button(canvis,image=ft20b,bg='#C2C2C2',width=200,height=60,command=f20,borderwidth=0, highlightthickness=0)
    b25 = Button(canvis,image=ft25b,bg='#979797',width=200,height=60,command=f25,borderwidth=0, highlightthickness=0)
    b30 = Button(canvis,image=ft30b,bg='#979797',width=200,height=60,command=f30,borderwidth=0, highlightthickness=0)
    bMax = Button(canvis,image=ftMaxb,bg='#979797',width=200,height=60,command=fmax,borderwidth=0, highlightthickness=0)

    sliderFont = font.Font(family='arial', size=16, weight='bold')

    sendSlider = Button(canvis,text="Go",bg='white',command=senddata,font=sliderFont,borderwidth=0)

    AdaminButton = Button(canvis,text="Admin",bg='#C2C2C2',width=5,height=1,command=nextPage)



    slider = Scale(canvis,orient=HORIZONTAL ,command=slide_update,from_=0,to_=max_distance,tickinterval=19,bg='white',font=sliderFont)

    distanceinfo = Label(canvis,width=2,height=1,textvariable=info_var,font=font.Font(family="arial",size=30,weight='bold'))

    slidButton=canvis.create_window(570,280,anchor='nw',window=sendSlider,width=100,height=75)

    b_home = Button(canvis,image=homepic,width=303,height=93,borderwidth=0, highlightthickness=0,background="#646464",command=f0)

    button7=canvis.create_window(60,280,anchor="nw", window=slider,width=500,height= 75)

    button1=canvis.create_window(x-190,y,anchor="nw", window=b10)
    button2=canvis.create_window(x*2-190,y,anchor="nw", window=b15)
    button3=canvis.create_window(x-190,y+80,anchor="nw", window=b20)
    button4=canvis.create_window(x*2-190,y+80,anchor="nw", window=b25)
    button5=canvis.create_window(x-190,y+160,anchor="nw", window=b30)
    button6=canvis.create_window(x*2-190,y+160,anchor="nw", window=bMax)
    info=canvis.create_window(700,292,anchor="nw",window=distanceinfo)
    admin=canvis.create_window(740,450,anchor="nw",window=AdaminButton)

    buttonhome=canvis.create_window(5,385,anchor="nw",window=b_home)

    '''
    b10.grid(row=row0,column=0,padx=10)
    b15.grid(row=row0,column=1,padx=10)
    b20.grid(row=row0,column=2,padx=10)
    b25.grid(row=row0,column=3,padx=10)
    b30.grid(row=row0,column=4,padx=10)
    bMax.grid(row=row0,column=5,padx=10)
    
    slider.grid(row=1,column=0,columnspan=6)
    '''

    root.overrideredirect(True)
    root.mainloop()


start()



