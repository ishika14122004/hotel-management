from tkinter import *
from tkinter import*
#it is used to make powerful gui model and it has many tool;eg-buttons etc.
from tkinter import ttk
from PIL import Image, ImageTk 
#to add images 
from tkinter import messagebox
import mysql.connector

from customer import Cust_Win
from room import RoomBooking
from details import DetailsRoom




class HotelManagementSystem:
    def _init_(self,root):
        self.root=root
        self.root.title("Hotel Management System")
        self.root.geometry("1500x840+0+0")

#############  above main frame  ####################

        img1=Image.open(r"C:\Users\ASUS\OneDrive\Desktop\python project\Images\hotel.jpg")
        img1=img1.resize((1550,140),Image.ANTIALIAS)
        self.photoimg1=ImageTk.PhotoImage(img1)

        lblimg=Label(self.root,image=self.photoimg1,bd=4,relief=RIDGE)
        lblimg.place(x=0,y=0,width=1550,height=140)




###############  hotel logo   #######################

        img2=Image.open(r"C:\Users\ASUS\OneDrive\Desktop\python project\Images\Hotel left Logo.jpg")
        img2=img2.resize((230,140),Image.ANTIALIAS)
        self.photoimg2=ImageTk.PhotoImage(img2)

        lblimg=Label(self.root,image=self.photoimg2,bd=4,relief=RIDGE)
        lblimg.place(x=0,y=0,width=230,height=140)


 ###############  title #############################
        
        lbl_title=Label(self.root,text="HOTEL MANAGEMENT SYSTEM",font=("times new roman",40,"bold"),bg="black",fg="gold",bd=4,relief=RIDGE)
        lbl_title.place(x=0,y=140,width=1550,height=50)



################  main frame ########################

        main_frame=Frame(self.root,bd=4,relief=RIDGE)
        main_frame.place(x=0,y=190,width=1550,height=620)



################# menu bar #########################
        lbl_menu=Label(main_frame,text="MENU",font=("times new roman",20,"bold"),bg="black",fg="gold",bd=4,relief=RIDGE)
        lbl_menu.place(x=0,y=0,width=230)   



################  button frame ########################

        btn_frame=Frame(main_frame,bd=4,relief=RIDGE)
        btn_frame.place(x=0,y=35,width=230,height=190)
        


########### buttons ############
#here we are using the grid to place the buttons just by specifying the rows and the columns

        cust_btn=Button(btn_frame,text="COSTUMER",command=self.cust_details,width=22,font=("times new roman",14,"bold"),bg="black",fg="gold",bd=0,cursor="hand1")
        cust_btn.grid(row=0,column=0,pady=1)

        room_btn=Button(btn_frame,text="ROOM",command=self.roombooking,width=22,font=("times new roman",14,"bold"),bg="black",fg="gold",bd=0,cursor="hand1")
        room_btn.grid(row=1,column=0,pady=1)


        details_btn=Button(btn_frame,text="DETAILS",command=self.Details_room,width=22,font=("times new roman",14,"bold"),bg="black",fg="gold",bd=0,cursor="hand1")
        details_btn.grid(row=2,column=0,pady=1)

        report_btn=Button(btn_frame,text="REPORT",width=22,font=("times new roman",14,"bold"),bg="black",fg="gold",bd=0,cursor="hand1")
        report_btn.grid(row=3,column=0,pady=1)

        logout_btn=Button(btn_frame,text="LOGOUT",command=self.logout,width=22,font=("times new roman",14,"bold"),bg="black",fg="gold",bd=0,cursor="hand1")
        logout_btn.grid(row=4,column=0,pady=1)



#############################  right side image ##############

        img3=Image.open(r"C:\Users\ASUS\OneDrive\Desktop\python project\Images\hotel.png")
        img3=img3.resize((1310,590),Image.ANTIALIAS)
        self.photoimg3=ImageTk.PhotoImage(img3)

        lblimg1=Label(main_frame,image=self.photoimg3,bd=4,relief=RIDGE)
        lblimg1.place(x=225,y=0,width=1310,height=590)
        


########################## left bottom corner images ##########

        img4=Image.open(r"C:\Users\ASUS\OneDrive\Desktop\python project\Images\hotelfood.png")
        img4=img4.resize((230,210),Image.ANTIALIAS)
        self.photoimg4=ImageTk.PhotoImage(img4)

        lblimg4=Label(main_frame,image=self.photoimg4,bd=4,relief=RIDGE)
        lblimg4.place(x=0,y=225,width=230,height=210)

        
        img5=Image.open(r"C:\Users\ASUS\OneDrive\Desktop\python project\Images\hotel bar.png")
        img5=img5.resize((230,190),Image.ANTIALIAS)
        self.photoimg5=ImageTk.PhotoImage(img5)

        lblimg5=Label(main_frame,image=self.photoimg5,bd=4,relief=RIDGE)
        lblimg5.place(x=0,y=420,width=230,height=190)

    def cust_details(self):
        self.new_window=Toplevel(self.root)
        self.app=Cust_Win(self.new_window)


    def roombooking(self):
        self.new_window=Toplevel(self.root)
        self.app=RoomBooking(self.new_window)

    def Details_room(self):
        self.new_window=Toplevel(self.root)
        self.app=DetailsRoom(self.new_window)


    def logout(self):
        self.root.destroy()
        

if __name__ == "_main_":
    root=Tk()
    obj=HotelManagementSystem(root)
    root.mainloop()                
        




        



        




        

