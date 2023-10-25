# Import google_streetview for the api module
import google_streetview.api
import requests

def get_view(lat, long):

	headings = [0,20,40,60,80,100,120,140,160,180,200,220,240,260,280,300,320,340]

	for heading in headings:
		# Define parameters for street view api
		params = [{
			'size': '640x640',
			'location': f'{lat},{long}', # coordinates
			'heading': f'{heading}', # camera angles in degree
			'pitch': '4', # camera up down control
			'fov': '30', # zoom level 0 to 90
			'key': 'YOUR_API_KEY' # Google Street View Static API key
		}]

		# Create a results object
		results = google_streetview.api.results(params)

		# print(results.links[0])

		url = results.links[0]
		response = requests.get(url)

		with open(f"downloads/img_{heading}.jpg", "wb") as f:
			f.write(response.content)

