from azure.cognitiveservices.vision.computervision import ComputerVisionClient
from azure.cognitiveservices.vision.computervision.models import VisualFeatureTypes
from msrest.authentication import CognitiveServicesCredentials
import time 
import requests
import json
import numpy as np
import os

# Get endpoint and key from environment variables
# export RES_REGION='East US 2'
# export RES_GROUP='AI-ML-vision'
# export ACCT_NAME='CV-ComputerVision-kentest'
# export ACCOUNT_KEY='f857bc507ce54d5ab4379eddbf80f837'	
# export ACCOUNT_ENDPOINT='https://cv-computervision-kentest.cognitiveservices.azure.com/' 
print ("using EXPORTED vars: export ACCOUNT_KEY= $ACCOUNT_KEY && export ACCOUNT_ENDPOINT = $ACCOUNT_ENDPOINT ")
print ("make sure you export these to your o/s environment ")
endpoint = os.environ['ACCOUNT_ENDPOINT']
key = os.environ['ACCOUNT_KEY']

# Set credentials
credentials = CognitiveServicesCredentials(key)

# Create client
client = ComputerVisionClient(endpoint, credentials)

# https://docs.microsoft.com/en-us/azure/cognitive-services/computer-vision/quickstarts-sdk/python-sdk#analyze-an-image

# Python Image Testing Example 
# Variables

_maxNumRetries = 1
print ("key="+ key)
	

# URL direction to image
#urlImage = "https://raw.githubusercontent.com/oakhillroboticmakerlabs/CVfirstSample/master/samples/commonObstacles/bigObstacle4.jpg"
# urlImage = 'https://oxfordportal.blob.core.windows.net/vision/Analysis/3.jpg'
#urlImage = "https://raw.githubusercontent.com/oakhillroboticmakerlabs/CVfirstSample/master/samples/Label4-Yellow-True.PNG"
# urlImage = "https://raw.githubusercontent.com/oakhillroboticmakerlabs/CVfirstSample/master/samples/commonObstacles/farm.jpg"
# urlImage = "https://raw.githubusercontent.com/oakhillroboticmakerlabs/CVfirstSample/master/samples/commonObstacles/river2.jpg"
#rlImage = "https://raw.githubusercontent.com/oakhillroboticmakerlabs/CVfirstSample/master/samples/commonObstacles/boatFront2.jpg"
#urlImage = "https://raw.githubusercontent.com/oakhillroboticmakerlabs/CVfirstSample/master/samples/commonObstacles/dam_obstacle.jpg"
urlImage = "https://raw.githubusercontent.com/oakhillroboticmakerlabs/CVfirstSample/master/samples/commonObstacles/little-river.jpg"

print('analyzing urlImage= '+urlImage)
# Computer Vision parameters
params = { 'visualFeatures' : 'Color,Categories,Description,Tags,ImageType'} 

headers = dict()
headers['Ocp-Apim-Subscription-Key'] = key
headers['Content-Type'] = 'application/json' 

json = { 'url': urlImage } 
data = None

url = "https://upload.wikimedia.org/wikipedia/commons/thumb/1/12/Broadway_and_Times_Square_by_night.jpg/450px-Broadway_and_Times_Square_by_night.jpg"

image_analysis = client.analyze_image(urlImage,visual_features=[VisualFeatureTypes.tags])
print(image_analysis)

print("----- TAGS  -----")
for tag in image_analysis.tags:
    print(tag)

print("----- MODELS -----")
models = client.list_models()

for x in models.models_property:
    print(x)
