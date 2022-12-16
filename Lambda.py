	
import os
import io
import boto3
import json
import numpy as np
import csv
import urllib.request
from PIL import Image
 
# grab environment variables
ENDPOINT_NAME = os.environ['ASSIGN_ENDPOINT']
runtime= boto3.client('runtime.sagemaker')
 
def lambda_handler(event, context):
    data = json.loads(json.dumps(event))
    img_url = json.dumps(data["url"])
    print(data)
    
    print(img_url)
    img_data = urllib.request.urlopen(urllib.request.Request(url=img_url[1:-1],headers={'Accept': 'application/jpg'},method='GET'),timeout=10).read()
    
    #Converting image data retrieved to Bytes
    imgdata = io.BytesIO(img_data)
    imgOBJ = Image.open(imgdata)
    print(imgOBJ)

    #Resizing the image
    imgOBJ = imgOBJ.resize((28, 28))
    imgOBJ = np.array(imgOBJ)
    
    #RGB to Grayscale conversion
    imgOBJ = np.array(imgOBJ)[:,:,0];   
    imgOBJ = Image.fromarray(imgOBJ);    
      
    #Resizing the image
    imgOBJ = imgOBJ.resize((28, 28))
    imgOBJ = np.array(imgOBJ)
    
    #Expanding the img array
    imgOBJ = np.expand_dims(imgOBJ, axis=0)
    imgOBJ = np.expand_dims(imgOBJ, axis=1)
    imgOBJ = imgOBJ.astype('float32')
    
    #Convert object o JSON string 
    dataAsJson = json.dumps(imgOBJ.tolist())
    
   
    response = runtime.invoke_endpoint(EndpointName=ENDPOINT_NAME,ContentType='application/json',Body=dataAsJson)
    result = json.loads(response['Body'].read().decode())
    
    print("Response")
    print(response)
    
    print("Result")
    print(result)
    
    #Code used to get the nearest prediction
    labeled_predictions = list(zip(range(10), result[0]))
    print("Labeled predictions: ")
    print(labeled_predictions)
    print()
    
    #Finding the inal predicted value
    labeled_predictions.sort(key=lambda label_and_prob: 1.0 - label_and_prob[1])
    print("Most likely answer: {}".format(labeled_predictions[0]))
    
    revert = "Predicted Number = "+ str(labeled_predictions[0][0])
    return revert
