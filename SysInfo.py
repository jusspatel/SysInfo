from tkinter import*
import platform
import tkinter.font as tkFont
import tkinter.ttk as ttk
import wmi
from numpy import arange, sin, pi
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
import numpy as np
import matplotlib.pyplot as plt
from psutil import cpu_percent
import psutil
from matplotlib.animation import FuncAnimation
 
c = wmi.WMI()    
my_system = c.Win32_ComputerSystem()[0] 
my = platform.uname()
fig = plt.Figure()

# x-array


root=Tk()
root.configure(bg = "black")
root.geometry('')


def cputusage():
    frame_len = 200
    y = []

    def animate(i) :
        x = psutil.cpu_times()
        z = x.user
        #print(z)
        y.append(z)
        if len(y) <= frame_len:
            plt.cla()
            plt.plot(y , 'r' , label = "CPU")
            
        plt.tight_layout()
    ani = FuncAnimation(plt.gcf() , animate , interval = 1000)
    plt.show()
def memusage():
    frame_len = 200
    y = []

    def animate(i) :
        x = psutil.cpu_freq()
        z = x.current
        y.append(z)
        if len(y) <= frame_len:
            plt.cla()
            plt.plot(y , 'r' , label = "CPU")
            
        plt.tight_layout()
    ani = FuncAnimation(plt.gcf() , animate , interval = 1000)
    plt.show()
def cpuusage():
    #newWindow = Toplevel(root)
    frame_len = 200
    y = []
    def animate(i) : 
        y.append(cpu_percent())
        if len(y) <= frame_len:
            plt.cla()
            plt.plot(y , 'r' , label = "CPU")
            
        plt.tight_layout()
    ani = FuncAnimation(plt.gcf() , animate , interval = 1000)
    plt.show()
def statsusage():
    frame_len = 200
    y = []

    def animate(i) :
        x = psutil.cpu_stats()
        z = x.ctx_switches
        
        y.append(z)
        
        if len(y) <= frame_len:
            plt.cla()
            plt.plot(y , 'r' , label = "CPU")
          
        plt.tight_layout()
    ani = FuncAnimation(plt.gcf() , animate , interval = 1000)
    plt.show()

        

def info():
    root.geometry('640x240')
    root.resizable(False , False)
    fontStyle = tkFont.Font(family="Lucida Grande", size=9)
    label1 = Label(root,text = "Advanced Options" , font = ("Banschrfit" , 15) , fg="white" , bg="black" , width = 15).place(x = 450 , y = 0)
    b1 = ttk.Button(root,text = "Check Current Cpu Usage" , command = cpuusage ,width = 30 ).place(x = 450 , y = 30 )
    b2 = ttk.Button(root,text = "Check Current Cpu \nFrequency (Mhz)" , command = memusage,width = 30 ).place(x = 450 , y = 55)
    b3 = ttk.Button(root,text = "Check No. of Context \nSwitches since boot" , command = statsusage,width = 30 ).place(x = 450 , y = 95)
    b4 = ttk.Button(root,text = "          Check time spent by \nprocesses executing in user mode" , command = cputusage, width = 30 ,).place(x = 450 , y = 135)

    ttk.Separator(root, orient=HORIZONTAL).grid(column=0, row=2, columnspan=3, sticky='ew')
    ttk.Separator(root, orient=HORIZONTAL).grid(column=0, row=4, columnspan=3, sticky='ew')
    ttk.Separator(root, orient=HORIZONTAL).grid(column=0, row=6, columnspan=3, sticky='ew')
    ttk.Separator(root, orient=HORIZONTAL).grid(column=0, row=8, columnspan=3, sticky='ew')
    ttk.Separator(root, orient=HORIZONTAL).grid(column=0, row=10, columnspan=3, sticky='ew')
    ttk.Separator(root, orient=HORIZONTAL).grid(column=0, row=12, columnspan=3, sticky='ew')
    ttk.Separator(root, orient=HORIZONTAL).grid(column=0, row=14, columnspan=3, sticky='ew')
    ttk.Separator(root, orient=HORIZONTAL).grid(column=0, row=16, columnspan=3, sticky='ew')



    ttk.Separator(root, orient=VERTICAL).grid(column=1, row=1, rowspan=18, sticky='ns')


    Label(root,text="System:", bg ="black" , fg = "white").grid(row=1,column=0)
    sys=(f"{my.system}")
    syss.set(sys)
    Label(root,text="",textvariable=syss, bg ="black" , fg = "white").grid(row=1,column=2)
    
    Label(root,text="Name:", bg ="black" , fg = "white").grid(row=3,column=0)
    node1=(f"{my.node}")
    nodee.set(node1)
    Label(root,text="",textvariable=nodee, bg ="black" , fg = "white").grid(row=3,column=2)
    
    Label(root,text="OS Release:", bg ="black" , fg = "white").grid(row=5,column=0)
    node2=(f"{my.release}")
    nodee1.set(node2)
    Label(root,text="",textvariable=nodee1, bg ="black" , fg = "white").grid(row=5,column=2)
    
    Label(root,text="Version:", bg ="black" , fg = "white").grid(row=7,column=0)
    node3=(f"{my.version}")
    nodee2.set(node3)
    Label(root,text="",textvariable=nodee2, bg ="black" , fg = "white").grid(row=7,column=2)
    
    Label(root,text="Machine:", bg ="black" , fg = "white").grid(row=9,column=0)
    node4=(f"{my.machine}")
    nodee3.set(node4)
    Label(root,text="",textvariable=nodee3, bg ="black" , fg = "white").grid(row=9,column=2)
    
    Label(root,text="Processor:", bg ="black" , fg = "white").grid(row=11,column=0)
    node5=(f"{my.processor}")
    nodee4.set(node5)
    Label(root,text="",textvariable=nodee4,font=fontStyle, bg ="black" , fg = "white").grid(row=11,column=2)
    
    Label(root,text="No.Of Processors:", bg ="black" , fg = "white").grid(row=13,column=0)
    node6=(f"{my_system.NumberOfProcessors}")
    nodee5.set(node6)
    Label(root,text="",textvariable=nodee5,font=fontStyle, bg ="black" , fg = "white").grid(row=13,column=2)
    
    Label(root,text="Manufacturer:", bg ="black" , fg = "white").grid(row=15,column=0)
    node7=(f"{my_system.manufacturer}")
    nodee6.set(node7)
    Label(root,text="",textvariable=nodee6,font=fontStyle, bg ="black" , fg = "white").grid(row=15,column=2)
    
    Label(root,text="Model:", bg ="black" , fg = "white").grid(row=17,column=0)
    node8=(f"{my_system.Model}")
    nodee7.set(node8)
    Label(root,text="",textvariable=nodee7,font=fontStyle, bg ="black" , fg = "white").grid(row=17,column=2)
    
syss=StringVar()
nodee=StringVar()
nodee1=StringVar()
nodee2=StringVar()
nodee3=StringVar()
nodee4=StringVar()
nodee5=StringVar()
nodee6=StringVar()
nodee7=StringVar()


b=ttk.Button(root,text="Check",command=info, ).grid(row=0,column=0,ipadx=40,columnspan=2)

root.mainloop()
