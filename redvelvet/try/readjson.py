from fastapi import FastAPI
from fastapi.responses import JSONResponse
from json2html import *
import json

file = open('../Cars.json')
response = json.load(file)
print(json2html.convert(json = response))