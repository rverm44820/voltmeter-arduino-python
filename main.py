from tkinter import *
import serial
from tkinter import messagebox

SERIAL_PORT ='COM3'
SERIAL_RATE = 9600
global ttt
global R1
global R2
global vout
global vin


window =Tk()
window.title('DVM')
window.geometry('270x270')


def quit():
    window.quit()

def read_volt():
    R1 = 10000
    R2 = 1000

    try:
        ser = serial.Serial(SERIAL_PORT,SERIAL_RATE)
        print('connected to port')
        reading = ser.readline()
        print('reading  ',float(reading))
        decoded_bytes= str(reading[0:len(reading)-2].decode('utf-8'))
        vout = (float(decoded_bytes))
        print('vout  ',vout)
        #vin = (vout / (R2(R1+R2)))
        #print('vin ',vin)
        new_volt = ('{0:0.2f}'.format(vout))

        lbl_volt.config(text=new_volt)#new_volt
        lbl_volt.after(600,read_volt)

    except:
        print('not found')
        #messagebox.showerror('not found','''\ cannot find  usb  to ttl hit ok to exit''')
        #sys.exit()

lbl_header =Label(window,text='Digital Voltmeter',font=('Helvetica',26))
lbl_header.place(x=130,y=30,anchor=CENTER)

lbl_volt = Label(window,text='0.00',font=('DSEG7 Classic',48))
lbl_volt.place(x=120,y=120,anchor='center')

btn_quit= Button(window,text='Quit',command=quit)
btn_quit.place(relx=0.5,y=200,anchor='center')

btn_start = Button(window,text='start',command=read_volt())
#btn_start.place(relx=0.5,y=230,anchor='center')

window.mainloop()

