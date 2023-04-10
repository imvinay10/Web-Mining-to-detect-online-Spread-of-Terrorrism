# -*- coding: utf-8 -*-

from tkinter import *
from PIL import Image, ImageTk
from tkinter import ttk, messagebox
import pymysql, os

class home_page:
    def __init__(self, root):
         self.window = root
         self.window.title("Welcome to Terrorism Analysis System")
         self.window.geometry("1280x900+0+0")
         self.window.config(bg = "white")
         
         self.bg_img = ImageTk.PhotoImage(file="img3.jpg")
         background = Label(self.window,image=self.bg_img).place(x=0,y=0,relwidth=1,relheight=1)
      
         frame = Frame(self.window, bg="white")
         frame.place(x=350,y=100,width=500,height=550)
         
         title1 = Label(frame, text="Terrorism Detection System", font=("times new roman",25,"bold"),bg="white").place(x=50, y=50)
        

         self.details = Button(frame,text="Enter Details",font=("times new roman",18, "bold"),bd=0,cursor="hand2",bg="green2",fg="white").place(x=120,y=130,width=220)
        
         self.search = Button(frame,text="Post",font=("times new roman",18, "bold"),bd=0,cursor="hand2",bg="green2",fg="white").place(x=120,y=200,width=220)
        

if __name__ == "__main__":
    root = Tk()
    obj = home_page(root)
    root.mainloop()
