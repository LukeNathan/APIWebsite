from tkinter import *
from PIL import ImageTk,Image
import requests
import random

root = Tk()
root.title("Country Info")
root.geometry("500x350")

html_str = """

<!DOCTYPE html>
<html>
<head>
  <script src="https://restcountries.eu/rest/v2/all"></script>
	<title>Country Information Index</title>
    <link rel="stylesheet" type="text/css" href="ApiHome.css">
    <link rel="script" type="text/javascript" href="HomeScript.js">
</head>
<body>

<font face="Quicksand-Regular" size="+2">

<div class="topnav">
  <a class="active" href="HomeApi.html">Home</a>
  <a href="America.html">Americas</a>
  <a href="Europe.html">Europe</a>
  <a href="Asia.html">Asia</a>
  <a href="Africa.html">Africa</a>
  <a href="Oceania.html">Oceania</a>
</div>

<div class="hero-image">
    <div class="hero-text">
      <h1 style="font-size:50px">Country Information Index</h1>
      <p>By Luke Nathan</p>
    </div>
</div>

<h2 align=center>Chosen Country</h2>

<var></var>

</body>
</html>

"""

def writeHTML(data):
	myfile = open("myapi.html","w+")
	myfile.write("<h1>JSON file returned by API call</h1>")
	myfile.write("<p>Copy and paste to <a href='https://jsoneditoronline.org/'>JSON editor</a> for pretty format.</p>")
	myfile.write(data)
	myfile.close()
	
def main(event):	# use API to get place info
	global datajson
	global response
	
	response = requests.get("https://restcountries.eu/rest/v2/all")

	# if API call is correct
	if (response.status_code == 200):
		data = response.content # response comes in as byte data type
		data_as_str = data.decode()	# decode to str
		writeHTML(data_as_str)  # call function to write string data to HTML file

		# load as a JSON to access specific data more easily
		datajson = response.json()

	else:
		data = "Error has occured"
		writeHTML(data)

response = requests.get("https://restcountries.eu/rest/v2/all")		
datajson = response.json()
	
def localwindow():

	global name_list
	global variable

	topframe = Frame(root,bg='#34d994',height='20')
	topframe.pack(fill=X) # make as wide as root
	can1 = Canvas(topframe,height='20',width='20',bg="#34d994",highlightthickness=0)

	imgframe = Frame(root, width=400,height=150)
	imgframe.pack(fill=None, expand=False)
	canvas = Canvas(imgframe,height=150,width=200)
	canvas.grid(row=0,column=0)
	l1 = Label(imgframe,text="Country Information Index", font=("Quicksand-Bold", 30), fg="#414245")
	l2 = Label(imgframe, text="Display countries and territories with their\ncapital, continent, population, and more", font=("Quicksand-Regular", 15), fg="#414245")
	l1.grid(row=0,column=0)
	l2.grid(row=1,column=0)

	"""style = ttk.Style()

	style.configure('TButton', font =
			('calibri', 10, 'bold'),
			foreground = 'black')"""
	name_list = [] #puts all countries in json into list
	for json_dict in datajson:
		full_name = str(json_dict['name'] + ", " + json_dict['capital'] + ", " + json_dict['region'])
		name_list.append(json_dict['name'])
		#name_list.append(full_name)

	capital_list = [] #does the same but for capitals
	for json_dict in datajson:
		capital_list.append(json_dict['capital'])

	continent_list = []
	for json_dict in datajson:
		continent_list.append(json_dict['region'])

	sub_list = []
	for json_dict in datajson:
		sub_list.append(json_dict['subregion'])

	pop_list = []
	for json_dict in datajson:
		pop_list.append(json_dict['population'])

	area_list = []
	for json_dict in datajson:
		area_list.append(json_dict['area'])

	web_list = []
	for json_dict in datajson:
		web_list.append(json_dict['topLevelDomain'])
	
	variable = StringVar(root) #makes dropdown with list of countries
	variable.set("Pick a country")
	w = OptionMenu(root, variable, *name_list)
	w.pack()

	def butfunct(): #prints country selected in dropdown on button press
		print(variable.get())
		index = name_list.index(variable.get())
		#print(index)
		print(capital_list[index])
		print(continent_list[index])
		print(sub_list[index])
		print(pop_list[index])
		print(area_list[index])
		print(web_list[index])
		countryNumber = random.randint(0, 249)

		f = open("HomeApi.html", "w")
		f.write(html_str)
		f.write("<p>" + variable.get())
		f.write("<br /> <p> Capital: " + capital_list[index])
		f.write("<br /> <p> Continent: " + continent_list[index])
		f.write("<br /> <p> Subregion: " + sub_list[index])
		f.write("<br /> <p> Population: " + str(pop_list[index]))
		f.write("<br /> <p> Area: " + str(area_list[index]) + " km^2")
		f.write("<br /> <p> Website domain: " + str(web_list[index]))
		f.write("<br />")
		f.write("<h2> <p> Random Country </h2>")
		f.write("<p>" + datajson[countryNumber]['name'])
		f.write("<p> Continent: " + datajson[countryNumber]['capital'])
		f.write("<p> Continent: " + datajson[countryNumber]['region'])
		f.write("<p> Subregion: " + datajson[countryNumber]['subregion'])
		f.write("<p> Population: " + str(datajson[countryNumber]['population']))
		f.write("<p> Area: " + str(datajson[countryNumber]['area']) + " km^2")
		f.write("<p> Website domain: " + str(datajson[countryNumber]['topLevelDomain']))
		#f.write("<br />" "Capital: " + datajson[countryNumber]['capital'])


	startButton = Button(root, text="Start", command = lambda: butfunct())
	startButton.bind("<Button-1>", main)
	startButton.pack()
	
	root.mainloop()
	
localwindow()
#main()


