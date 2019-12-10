import os, io
from google.cloud import vision
from google.cloud.vision import types

os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = r'test-for-receipt-OCR-e3f80220c980.json'

client = vision.ImageAnnotatorClient()

print(dir(client))