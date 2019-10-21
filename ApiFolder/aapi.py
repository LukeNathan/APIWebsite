from tkinter import *
from PIL import ImageTk,Image
import requests
import random

def writeHTML(data):
	myfile = open("myapi.html","w+")
	myfile.write("<h1>JSON file returned by API call</h1>")
	myfile.write("<p>Copy and paste to <a href='https://jsoneditoronline.org/'>JSON editor</a> for pretty format.</p>")
	myfile.write(data)
	myfile.close()

def main(event):	# use API to get place info
	response = requests.get("https://restcountries.eu/rest/v2/all")

	# if API call is correct
	if (response.status_code == 200):
		data = response.content # response comes in as byte data type
		data_as_str = data.decode()	# decode to str
		writeHTML(data_as_str)  # call function to write string data to HTML file

		# load as a JSON to access specific data more easily
		datajson = response.json()
		countryNumber = random.randint(0, 249)
		print(datajson[countryNumber]['name'])
		print(datajson[countryNumber]['capital'])
		print(datajson[countryNumber]['topLevelDomain'])
		print(datajson[countryNumber]['region'])
		print(datajson[countryNumber]['subregion'])
		print(datajson[countryNumber]['population'])
		print(datajson[countryNumber]['area'])
		print(datajson[countryNumber]['languages'])
		print(datajson[countryNumber]['currencies'])

		f = open("HomeApi.html", "a")
		f.write(datajson[countryNumber]['name'])
		f.close()

	
	else:
		data = "Error has occured"
		writeHTML(data)

def test(event):
        print(event) #ensure that this line is indented
        
def localwindow():

	root = Tk()
	root.title("Country Info")
	root.geometry("500x350")

	topframe = Frame(root,bg='#34d994',height='20')
	topframe.pack(fill=X) # make as wide as root
	can1 = Canvas(topframe,height='20',width='20',bg="#34d994",highlightthickness=0)
	'''
	can1.create_line(0, 5, 20, 5,fill='white')
	can1.create_line(0, 10, 20, 10,fill='white')
	can1.create_line(0, 15, 20, 15,fill='white')
	can1.bind("<Button-1>",main) # keyword 
	can1.pack(side=LEFT, padx=5, pady=5)
	'''


	imgframe = Frame(root, width=400,height=150)
	imgframe.pack(fill=None, expand=False)
	canvas = Canvas(imgframe,height=150,width=200)
	canvas.grid(row=0,column=0)
	l1 = Label(imgframe,text="Country Information Index", font=("Quicksand-Bold", 30), fg="#414245")
	l2 = Label(imgframe, text="Display countries and territories with their\ncapital, continent, language, and more", font=("Quicksand-Regular", 15), fg="#414245")
	l1.grid(row=0,column=0)
	l2.grid(row=1,column=0)
	#myimage = Image.open("/Users/luke.nathan/Desktop/Code/Grade 10/ApiFolder/World.jpg")
	#myimage = myimage.resize((200, 150), Image.ANTIALIAS)
	#myimg = ImageTk.PhotoImage(myimage)
	#canvas.create_image(0, 0, image=myimg, anchor = NW)

	"""style = ttk.Style()

	style.configure('TButton', font =
                        ('calibri', 10, 'bold'),
                        foreground = 'black')"""

	startButton = Button(root, text="Start")
	startButton.bind("<Button-1>", main)
	startButton.pack()
	#startButton.grid(row=1, column=1)

	
	root.mainloop()

localwindow()
#main()


