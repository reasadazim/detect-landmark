import json
import os
from street_view import *
from google.cloud import vision

get_view(33.4486691,-111.969089 )
# get_view(46.1812793,-123.817147)
# get_view(24.9615347,89.3461435)
# get_view(51.8958842,-8.4939246)
# get_view(23.7804011,90.4167485)


directory = 'downloads'
landmarks_list = []

for filename in os.listdir(directory):

    def detect_landmarks(path):
        """Detects landmarks in the file."""
        client = vision.ImageAnnotatorClient()

        with open(path, "rb") as image_file:
            content = image_file.read()

        image = vision.Image(content=content)

        response = client.landmark_detection(image=image)
        landmarks = response.landmark_annotations

        for landmark in landmarks:
            # print(landmark.description)

            landmarks_list.append(landmark.description)

            # for location in landmark.locations:
            #     lat_lng = location.lat_lng
            #     print(f"Latitude {lat_lng.latitude}")
            #     print(f"Longitude {lat_lng.longitude}")

        if response.error.message:
            raise Exception(
                "{}\nFor more info on error messages, check: "
                "https://cloud.google.com/apis/design/errors".format(response.error.message)
            )


    detect_landmarks(f'downloads/{filename}')
    # detect_landmarks(f'downloads/img_20.jpg')

landmarks = set(landmarks_list)
landmarks = list(landmarks)
output = {}
index = 0
for landmark in landmarks:
    output.update({index: landmark})
    index = index + 1

print(json.dumps(output))
