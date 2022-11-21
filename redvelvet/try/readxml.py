import lxml.html
from lxml import etree
 
xslt_doc = etree.parse("template.xslt")
xslt_transformer = etree.XSLT(xslt_doc)
 
source_doc = etree.parse("Cars.xml")
output_doc = xslt_transformer(source_doc)

#print(str(output_doc))
output_doc.write("tes.html", pretty_print=True)
print("success")