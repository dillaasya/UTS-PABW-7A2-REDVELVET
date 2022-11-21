from fastapi import FastAPI
from fastapi.responses import FileResponse
from json2html import*
import json
import pandas as pd
app = FastAPI()

@app.get("/")
async def root():
    return 'Hello World, by PABW 7A2 REDVELVET'

@app.get("/cars_json")
async def root():
    file = open('Cars.json')
    f = json.load(file)
    scanOutput = json2html.convert(json = f)
    htmlreportfile = "D:/UMSIDA/SEMESTER 7/PENGEMBANGAN APLIKASI BERBASIS WEB/redvelvet/"
    new_file = open("json2html_output.html","w")
    new_file.write(scanOutput)
    new_file.close()
    return FileResponse("json2html_output.html")

@app.get("/cars_csv")
async def root():
    file = pd.read_csv("Cars.csv")
    convert = file.to_html("csv2html_output.html")
  
    return FileResponse("csv2html_output.html")


@app.get("/cars_xml")
async def root():
    import lxml.html
    from lxml import etree
    
    xslt_doc = etree.parse("template.xslt")
    xslt_transformer = etree.XSLT(xslt_doc)
    
    source_doc = etree.parse("Cars.xml")
    output_doc = xslt_transformer(source_doc)

    #print(str(output_doc))
    output_doc.write("xml2html_output.html", pretty_print=True)
    print("success")
    return FileResponse("xml2html_output.html")