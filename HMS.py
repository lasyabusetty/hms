from tkinter import *
from tkinter import ttk
import tkinter
import mysql.connector
from tkinter import messagebox
import datetime


class HospitalManagementSystem:
    def __init__(self,root):
        self.root=root
        self.root.title("Hospital Management System")
        self.root.geometry("1550x800+0+0")
        #Variable
        self.tabletname_var=StringVar()
        self.refno_var=StringVar()
        self.dose_var=StringVar()
        self.notablet_var=StringVar()
        self.lot_var=StringVar()
        self.issue_var=StringVar()
        self.expiry_var=StringVar()
        self.dailydose_var=StringVar()
        self.sideeffects_var=StringVar()
        self.info_var=StringVar()
        self.bp_var=StringVar()
        self.storage_var=StringVar()
        self.medics_var=StringVar()
        self.pid_var=StringVar()
        self.nhs_var=StringVar()
        self.pname_var=StringVar()
        self.pdob_var=StringVar()
        self.paddress_var=StringVar()
                
        lbltitle=Label(self.root,text="HOSPITAL MANAGEMENT SYSTEM",bg="powder blue",fg="green",bd=10,relief=RIDGE,font=("times new roman",40,"bold"),padx=2,pady=6)
        lblname=Label(self.root,text="",bg="powder blue",fg="green",bd=10,relief=RIDGE,font=("times new roman",10),padx=2,pady=6)
        lbltitle.pack(side=TOP,fill=X)
        lblname.pack(side=TOP,fill=X)
        
        frame=Frame(self.root,bd=12,relief=RIDGE,padx=20,bg="powder blue")
        frame.place(x=0,y=130,width=1530,height=400)
        
        #DataFrameLeft
        DataFrameLeft=LabelFrame(frame,text="Patient Information",bg="powder blue",fg="green",bd=12,relief=RIDGE,font=("times new roman",12,"bold"))
        DataFrameLeft.place(x=0,y=5,width=900,height=350)
        
        lblMembr=Label(DataFrameLeft,bg="powder blue",text="Tablet Name: ",font=("times new roman",12,"bold"),padx=2,pady=6)
        lblMembr.grid(row=0,column=0,sticky=W)
        
        comPatient=ttk.Combobox(DataFrameLeft,textvariable=self.tabletname_var,state="readonly",font=("times new roman",15,"bold"),width=27)
        comPatient["value"]=("Corona Virus", "Dengue","Malaria")
        comPatient.current(0)
        comPatient.grid(row=0,column=1)
        
        lblPRN_No=Label(DataFrameLeft,font=("times new roman",12,"bold"),text="Reference No: ",padx=2,pady=6,bg="powder blue")
        lblPRN_No.grid(row=1,column=0,sticky=W)
        txtPRN_NO=Entry(DataFrameLeft,font=("times new roman",15,"bold"),textvariable=self.refno_var,width=29)
        txtPRN_NO.grid(row=1,column=1)
        
        lblTitle=Label(DataFrameLeft,font=("times new roman",12,"bold"),text="Dose: ",padx=2,pady=6,bg="powder blue")
        lblTitle.grid(row=2,column=0,sticky=W)
        txtTitle=Entry(DataFrameLeft,font=("times new roman",15,"bold"),textvariable=self.dose_var,width=29)
        txtTitle.grid(row=2,column=1)
        
        lblFirstName=Label(DataFrameLeft,font=("times new roman",12,"bold"),text="No. of Tablets: ",padx=2,pady=6,bg="powder blue")
        lblFirstName.grid(row=3,column=0,sticky=W)
        txtFirstName=Entry(DataFrameLeft,font=("times new roman",15,"bold"),textvariable=self.notablet_var,width=29)
        txtFirstName.grid(row=3,column=1)
        
        lblLastName=Label(DataFrameLeft,font=("times new roman",12,"bold"),text="Lot: ",padx=2,pady=6,bg="powder blue")
        lblLastName.grid(row=4,column=0,sticky=W)
        txtLastName=Entry(DataFrameLeft,font=("times new roman",15,"bold"),textvariable=self.lot_var,width=29)
        txtLastName.grid(row=4,column=1)
        
        lblAddress1=Label(DataFrameLeft,font=("times new roman",12,"bold"),text="Issue Date: ",padx=2,pady=6,bg="powder blue")
        lblAddress1.grid(row=5,column=0,sticky=W)
        txtAddress1=Entry(DataFrameLeft,font=("times new roman",15,"bold"),textvariable=self.issue_var,width=29)
        txtAddress1.grid(row=5,column=1)
        
        lblAddress2=Label(DataFrameLeft,font=("times new roman",12,"bold"),text="Expiry Date: ",padx=2,pady=6,bg="powder blue")
        lblAddress2.grid(row=6,column=0,sticky=W)
        txtAddress2=Entry(DataFrameLeft,font=("times new roman",15,"bold"),textvariable=self.expiry_var,width=29)
        txtAddress2.grid(row=6,column=1)
        
        lblPostalCode=Label(DataFrameLeft,font=("times new roman",12,"bold"),text="Daily Dose: ",padx=2,pady=6,bg="powder blue")
        lblPostalCode.grid(row=7,column=0,sticky=W)
        txtPostalCode=Entry(DataFrameLeft,font=("times new roman",15,"bold"),textvariable=self.dailydose_var,width=29)
        txtPostalCode.grid(row=7,column=1)
        
        lblMobile=Label(DataFrameLeft,font=("times new roman",12,"bold"),text="Side Effects: ",padx=2,pady=6,bg="powder blue")
        lblMobile.grid(row=8,column=0,sticky=W)
        txtMobile=Entry(DataFrameLeft,font=("times new roman",15,"bold"),textvariable=self.sideeffects_var,width=29)
        txtMobile.grid(row=8,column=1)
        
        lblBookId=Label(DataFrameLeft,font=("times new roman",12,"bold"),text="Further Information: ",padx=2,pady=6,bg="powder blue")
        lblBookId.grid(row=0,column=2,sticky=W)
        txtBookId=Entry(DataFrameLeft,font=("times new roman",15,"bold"),textvariable=self.info_var,width=29)
        txtBookId.grid(row=0,column=3)
        
        lblBookTitle=Label(DataFrameLeft,font=("times new roman",12,"bold"),text="Blood Pressure: ",padx=2,pady=6,bg="powder blue")
        lblBookTitle.grid(row=1,column=2,sticky=W)
        txtBookTitle=Entry(DataFrameLeft,font=("times new roman",15,"bold"),textvariable=self.bp_var,width=29)
        txtBookTitle.grid(row=1,column=3)
        
        lblAuthor=Label(DataFrameLeft,font=("times new roman",12,"bold"),text="Storage Advice: ",padx=2,pady=6,bg="powder blue")
        lblAuthor.grid(row=2,column=2,sticky=W)
        txtAuthor=Entry(DataFrameLeft,font=("times new roman",15,"bold"),textvariable=self.storage_var,width=29)
        txtAuthor.grid(row=2,column=3)
        
        lblDateBorrowed=Label(DataFrameLeft,font=("times new roman",12,"bold"),text="Medications: ",padx=2,pady=6,bg="powder blue")
        lblDateBorrowed.grid(row=3,column=2,sticky=W)
        txtDateBorrowed=Entry(DataFrameLeft,font=("times new roman",15,"bold"),textvariable=self.medics_var,width=29)
        txtDateBorrowed.grid(row=3,column=3)
        
        lblDateDue=Label(DataFrameLeft,font=("times new roman",12,"bold"),text="Patient ID: ",padx=2,pady=6,bg="powder blue")
        lblDateDue.grid(row=4,column=2,sticky=W)
        txtDateDue=Entry(DataFrameLeft,font=("times new roman",15,"bold"),textvariable=self.pid_var,width=29)
        txtDateDue.grid(row=4,column=3)
        
        lblDaysOnBook=Label(DataFrameLeft,font=("times new roman",12,"bold"),text="NHS No.: ",padx=2,pady=6,bg="powder blue")
        lblDaysOnBook.grid(row=5,column=2,sticky=W)
        txtDaysOnBook=Entry(DataFrameLeft,font=("times new roman",15,"bold"),textvariable=self.nhs_var,width=29)
        txtDaysOnBook.grid(row=5,column=3)
        
        lblLateReturnFine=Label(DataFrameLeft,font=("times new roman",12,"bold"),text="Patient Name: ",padx=2,pady=6,bg="powder blue")
        lblLateReturnFine.grid(row=6,column=2,sticky=W)
        txtLateReturnFine=Entry(DataFrameLeft,font=("times new roman",15,"bold"),textvariable=self.pname_var,width=29)
        txtLateReturnFine.grid(row=6,column=3)
        
        lblDateOverDue=Label(DataFrameLeft,font=("times new roman",12,"bold"),text="Patient D.O.B: ",padx=2,pady=6,bg="powder blue")
        lblDateOverDue.grid(row=7,column=2,sticky=W)
        txtDateOverDue=Entry(DataFrameLeft,font=("times new roman",15,"bold"),textvariable=self.pdob_var,width=29)
        txtDateOverDue.grid(row=7,column=3)
        
        lblActualPrice=Label(DataFrameLeft,font=("times new roman",12,"bold"),text="Patient Address: ",padx=2,pady=6,bg="powder blue")
        lblActualPrice.grid(row=8,column=2,sticky=W)
        txtActualPrice=Entry(DataFrameLeft,font=("times new roman",15,"bold"),textvariable=self.paddress_var,width=29)
        txtActualPrice.grid(row=8,column=3)
        
        #DataFrameRight
        DataFrameRight=LabelFrame(frame,text="Patient Details",bg="powder blue",fg="green",bd=12,relief=RIDGE,font=("times new roman",12,"bold"))
        DataFrameRight.place(x=910,y=5,width=540,height=350)
        
        self.txtBox=Text(DataFrameRight,font=("times new roman",12,"bold"),width=60,height=15,padx=4,pady=6)
        self.txtBox.grid(row=0,column=2)

        #Buttons Frame
        Framebutton=Frame(self.root,bd=12,relief=RIDGE,padx=20,bg="powder blue")
        Framebutton.place(x=0,y=530,width=1530,height=70)
        
        btnAddData=Button(Framebutton,command=self.add_data,text="Add Data",font=("times new roman",13,"bold"),width=23,height=2,bg="blue",fg="white")
        btnAddData.grid(row=0,column=0)
        
        btnAddData=Button(Framebutton,command=self.show_data,text="Show Data",font=("times new roman",13,"bold"),width=23,height=2,bg="blue",fg="white")
        btnAddData.grid(row=0,column=1)
        
        btnAddData=Button(Framebutton,command=self.update,text="Update Data",font=("times new roman",13,"bold"),width=23,height=2,bg="blue",fg="white")
        btnAddData.grid(row=0,column=2)
        
        btnAddData=Button(Framebutton,command=self.delete,text="Delete Data",font=("times new roman",13,"bold"),width=23,height=2,bg="blue",fg="white")
        btnAddData.grid(row=0,column=3)
        
        btnAddData=Button(Framebutton,command=self.reset,text="Reset",font=("times new roman",13,"bold"),width=23,height=2,bg="blue",fg="white")
        btnAddData.grid(row=0,column=4)
        
        btnAddData=Button(Framebutton,command=self.exit,text="Exit",font=("times new roman",13,"bold"),width=23,height=2,bg="blue",fg="white")
        btnAddData.grid(row=0,column=5)
        
        #Information Frame
        FrameDetails=Frame(self.root,bd=12,relief=RIDGE,padx=20,bg="powder blue")
        FrameDetails.place(x=0,y=600,width=1530,height=195)          
        
        Table_frame=Frame(FrameDetails,bd=6,relief=RIDGE,bg="powder blue")
        Table_frame.place(x=0,y=2,width=1460,height=170)
        
        xscroll=ttk.Scrollbar(Table_frame,orient=HORIZONTAL)
        yscroll=ttk.Scrollbar(Table_frame,orient=VERTICAL)
        
        self.hospital_table=ttk.Treeview(Table_frame,column=("tabletname","refno","dose","notablet","lot","issue","expiry","dailydose","sideeffects","info","bp","storage","medics","nhs","pid","pname","pdob","paddress"),xscrollcommand=xscroll.set,yscrollcommand=yscroll.set)
        
        xscroll.pack(side=BOTTOM,fill=X)
        yscroll.pack(side=RIGHT,fill=Y)
        
        xscroll.config(command=self.hospital_table.xview)
        yscroll.config(command=self.hospital_table.yview)
        
        self.hospital_table.heading("tabletname",text="Tablet Name")
        self.hospital_table.heading("refno",text="Reference No")
        self.hospital_table.heading("dose",text="Dose")
        self.hospital_table.heading("notablet",text="No. of Tablets")
        self.hospital_table.heading("lot",text="Lot")
        self.hospital_table.heading("issue",text="Issue Date")
        self.hospital_table.heading("expiry",text="Expiry Date")
        self.hospital_table.heading("dailydose",text="Daily Dose")
        self.hospital_table.heading("sideeffects",text="Side Effects")
        self.hospital_table.heading("info",text="Further Information")
        self.hospital_table.heading("bp",text="Blood Pressure")
        self.hospital_table.heading("storage",text="Storage Advice")
        self.hospital_table.heading("medics",text="Medications")
        self.hospital_table.heading("pid",text="Patient ID")
        self.hospital_table.heading("nhs",text="NHS No.")
        self.hospital_table.heading("pname",text="Patient Name")
        self.hospital_table.heading("pdob",text="Patient D.O.B")
        self.hospital_table.heading("paddress",text="Patient Address")
        
        self.hospital_table["show"]="headings"
        self.hospital_table.pack(fill=BOTH,expand=1)
        
        self.hospital_table.column("tabletname",width=100)
        self.hospital_table.column("refno",width=100)
        self.hospital_table.column("dose",width=100)
        self.hospital_table.column("notablet",width=100)
        self.hospital_table.column("lot",width=100)
        self.hospital_table.column("issue",width=100)
        self.hospital_table.column("expiry",width=100)
        self.hospital_table.column("dailydose",width=100)
        self.hospital_table.column("sideeffects",width=100)
        self.hospital_table.column("info",width=100)
        self.hospital_table.column("bp",width=100)
        self.hospital_table.column("storage",width=100)
        self.hospital_table.column("medics",width=100)
        self.hospital_table.column("pid",width=100)
        self.hospital_table.column("nhs",width=100)
        self.hospital_table.column("pname",width=100)
        self.hospital_table.column("pdob",width=100)
        self.hospital_table.column("paddress",width=100)
        
        self.fetch_data()
        self.hospital_table.bind("<ButtonRelease-1>",self.get_cursor)
        
    def add_data(self):
        conn=mysql.connector.connect(host="localhost",username="root",password="root",database="mydata")
        my_cursor=conn.cursor()
        my_cursor.execute("insert into hospital values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(self.tabletname_var.get(),self.refno_var.get(),self.dose_var.get(),self.notablet_var.get(),self.lot_var.get(),self.issue_var.get(),self.expiry_var.get(),self.dailydose_var.get(),self.sideeffects_var.get(),self.info_var.get(),self.bp_var.get(),self.storage_var.get(),self.medics_var.get(),self.pid_var.get(),self.nhs_var.get(),self.pname_var.get(),self.pdob_var.get(),self.paddress_var.get()))
        conn.commit()
        self.fetch_data()
        conn.close()
            
        messagebox.showinfo("Success","Patient has been inserted successfully")
        
    def fetch_data(self):
        conn=mysql.connector.connect(host="localhost",username="root",password="root",database="mydata")
        my_cursor=conn.cursor()
        my_cursor.execute("select * from hospital")
        rows=my_cursor.fetchall()
        
        if len(rows)!=0:
            self.hospital_table.delete(*self.hospital_table.get_children())
            for i in rows:
                self.hospital_table.insert("",END,values=i)
            conn.commit()
        conn.close()
        
    def get_cursor(self,event=""):
        cursor_row=self.hospital_table.focus()
        content=self.hospital_table.item(cursor_row)
        row=content['values']
        
        self.tabletname_var.set(row[0]),self.refno_var.set(row[1]),self.dose_var.set(row[2]),self.notablet_var.set(row[3]),self.lot_var.set(row[4]),self.issue_var.set(row[5]),self.expiry_var.set(row[6]),self.dailydose_var.set(row[7]),self.sideeffects_var.set(row[8]),self.info_var.set(row[9]),self.bp_var.set(row[10]),self.storage_var.set(row[11]),self.medics_var.set(row[12]),self.pid_var.set(row[13]),self.nhs_var.set(row[14]),self.pname_var.set(row[15]),self.pdob_var.set(row[16]),self.paddress_var.set(row[17])
        
    def show_data(self):
        self.txtBox.insert(END,"Tablet Name:\t\t"+self.tabletname_var.get()+"\n"),
        self.txtBox.insert(END,"Reference No:\t\t"+self.refno_var.get()+"\n"),
        self.txtBox.insert(END,"Dose:\t\t"+self.dose_var.get()+"\n"),
        self.txtBox.insert(END,"No. of Tablets:\t\t"+self.notablet_var.get()+"\n"),
        self.txtBox.insert(END,"Lot:\t\t"+self.lot_var.get()+"\n"),
        self.txtBox.insert(END,"Issue Date:\t\t"+self.issue_var.get()+"\n"),
        self.txtBox.insert(END,"Expiry Date:\t\t"+self.expiry_var.get()+"\n"),
        self.txtBox.insert(END,"Daily Dose:\t\t"+self.dailydose_var.get()+"\n"),
        self.txtBox.insert(END,"Side Effects:\t\t"+self.sideeffects_var.get()+"\n"),
        self.txtBox.insert(END,"Further Information:\t\t"+self.info_var.get()+"\n"),
        self.txtBox.insert(END,"Blood Pressure:\t\t"+self.bp_var.get()+"\n"),
        self.txtBox.insert(END,"Storage Device:\t\t"+self.storage_var.get()+"\n"),
        self.txtBox.insert(END,"Medications:\t\t"+self.medics_var.get()+"\n"),
        self.txtBox.insert(END,"Patient ID:\t\t"+self.pid_var.get()+"\n"),
        self.txtBox.insert(END,"NHS No.:\t\t"+self.nhs_var.get()+"\n"),
        self.txtBox.insert(END,"Patient Name:\t\t"+self.pname_var.get()+"\n"),
        self.txtBox.insert(END,"Patient D.O.B:\t\t"+self.pdob_var.get()+"\n"),
        self.txtBox.insert(END,"Patient Address:\t\t"+self.paddress_var.get()+"\n")           
    
    def update(self):
        conn=mysql.connector.connect(host="localhost",username="root",password="root",database="mydata")
        my_cursor=conn.cursor()
        my_cursor.execute("update hospital set TabletName=%s,Dose=%s,NoTablet=%s,Lot=%s,Issue=%s,Expiry=%s,DailyDose=%s,SideEffects=%s,Info=%s,BP=%s,Storage=%s,Medics=%s,PID=%s,NHS=%s,PName=%s,PDOB=%s,PAddress=%s where RefNo=%s",(self.tabletname_var.get(),self.dose_var.get(),self.notablet_var.get(),self.lot_var.get(),self.issue_var.get(),self.expiry_var.get(),self.dailydose_var.get(),self.sideeffects_var.get(),self.info_var.get(),self.bp_var.get(),self.storage_var.get(),self.medics_var.get(),self.pid_var.get(),self.nhs_var.get(),self.pname_var.get(),self.pdob_var.get(),self.paddress_var.get(),self.refno_var.get()))
        conn.commit()
        self.fetch_data()
        self.reset()
        conn.close()
        
        messagebox.showinfo("Success","Patient has been Updated")
    
    def reset(self):
        self.tabletname_var.set(""),self.refno_var.set(""),self.dose_var.set(""),self.notablet_var.set(""),self.lot_var.set(""),self.issue_var.set(""),self.expiry_var.set(""),self.dailydose_var.set(""),self.sideeffects_var.set(""),self.info_var.set(""),self.bp_var.set(""),self.storage_var.set(""),self.medics_var.set(""),self.pid_var.set(""),self.nhs_var.set(""),self.pname_var.set(""),self.pdob_var.set(""),self.paddress_var.set("")
        self.txtBox.delete("1.0",END)
        
    def delete(self):
        if self.refno_var.get()=="" or self.pid_var.get()=="":
            messagebox.showinfo("Error","First Select the Patient")
        else:
            conn=mysql.connector.connect(host="localhost",username="root",password="root",database="mydata")
            my_cursor=conn.cursor()
            query="delete from hospital where RefNo=%s"
            value=(self.refno_var.get(),)
            my_cursor.execute(query,value)
            
            conn.commit()
            self.fetch_data()
            self.reset()
            conn.close()
            
            messagebox.showinfo("Success","Patient has been Deleted")
        
    def exit(self):
        exit=tkinter.messagebox.askyesno("Hospital Management System","Do you want to exit?")
        if exit>0:
            self.root.destroy()
            return
        
if __name__ == "__main__":
    root=Tk()
    obj=HospitalManagementSystem(root)
    root.mainloop()