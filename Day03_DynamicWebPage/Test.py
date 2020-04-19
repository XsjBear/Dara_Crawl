#读取word docx文档内容
from zipfile import ZipFile
from urllib.request import urlopen
from io import BytesIO
from bs4 import BeautifulSoup

wordFile = urlopen("https://wk.baidu.com/view/1a1c4c9366ec102de2bd960590c69ec3d5bbdbb6?pcf=2&from=singlemessage&isappinstalled=0").read()
print(wordFile)
wordFile = BytesIO(wordFile)
document = ZipFile(wordFile)#
xml_content = document.read("word/document.xml")
#print(xml_content.decode("utf-8"))

wordObj = BeautifulSoup(xml_content.decode("utf-8"),"lxml")
textStrings = wordObj.findAll("w:t")
for textElem in textStrings:
    print(textElem.text)