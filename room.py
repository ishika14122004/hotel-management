from tkinter import*
from PIL import Image, ImageTk 
from tkinter import ttk
import random
from time import strftime
from datetime import datetime
import mysql.connector
from tkinter import messagebox
# from room import RoomBooking


class RoomBooking:
    def __init__(self,root):
        self.root=root
        self.root.title("Hotel Management System")
        self.root.geometry("1295x550+230+220")


        # ========================== Variables ======================
        self.var_contact=StringVar()
        self.var_checkin=StringVar()
        self.var_checkout=StringVar()
        self.var_roomtype=StringVar()
        self.var_roomavailable=StringVar()
        self.var_meal=StringVar()
        self.var_noofdays=StringVar()
        self.var_paidtax=StringVar()
        self.var_actualtotal=StringVar()
        self.var_total=StringVar()


        ###############  title #############################

        lbl_title=Label(self.root,text="ROOM BOOKING DETAILS",font=("times new roman",18,"bold"),bg="black",fg="gold",bd=4,relief=RIDGE)
        lbl_title.place(x=0,y=0,width=1295,height=50)



        ###############  hotellogo   #######################

        # img2=Image.open(r"C:\Users\ASUS\OneDrive\Desktop\python project\Images\Hotel_Logo.jpg")
        # img2=img2.resize((100,40))
        # self.photoimg2=ImageTk.PhotoImage(img2)

        # lblimg=Label(self.root,image=self.photoimg2,bd=0,relief=RIDGE)
        # lblimg.place(x=5,y=2,width=100,height=40)


        ###############  labelframe   #######################
        
        labelframeleft= LabelFrame(self.root,bd=2,relief=RIDGE,text="Room Booking Details" ,font=("times new roman",12, "bold"),padx=2)  
        labelframeleft.place(x=5,y=50,width=425,height=490)



        ###############  label and entry  #######################

        #customer contact
        lbl_cust_contact=Label(labelframeleft,text="Customer Contact",font=("arial",12, "bold"),padx=2,pady=6)
        lbl_cust_contact.grid(row=0,column=0,sticky=W)

        enty_contact= ttk.Entry(labelframeleft, textvariable=self.var_contact,font=("arial",13, "bold"),width=20)
        enty_contact.grid(row=0,column=1,sticky=W)

        # Fetch Data Button
        btnFetchData=Button(labelframeleft,command=self.Fetch_contact,text="Fetch Data",width=8,font=("arial",8, "bold"),bg="black",fg="gold")
        btnFetchData.place(x=347, y=4)


        # Check-in Date
        check_in_date=Label(labelframeleft, font=("arial", 12, "bold"), text="Check_in Date:",padx=2, pady=6)
        check_in_date.grid(row=1,column=0,sticky=W)
        txt_Check_date=ttk.Entry(labelframeleft,textvariable=self.var_checkin,font=("arial", 13, "bold"), width= 29)
        txt_Check_date.grid(row=1, column=1)


        # Check-out Date
        lbl_Check_out=Label(labelframeleft, font=("arial", 12, "bold"), text="Check_Out Date:",padx=2, pady=6)
        lbl_Check_out.grid(row=2,column=0,sticky=W)
        txt_Check_out=ttk.Entry(labelframeleft,textvariable=self.var_checkout,font=("arial", 13, "bold"), width=29)
        txt_Check_out.grid(row=2, column=1)

        #Room Type
        label_RoomType=Label(labelframeleft, font=("arial", 12, "bold"), text="Room Type:", padx=2, pady=6)
        label_RoomType.grid(row=3, column=0, sticky=W)

        conn=mysql.connector.connect(host="localhost", username="root", password="pass123",database="management")
        my_cursor=conn.cursor()
        my_cursor.execute("select RoomType from details")
        ide=my_cursor.fetchall()

        combo_RoomType=ttk.Combobox(labelframeleft,textvariable=self.var_roomtype, font=("arial", 12, "bold"),width=27, state="readonly")
        combo_RoomType["value"] = ide
        combo_RoomType.current(0)
        combo_RoomType.grid(row=3, column=1)

        # Available Room
        lblRoomAvailable=Label(labelframeleft, font=("arial", 12, "bold"), text="Available Room:", padx=2, pady=6)
        lblRoomAvailable.grid(row=4, column=0, sticky=W)
        # txtRoomAvailable=ttk.Entry(labelframeleft,textvariable=self.var_roomavailable, font=("arial", 13, "bold"), width=29)
        # txtRoomAvailable.grid(row=4, column=1)

        conn=mysql.connector.connect(host="localhost", username="root", password="Sevak@3330IITDRMSD",database="management")
        my_cursor=conn.cursor()
        my_cursor.execute("select RoomNo from details")
        rows=my_cursor.fetchall()

        combo_RoomNo=ttk.Combobox(labelframeleft,textvariable=self.var_roomavailable, font=("arial", 12, "bold"),width=27, state="readonly")
        combo_RoomNo["value"] = rows
        combo_RoomNo.current(0)
        combo_RoomNo.grid(row=4, column=1)

        # Meal
        lblMeal=Label(labelframeleft, font=("arial", 12, "bold"), text="Meal:", padx=2, pady=6)
        lblMeal.grid(row=5, column=0, sticky=W)
        txtMeal=ttk.Entry(labelframeleft, textvariable=self.var_meal,font=("arial", 13, "bold"), width=29)
        txtMeal.grid(row=5, column=1)

        # No. of Days
        lblNoOfDays=Label(labelframeleft,font=("arial", 12, "bold"), text="No of Days:", padx=2, pady=6)
        lblNoOfDays.grid(row=6, column=0, sticky=W)
        txtNoOfDays=ttk.Entry(labelframeleft,textvariable=self.var_noofdays, font=("arial", 13, "bold"), width=29)
        txtNoOfDays.grid(row=6, column=1)

        # Paid Tax
        lblNoOfDays=Label(labelframeleft,font=("arial", 12, "bold"), text="Paid Tax:", padx=2, pady=6)
        lblNoOfDays.grid(row=7, column=0, sticky=W)
        txtNoOfDays=ttk.Entry(labelframeleft,textvariable=self.var_paidtax, font=("arial", 13, "bold"), width=29)
        txtNoOfDays.grid(row=7, column=1)

        # Sub Total
        lblNoOfDays=Label(labelframeleft,font=("arial", 12, "bold"), text="Sub Total:", padx=2, pady=6)
        lblNoOfDays.grid(row=8, column=0, sticky=W)
        txtNoOfDays=ttk.Entry(labelframeleft, textvariable=self.var_actualtotal,font=("arial", 13, "bold"), width=29)
        txtNoOfDays.grid(row=8, column=1)

        # Total Cost
        lblIDNumber=Label(labelframeleft, font=("arial", 12, "bold"), text="Total Cost:",padx=2, pady=6)
        lblIDNumber.grid(row=9, column=0,sticky=W)
        txtIDNumber=ttk.Entry(labelframeleft,textvariable=self.var_total,font=("arial", 13, "bold"), width=29)
        txtIDNumber.grid(row=9,column=1)

        #================= Bill Button =====================

        btnBill=Button(labelframeleft,text="Bill",width=10,command=self.total,font=("arial",11, "bold"),bg="black",fg="gold")
        btnBill.grid(row=10,column=0,padx=1,sticky=W)


        #=================below buttons=====================

        btn_frame=Frame(labelframeleft,bd=2,relief=RIDGE) 
        btn_frame.place(x=0,y=400,width=412,height=40)

        btnAdd=Button(btn_frame,text="Add",command=self.add_data,width=10,font=("arial",11, "bold"),bg="black",fg="gold")
        btnAdd.grid(row=0,column=0,padx=1)

        btnUpdate=Button(btn_frame,text="Update",command=self.update,width=10,font=("arial",11, "bold"),bg="black",fg="gold")
        btnUpdate.grid(row=0,column=1,padx=1)

        btnDelete=Button(btn_frame,text="Delete",command=self.cust_Delete,width=10,font=("arial",11, "bold"),bg="black",fg="gold")
        btnDelete.grid(row=0,column=2,padx=1)

        btnReset=Button(btn_frame,text="Reset",command=self.cust_Reset,width=10,font=("arial",11, "bold"),bg="black",fg="gold")
        btnReset.grid(row=0,column=3,padx=1)

        # ======================= Right Side Image ===========================

        # img3=Image.open(r"C:\Users\SEVAK\Downloads\istockphoto-1293415546-612x612.jpg")
        # img3=img3.resize((530,200),Image.ANTIALIAS)
        # self.photoimg3=ImageTk.PhotoImage(img3)

        # lblimg=Label(self.root,image=self.photoimg3,bd=0,relief=RIDGE)
        # lblimg.place(x=760,y=55,width=530,height=200)


        #================tabel frame search ======================

        Table_frame= LabelFrame(self.root,bd=2,relief=RIDGE,text="View Details And Search System",font=("arial",12,"bold") ,padx=2)  
        Table_frame.place(x=435,y=280,width=860,height=260)

        lblSearchBy=Label(Table_frame,font=("arial",12, "bold"),text="Search By:",bg="red",fg="white")
        lblSearchBy.grid(row=0,column=0,sticky=W,padx=2)

        self.search_var=StringVar()

        combo_Search=ttk.Combobox(Table_frame,textvariable=self.search_var,font=("arial",12, "bold"),width=24,state="readonly")
        combo_Search["value"]=("Contact","Room")
        combo_Search.current(0)
        combo_Search.grid(row=0,column=1)

        self.txt_search=StringVar()
        txtSearch= ttk.Entry(Table_frame,textvariable=self.txt_search,width=24,font=("arial",13, "bold"))
        txtSearch.grid(row=0,column=2,padx=2)

        btnSearch=Button(Table_frame,text="Search",width=10,command=self.search,font=("arial",11, "bold"),bg="black",fg="gold")
        btnSearch.grid(row=0,column=5,padx=1)

        btnShowAll=Button(Table_frame,text="Show All",width=10,command=self.fetch_data,font=("arial",11, "bold"),bg="black",fg="gold")
        btnShowAll.grid(row=0,column=4,padx=1)

        # ============================== Show Data Table ===================================
        details_table=Frame(Table_frame,bd=2,relief=RIDGE) 
        details_table.place(x=0,y=55,width=860,height=180)


        scroll_x = ttk.Scrollbar(details_table, orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(details_table, orient=VERTICAL)

        self.Room_Table=ttk.Treeview(details_table, column=("contact","checkin", "checkout", "roomtype", "roomavailable", "meal", "noOfdays"
                                                                    ), xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)
        
        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)

        scroll_x.config(command=self.Room_Table.xview)
        scroll_y.config(command=self.Room_Table.yview)

        self.Room_Table.heading("contact", text="Contact")
        self.Room_Table.heading("checkin", text="Check-in")
        self.Room_Table.heading("checkout", text="Check-out")
        self.Room_Table.heading("roomtype", text="Room Type")
        self.Room_Table.heading("roomavailable", text="Room No")
        self.Room_Table.heading("meal", text="Meal")
        self.Room_Table.heading("noOfdays", text="No Of Days")
        

        self.Room_Table["show"]="headings"

        self.Room_Table.column("contact",width=100)
        self.Room_Table.column("checkin",width=100)
        self.Room_Table.column("checkout",width=100)
        self.Room_Table.column("roomtype",width=100)
        self.Room_Table.column("roomavailable",width=100)
        self.Room_Table.column("meal",width=100)
        self.Room_Table.column("noOfdays",width=100)
        
        self.Room_Table.pack(fill=BOTH,expand=1)
        self.Room_Table.bind("<ButtonRelease-1>", self.get_cursor)
        # self.fetch_data()

    def add_data(self):
        if self.var_contact.get()=="" or self.var_checkin.get()=="":
            messagebox.showerror("Error", "All fields are required", parent=self.root)
        else:
            try:
                conn=mysql.connector.connect(host="localhost", username="root", password="Sevak@3330IITDRMSD",database="management")
                my_cursor=conn.cursor()
                my_cursor.execute("insert into room values(%s, %s, %s, %s, %s, %s, %s, %s)", (
                                                                                                self.var_contact.get(),
                                                                                                self.var_checkin.get(),
                                                                                                self.var_checkout.get(),
                                                                                                self.var_roomtype.get(),
                                                                                                self.var_roomavailable.get(),
                                                                                                self.var_meal.get(),
                                                                                                self.var_noofdays.get()
                                                                                                ))

                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Success", "Room Booked")
            except Exception as es:
                messagebox.showwarning("Warning", f"Something went wrong:{str(es)}",parent=self.root)

    # Fetch Data
                
    def fetch_data(self):
                conn=mysql.connector.connect(host="localhost", username="root", password="Sevak@3330IITDRMSD",database="management")
                my_cursor=conn.cursor()
                my_cursor.execute("select * from room")
                rows=my_cursor.fetchall()
                if len(rows) != 0:
                     self.Room_Table.delete(*self.Cust_Details_Table.get_children())
                     for i in rows:
                          self.Room_Table.insert("",END, values=i)
                     conn.commit()
                conn.close()

    # getcursor
    def get_cursor(self, event=""):
        cursor_row=self.Room_Table.focus()
        content=self.Room_Table.item(cursor_row)
        row=content["values"]

        self.var_contact.set(row[0])
        self.var_checkin.set(row[1])
        self.var_checkout.set(row[2])
        self.var_roomtype.set(row[3])
        self.var_roomavailable.set(row[4])
        self.var_meal.set(row[5])
        self.var_noofdays.set(row[6])

    # update function
        
    def update(self):
        if self.var_contact.get()=="":
            messagebox.showerror("Error", "Please enter mobile number", parent=self.root)
        else:
            conn=mysql.connector.connect(host="localhost", username="root", password="Sevak@3330IITDRMSD",database="management")
            my_cursor=conn.cursor()
            my_cursor.execute("update room set check-in=%s, check-out=%s, roomtype=%s, roomavailable=%s, meal=%s, noOfdays=%s where Contact=%s",
                                                                                                             (
                                                                                                              self.var_checkin.get(),
                                                                                                              self.var_checkout.get(),
                                                                                                              self.var_roomtype.get(),
                                                                                                              self.var_roomavailable.get(),
                                                                                                              self.var_meal.get(),
                                                                                                              self.var_noofdays.get(),
                                                                                                              self.var_contact.get()))
            
            conn.commit()
            self.fetch_data()
            conn.close()
            messagebox.showinfo("Update", "Room details has been updated sucessfully",parent=self.root)
    
    # delete function
    
    def cust_Delete(self):
        cust_Delete=messagebox.askyesno("Hotel Management System", "Do you want to delete this customer", parent= self.root)
        if cust_Delete > 0:
            conn=mysql.connector.connect(host="localhost", username="root", password="Sevak@3330IITDRMSD",database="management")
            my_cursor=conn.cursor()
            query="delete from room where Contact=%s"
            values=(self.var_contact.get(),)
            my_cursor.execute(query, values)
        else:
             if not cust_Delete:
                  return
        conn.commit()
        self.fetch_data()
        conn.close()

    # Reset
    def cust_Reset(self):
        self.var_contact.set("")
        self.var_checkin.set("")
        self.var_checkout.set("")
        self.var_roomtype.set("")
        self.var_roomavailable.set("")
        self.var_meal.set("")
        self.var_noofdays.set("")
        self.var_paidtax.set("")
        self.var_actualtotal.set("")
        self.var_total.set("")

                                                                                                
                    


    # ============================ All Data Fetch =========================================
        
    def Fetch_contact(self):
        if self.var_contact.get()=="":
            messagebox.showerror("Error", "Please enter Contact Number", parent=self.root)
        else:
            conn=mysql.connector.connect(host="localhost", username="root", password="Sevak@3330IITDRMSD",database="management")
            my_cursor=conn.cursor()
            query=("select Name from customer where Mobile=%s")
            value=(self.var_contact.get(),)
            my_cursor.execute(query, value)
            row=my_cursor.fetchone()

            if row==None:
                messagebox.showerror("Error", "This number Not Found", parent=self.root)
            else:
                conn.commit()
                conn.close()

                showDataframe=Frame(self.root, bd=4, relief=RIDGE, padx=2)
                showDataframe.place(x=455, y=55, width=300, height=180)

                lblName=Label(showDataframe, text="Name:", font=("arial", 12, "bold"))
                lblName.place(x=0, y=0)

                lbl=Label(showDataframe, text=row, font=("arial", 12, "bold"))
                lbl.place(x=90, y=0)


                # Gender 

                conn=mysql.connector.connect(host="localhost", username="root", password="Sevak@3330IITDRMSD",database="management")
                my_cursor=conn.cursor()
                query=("select Gender from customer where Mobile=%s")
                value=(self.var_contact.get(),)
                my_cursor.execute(query, value)
                row=my_cursor.fetchone()

                
                lblGender=Label(showDataframe, text="Gender:", font=("arial", 12, "bold"))
                lblGender.place(x=0, y=30)

                lbl2=Label(showDataframe, text=row, font=("arial", 12, "bold"))
                lbl2.place(x=90, y=30)

                # Email

                conn=mysql.connector.connect(host="localhost", username="root", password="Sevak@3330IITDRMSD",database="management")
                my_cursor=conn.cursor()
                query=("select Email from customer where Mobile=%s")
                value=(self.var_contact.get(),)
                my_cursor.execute(query, value)
                row=my_cursor.fetchone()

                
                lblEmail=Label(showDataframe, text="Email:", font=("arial", 12, "bold"))
                lblEmail.place(x=0, y=60)

                lbl3=Label(showDataframe, text=row, font=("arial", 12, "bold"))
                lbl3.place(x=90, y=60)


                # Nationality

                conn=mysql.connector.connect(host="localhost", username="root", password="Sevak@3330IITDRMSD",database="management")
                my_cursor=conn.cursor()
                query=("select Nationality from customer where Mobile=%s")
                value=(self.var_contact.get(),)
                my_cursor.execute(query, value)
                row=my_cursor.fetchone()

                
                lblNationality=Label(showDataframe, text="Nationality:", font=("arial", 12, "bold"))
                lblNationality.place(x=0, y=90)

                lbl4=Label(showDataframe, text=row, font=("arial", 12, "bold"))
                lbl4.place(x=90, y=90)

                # Address

                conn=mysql.connector.connect(host="localhost", username="root", password="Sevak@3330IITDRMSD",database="management")
                my_cursor=conn.cursor()
                query=("select Address from customer where Mobile=%s")
                value=(self.var_contact.get(),)
                my_cursor.execute(query, value)
                row=my_cursor.fetchone()

                
                lblAddress=Label(showDataframe, text="Address:", font=("arial", 12, "bold"))
                lblAddress.place(x=0, y=120)

                lbl5=Label(showDataframe, text=row, font=("arial", 12, "bold"))
                lbl5.place(x=90, y=120)
    
    # Search System
                
    def search(self):
        conn=mysql.connector.connect(host="localhost", username="root", password="Sevak@3330IITDRMSD",database="management")
        my_cursor=conn.cursor()
        my_cursor.execute("select * from room where "+str(self.search_var.get())+"LIKE'%"+str(self.txt_search.get())+"%'")
        rows=my_cursor.fetchall()
        if len(rows) != 0:
             self.Room_Table.delete(*self.Room_Table.get_children())
             for i in rows:
                  self.Room_Table.insert("", END, values=i)
             conn.commit()
        conn.close()


        
    def total(self):
        inDate=self.var_checkin.get()
        outDate=self.var_checkout.get()
        inDate=datetime.strptime(inDate, "%d/%m/%Y")
        outDate=datetime.strptime(outDate, "%d/%m/%Y")
        self.var_noofdays.set(abs(outDate-inDate).days)

        if (self.var_meal.get()=="BreakFast" and self.var_roomtype.get()=="luxury"):
            q1=float(300)
            q2=float(700)
            q3=float(self.var_noofdays.get())
            q4=float(q1 + q2)
            q5=float(q3 + q4)
            Tax="Rs."+str("%.2f"%((q5)*0.1))
            ST="Rs."+str("%.2f"%((q5)))
            TT="Rs."+str("%.2f"%(q5 + ((q5)*0.1)))
            self.var_paidtax.set(Tax)
            self.var_actualtotal.set(ST)
            self.var_total.set(TT)

        elif (self.var_meal.get()=="Lunch" and self.var_roomtype.get()=="Single"):
            q1=float(300)
            q2=float(700)
            q3=float(self.var_noofdays.get())
            q4=float(q1 + q2)
            q5=float(q3 + q4)
            Tax="Rs."+str("%.2f"%((q5)*0.1))
            ST="Rs."+str("%.2f"%((q5)))
            TT="Rs."+str("%.2f"%(q5 + ((q5)*0.1)))
            self.var_paidtax.set(Tax)
            self.var_actualtotal.set(ST)
            self.var_total.set(TT)
        

        elif (self.var_meal.get()=="BreakFast" and self.var_roomtype.get()=="Duplex"):
            q1=float(500)
            q2=float(1000)
            q3=float(self.var_noofdays.get())
            q4=float(q1 + q2)
            q5=float(q3 + q4)
            Tax="Rs."+str("%.2f"%((q5)*0.1))
            ST="Rs."+str("%.2f"%((q5)))
            TT="Rs."+str("%.2f"%(q5 + ((q5)*0.1)))
            self.var_paidtax.set(Tax)
            self.var_actualtotal.set(ST)
            self.var_total.set(TT)


if __name__ == "__main__":
    root=Tk()
    obj=RoomBooking(root) 
    root.mainloop()