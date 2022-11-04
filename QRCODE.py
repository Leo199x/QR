#!/usr/bin/env python
# coding: utf-8

# In[1]:


# import tkinter as tk# standard Python interface to the Tk GUI toolkit

# from tkinter import filedialog


# In[2]:


# root = tk.Tk()#The root window is created
# # """
# # Tkinter works by starting a tcl/tk interpreter under the covers,
# # and then translating tkinter commands into tcl/tk commands. 
# # The main window and this interpreter are intrinsically linked, 
# # and both are required for a tkinter application to work
# # """
# x = filedialog.askopenfilename()

# root.mainloop()#that execution of your python program halts there


# "pip install qrcode
# #pillow library for image manipulation
# pip install pillow"

# In[ ]:





# # FOR SIMPLE QRCODE 

# In[3]:


# import  qrcode
#quick response code 2D of bar code


# In[4]:


# image = qrcode.make(x)
# image.save("qr.png","PNG")


# # ADVANCED  

# ## version parameter takes an integer from 1 to 40 to control the size of the qrcode 
# ## smaller the number the smaller the a\qrcode size 

# In[5]:


# #ERROR_CORRECT_M, it is default 15% error can be corrected
# #border default 5
# qr=qrcode.QRCode(
#     version=1 ,
#     error_correction=qrcode.constants.ERROR_CORRECT_M,
#     box_size=10,
#     border=4
#     )

# data=x#data provide

# qr.add_data(data)

# #fit automatic false (static)
# qr.make(fit=True)

# img=qr.make_image(fill="black",back_color="white")
# #black and background white

# img.save("sad.png")


# In[9]:


import QRCODE as qr

print("""QR Stands For Quick Response Code 
It can be considered as 2D dimensional representation of barcode
PLEASE NOTE 1kb is the limit size of the QR Code
""")

# # import tkinter as tk

# # root = tk.Tk()

# # v = tk.IntVar()

# # tk.Label(root, 
# #         text="""MAKE QR CODE OF:""",
# #         justify = tk.LEFT,
# #         padx = 20).pack()
# # tk.Radiobutton(root, 
# #               text="Text",
# #               padx = 20, 
# #               variable=v, 
# #               value=1).pack()
# # tk.Radiobutton(root, 
# #               text="Link",
# #               padx = 20, 
# #               variable=v, 
# #               value=2).pack()

# # root.mainloop()

# v.get()

x=int(input("""Make QR CODE OF:
1.Text
2.Link
"""))


data=input("Provide the data here:")

img=qr.make(data)
img.save(r"C:\Users\Abhi\Desktop\EXPO\lol.png")


# In[10]:


from PIL import Image
f = Image.open(r"C:\Users\Abhi\Desktop\EXPO\lol.png").show()


# In[ ]:




