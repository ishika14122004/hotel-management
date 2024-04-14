from tkinter import*
# from PIL import Image, ImageTk 
from tkinter import ttk
import random
from time import strftime
from datetime import datetime
import mysql.connector
from tkinter import messagebox

# // from room import RoomBooking //


class DetailsRoom:
    def __init__(self,root):
        self.root=root
        self.root.title("Hotel Management System")
        self.root.geometry("1295x550+230+220")



        ###############  title #############################

        lbl_title=Label(self.root,text="ROOM BOOKING DETAILS",font=("times new roman",18,"bold"),bg="black",fg="gold",bd=4,relief=RIDGE)
        lbl_title.place(x=0,y=0,width=1295,height=50)



        ###############  hotellogo   #######################

        # img2=Image.open(r"C:\Users\ASUS\OneDrive\Desktop\python project\Images\Hotel_Logo.jpg")
        # img2=img2.resize((100,40),Image.ANTIALIAS)
        # self.photoimg2=ImageTk.PhotoImage(img2)

        # lblimg=Label(self.root,image=self.photoimg2,bd=0,relief=RIDGE)
        # lblimg.place(x=5,y=2,width=100,height=40)


        ###############  labelframe   #######################
        
        labelframeleft= LabelFrame(self.root,bd=2,relief=RIDGE,text="New Room Detail" ,font=("times new roman",12, "bold"),padx=2)  
        labelframeleft.place(x=5,y=50,width=540,height=350)


        ###############  label and entry  #######################

        # Floor
        lbl_floor=Label(labelframeleft,text="Floor",font=("arial",12, "bold"),padx=2,pady=6)
        lbl_floor.grid(row=0,column=0,sticky=W, padx=20)
        
        self.var_floor=StringVar()
        enty_floor= ttk.Entry(labelframeleft,textvariable=self.var_floor,font=("arial",13, "bold"),width=20)
        enty_floor.grid(row=0,column=1,sticky=W)



        # Room No
        lbl_RoomNo=Label(labelframeleft, font=("arial", 12, "bold"), text="Room No",padx=2, pady=6)
        lbl_RoomNo.grid(row=1,column=0,sticky=W, padx=20)
        
        self.var_roomNo=StringVar()
        enty_RoomNo= ttk.Entry(labelframeleft,textvariable=self.var_roomNo,font=("arial",13, "bold"),width=20)
        enty_RoomNo.grid(row=1,column=1,sticky=W)

        #Room Type
        label_RoomType=Label(labelframeleft, font=("arial", 12, "bold"), text="Room Type:", padx=2, pady=6)
        label_RoomType.grid(row=2, column=0, sticky=W,padx=20)
        
        self.var_RoomType=StringVar()
        enty_RoomType= ttk.Entry(labelframeleft,textvariable=self.var_RoomType,font=("arial",13, "bold"),width=20)
        enty_RoomType.grid(row=2,column=1,sticky=W)



        #=================below buttons=====================

        btn_frame=Frame(labelframeleft,bd=2,relief=RIDGE) 
        btn_frame.place(x=0,y=200,width=412,height=40)

        btnAdd=Button(btn_frame,text="Add",width=10,command=self.add_data,font=("arial",11, "bold"),bg="black",fg="gold")
        btnAdd.grid(row=0,column=0,padx=1)

        btnUpdate=Button(btn_frame,text="Update",width=10,command=self.update,font=("arial",11, "bold"),bg="black",fg="gold")
        btnUpdate.grid(row=0,column=1,padx=1)

        btnDelete=Button(btn_frame,text="Delete",width=10,command=self.cust_Delete,font=("arial",11, "bold"),bg="black",fg="gold")
        btnDelete.grid(row=0,column=2,padx=1)

        btnReset=Button(btn_frame,text="Reset",width=10,command=self.cust_Reset,font=("arial",11, "bold"),bg="black",fg="gold")
        btnReset.grid(row=0,column=3,padx=1)



        #================tabel frame search ======================

        Table_frame= LabelFrame(self.root,bd=2,relief=RIDGE,text="Show Room Details",font=("arial",12,"bold") ,padx=2)  
        Table_frame.place(x=600,y=55,width=600,height=350)


        scroll_x = ttk.Scrollbar(Table_frame, orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(Table_frame, orient=VERTICAL)

        self.Room_Table=ttk.Treeview(Table_frame, column=("floor", "roomno", "roomType"
                                                                    ), xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)
        
        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)

        scroll_x.config(command=self.Room_Table.xview)
        scroll_y.config(command=self.Room_Table.yview)


        self.Room_Table.heading("floor", text="Floor")
        self.Room_Table.heading("roomno", text="Room No")
        self.Room_Table.heading("roomType", text="Room Type")
        
        

        self.Room_Table["show"]="headings"

        self.Room_Table.column("floor",width=100)
        self.Room_Table.column("roomno",width=100)
        self.Room_Table.column("roomType",width=100)
        
        self.Room_Table.pack(fill=BOTH,expand=1)
        self.Room_Table.bind("<ButtonRelease-1>", self.get_cursor)
        # self.fetch_data()

    def add_data(self):
        if self.var_floor.get()=="" or self.var_RoomType.get()=="":
            messagebox.showerror("Error", "All fields are required", parent=self.root)
        else:
            try:
                conn=mysql.connector.connect(host="localhost", username="root", password="Sevak@3330IITDRMSD",database="management")
                my_cursor=conn.cursor()
                my_cursor.execute("insert into details values(%s, %s, %s)", (
                                                                                                self.var_floor.get(),
                                                                                                self.var_roomNo.get(),
                                                                                                self.var_RoomType.get()
                                                                                                ))

                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Success", "New Room Added Successfully")
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

        self.var_floor.set(row[0])
        self.var_roomNo.set(row[1])
        self.var_RoomType.set(row[2])

    # update function
        
    def update(self):
        if self.var_floor.get()=="":
            messagebox.showerror("Error", "Please enter floor Number", parent=self.root)
        else:
            conn=mysql.connector.connect(host="localhost", username="root", password="Sevak@3330IITDRMSD",database="management")
            my_cursor=conn.cursor()
            my_cursor.execute("update details set Floor=%s, RoomType=%s, RoomNO=%s",
                                                                                (
                                                                                self.var_floor.get(),
                                                                                self.var_roomNo.get(),
                                                                                self.var_RoomType.get()
                                                                                ))
                                                                                                              
            
            conn.commit()
            self.fetch_data()
            conn.close()
            messagebox.showinfo("Update", "New Room details has been updated sucessfully",parent=self.root)    
        
    # delete function
    
    def cust_Delete(self):
        cust_Delete=messagebox.askyesno("Hotel Management System", "Do you want to delete Room Details", parent= self.root)
        if cust_Delete > 0:
            conn=mysql.connector.connect(host="localhost", username="root", password="Sevak@3330IITDRMSD",database="management")
            my_cursor=conn.cursor()
            query="delete from details where RoomNo=%s"
            values=(self.var_roomNo.get(),)
            my_cursor.execute(query, values)
        else:
             if not cust_Delete:
                  return
        conn.commit()
        self.fetch_data()
        conn.close()


    # Reset
    def cust_Reset(self):
        self.var_floor.set("")
        self.var_roomNo.set("")
        self.var_RoomType.set("")




if __name__ == "__main__":
    root=Tk()
    obj=DetailsRoom(root) 
    root.mainloop()