import tkinter as tk
import PyPDF2
from PIL import Image,ImageTk
from tkinter.filedialog import askopenfile

root=tk.Tk()

canvas= tk.Canvas(root,width=600,height=300)
canvas.grid(columnspan=3,rowspan=3)

logo=Image.open('logo.png')
logo= ImageTk.PhotoImage(logo)
logo_label = tk.Label(image=logo)
logo_label.image=logo
logo_label.grid(column=1,row=0)

#instructions

instructions =tk.Label(root,text="Select a PDf file on your computer to extract all its text",font="BatmanForeverAlternate")
instructions.grid(columnspan=3,column=0,row=1)   

def open_file():
	browse_text.set("loading...")
	file = askopenfile(parent=root,mode='rb',title="Choose a file",filetype=[("Pdf file","*.pdf")])
	if file:
		read_pdf = PyPDF2.PdfFileReader(file)
		page = read_pdf.getPage(0)
		page_content = page.extractText()

		#text_box	
		text_box=tk.Text(root,height=10,width=50,padx=10,pady=10)
		text_box.insert(1.0,page_content)
		text_box.tag_configure("center",justify="center")
		text_box.tag_add("center",1.0,"end")
		text_box.grid(column=1,row=3)

		browse_text.set("browse")

#browse button
browse_text = tk.StringVar()
browse_btn=tk.Button(root,textvariable=browse_text,command=lambda:open_file(),font="BatmanForeverAlternate",bg="#20bebe",fg="grey",height=1,width=11)
browse_text.set("Browse")
browse_btn.grid(column=1,row=2)

canvas= tk.Canvas(root,width=600,height=150)
canvas.grid(columnspan=3)

root.mainloop()