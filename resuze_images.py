from doctest import master
from tkinter import *
import tkinter as tk
from  tkinter import ttk
from turtle import width
from typing import List
from ttkthemes import ThemedStyle
from tkinter import messagebox
import random
from tkinter import filedialog as fd
from PIL import ImageTk, Image
import names  
import os
import queue

class resize_images():
   global num_win
   global master
   
   def __init__(self,master):
      self.master=master
      self.num_win=0
      
      
      self.l=Label(self.master,text="Status", foreground="green" ,font=('',8))
      self.l.place(relx=0.0,rely=1,anchor='sw')
      self.treeview()
      self.progress=ttk.Progressbar(self.master,orient=HORIZONTAL,length=100,mode='determinate')
      self.progress.place(x=390,y=420)  
      self.displayimage=Frame(self.master,width= 140, height= 140,relief=GROOVE,bd=2)
      self.displayimage.place(x=350,y=190)
      Label(self.displayimage,text='width:').place(x=10,y=5)
      self.iw=tk.Entry(self.displayimage,width=7,relief=GROOVE,bd=2)
      self.iw.place(x=60,y=5)
      Label(self.displayimage,text='height:').place(x=10,y=35)
      self.ih=tk.Entry(self.displayimage,width=7,relief=GROOVE,bd=2)
      self.ih.place(x=60,y=35)
      self.iw.insert(0,"640")
      self.ih.insert(0,"480")
     

   def temp_txt(self,e):
          pass
   def temp_txt1(self,e):
          pass
   def up(self,event):
      
      pass
     

   def exit(self,event = None):
         self.master.quit()
   def exit1(self,e):
         self.master.quit()
   def settitle(self,name):  
      self.name=name 
      self.master.title(self.name)
   def setsize(self,width,height):
      self.width=width
      self.height=height
      self.master.geometry("%dx%d" %(self.width,self.height))
      self.master.protocol("WM_DELETE_WINDOW", self.exit)
      self.master.bind("<Escape>",self.exit)
   def setvisible(self,bol):
          self.addbutton("Add")
          self.bol=bol
          style = ThemedStyle(self.master)
          #style.theme_use('blue')
          
      
      
          
          if(bol):
            
            
            self.master.mainloop()
            
   def setresible(self):
          self.master.resizable(False,False)
          
   def addbutton(self,text):
         w=8
         self.b1=Button(self.master,text=text,width=w,height=1,command=self.add_row)
         self.b1.place(x=self.width-100,y=20)
         self.b2=Button(self.master,text="Delete",width=w,height=1,command=self.del_column)
         self.b2.place(x=self.width-100,y=110)
         self.b3=Button(self.master,text="Exit",width=w,height=1,command=self.exit)
         self.b3.place(x=self.width-100,y=140)
         self.b4=Button(self.master,text="Convert",width=w,height=1,command=self.convert)
         self.b4.place(x=self.width-100,y=80)
         self.b5=Button(self.master,text="AddFolder",width=w,height=1,command=self.select_folder)
         self.b5.place(x=self.width-100,y=50)
         self.b1.bind('<Control-p>', self.add_row)
   def treeview(self):
         
         self.treeview = ttk.Treeview(self.master,height=15,column=("c1", "c2"), show='headings')
         self.treeview.grid(row=0, sticky=W,padx=10,pady=20)
         self.treeview.column("# 1", anchor=CENTER,width=0)
         #self.treeview.heading("# 1", text="Sno")
         self.treeview.column("# 2", anchor=W,width=300)
         self.treeview.heading("# 2", text="FilePath")
         vsb = ttk.Scrollbar(self.master, orient="vertical", command=self.treeview.yview)
         vsb.grid(column=1, row=0, sticky='NS',pady=20,padx=0)
         self.treeview.configure(yscrollcommand=vsb.set)
         hsb = ttk.Scrollbar(self.master, orient=tk.HORIZONTAL, command=self.treeview.xview)
         #hsb.grid(column=0, row=1, sticky='EW',pady=20,padx=0)
         self.treeview.configure(xscrollcommand=hsb.set)
         self.treeview.bind("<Button-1>",self.onDoubleClick)
   def onDoubleClick(self,event):
            item=self.treeview.selection()
            for i in item:
               self.show_image(self.treeview.item(i, "values")[1])
               

   def del_column(self):
      selected_items = self.treeview.selection()        
      for selected_item in selected_items:          
         self.treeview.delete(selected_item)
   def select_folder(self):
         
         self.extension=['jpg','png','gif']
         try:
            folder_selected = fd.askdirectory()
            files=os.listdir(folder_selected)
            for i,data in enumerate(files):
                  if(data.endswith(tuple(self.extension))):
                     self.treeview.insert('', 'end', text="1", values=("",folder_selected+"/"+data))
         except :
            pass                     

   def add_row(self,event = None):
      self.extension=['jpg','png','gif']
      filename = fd.askopenfilename(parent=self.master,
      title="Select an Image",
      filetypes=[
               
               
               ]
      )
      if(filename.endswith(tuple(self.extension))):
         self.treeview.insert('', 'end', text="1", values=("", filename))
      
   def convert(self):
      from tkinter import messagebox
      d=[]

      for child in self.treeview.get_children():
         d.append(self.treeview.item(child)["values"][1])
         
      d=list(set(d))
      
      if(len(d)==0):
         messagebox.showinfo("Message", "Select Image Files")
         
      else :
         start=round(100/len(d))

      
      for i,data in enumerate(d):
         self.img_save(data)
         self.progress['value']+=start
         self.master.update_idletasks()
      if(len(d)!=0):
         messagebox.showinfo("Message", "Success")
      self.treeview.delete(*self.treeview.get_children())
      self.progress['value']=0
      start=0
      self.master.update_idletasks()
  
   def show_image(self,imagefile):
         img=ImageTk.PhotoImage(file=imagefile)

         
          

   def img_save(self,key):
         w=640
         h=480
         if(self.iw.get()!='' and self.ih.get()!=''): 
            w=int(self.iw.get())
            h=int(self.ih.get())
         
         format=os.path.splitext(key)[1]
         filename=os.path.basename(key)
         
         format=format.upper()
         if(format=='.JPG'):
            format='JPEG'
         if(format=='.PNG'):
            format='PNG'
         if(format=='.GIF'):
            format='GIF'
         
         try:
            img=Image.open(key)
            img=img.resize((w,h),Image.LANCZOS)
            r=img.save(".//output//"+filename,format)
            self.l['text']=filename
         except Exception as e:
            print("file_not converted"+str(e))


   

         
         
root=Tk()


b=resize_images(root)
b.settitle("imageresize ver 1.0")
b.setsize(500,450)
b.setresible()
b.setvisible(True)
