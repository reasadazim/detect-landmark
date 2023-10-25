# Detect landmark using google street view and google cloud vision API

This program takes coordinates (longitude, latitude) as input and output detected landmark name.

## How does it work?
 - [x] Takes coordinates as input
 - [x] Download images from street view in different angle (e.g. 0°, 30°....360°) 
 - [x] Iterates through each image and search for landmarks using Google Cloud Vision API
 - [x] If any landmark is detected, it output the name of the landmark.

## Packages required
 - `pip install google-streetview`
 - `pip install google-cloud-vision`
 - `pip install requests`
 
## Get a Street View Static API key
 - Create a project in [Google Cloud Platform](https://console.cloud.google.com/)
 - Enable billing
 - Create an API key for your project (API & Services > Credentials > Create Credentials > API Key)
 - Enable Street View Static API 
## Install Google Cloud CLI installer
 - Download and install https://cloud.google.com/sdk/docs/install-sdk
 - run command in terminal `gcloud  auth  application-default  login`
 - Login using your google account

**You are done, now run `main.py` file.**

## Tested in
 - Python 3.11.2

## Screenshots
![landmark detected](https://reasadazim.com/wp-content/uploads/2023/10/Screenshot-2023-10-25-223718.png)
