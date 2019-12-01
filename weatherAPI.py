import requests
import json
from bs4 import BeautifulSoup as bs


class weatherInfo():
	def __init__(self, url = "http://api.openweathermap.org/data/2.5/weather", apiKey = "c296091db07a990cde0c9ec6e4e7bfe9"):
		self.url = url
		self.zipCode = "07060"
		self.apiKey = apiKey
		self.query = self.url + "?zip=" + self.zipCode + "&appid=" + self.apiKey

	def getWeather(self, zip = None):
		if( zip != None):
			self.zipCode = zip
			self.query = self.url + "?zip=" + self.zipCode + "&appid=" + self.apiKey
		with requests.Session() as s:
			#send query as request and put response into json
			r = s.get(self.query)
			data = r.json()
			print(data)
			#extract data that we need from the json response
			tempK = data['main']['temp']
			humid = data['main']['humidity']
			pres = data['main']['pressure']
			tempF = self.kToF(tempK)
			description = data['weather']
			detailDescription = data['weather'][0]

			print("description: "+detailDescription['description'])
			print(detailDescription['description'])

			info = (tempF, humid, pres, detailDescription['description'])

			print("temperature: "+str(tempF))
			print("humidity: "+str(humid))
			print("pressure: "+str(pres))
			return info

	def getWeather2(self, zip = None):
		if( zip != None):
			self.zipCode = zip
			self.query = self.url + "?zip=" + self.zipCode + "&appid=" + self.apiKey
		with requests.Session() as s:
			#send query as request and put response into json
			r = s.get(self.query)
			data = r.json()
			print(data)
			#extract data that we need from the json response
			weather = data['weather']['description']
			details = extractDetails(weather)
			print(details)
			return details

	def setInfo(self, zip, url = None, apiKey = None):
		self.zipCode = zip
		if (url != None):
			self.url = url
		if (apiKey != None):
			self.apiKey = apiKey

	def kToF(self, temp):
		return int(temp*(9/5)-459.67)

weather = weatherInfo()
weather.getWeather()
