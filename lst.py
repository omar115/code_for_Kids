import cv2
import io
from PIL import Image, ImageEnhance
import pytesseract
from wand.image import Image as wi
import re
import pandas as pd
from PyPDF2 import PdfFileWriter, PdfFileReader
from pdf2image import convert_from_path


claim = '15232353'
file = "a.pdf"
pages_to_keep = [0]
infile = PdfFileReader(file, 'rb')
output = PdfFileWriter()

for i in pages_to_keep:
    p = infile.getPage(i)
    output.addPage(p)


with open('A1.pdf', 'wb') as f:
    output.write(f)


pages = convert_from_path('A1.pdf', 500)

for page in pages:
    page.save('A1.jpg', 'JPEG')

#img = Image.open('B1.jpg').convert('LA')
#img.save('B1.png')



# Grayscale, Gaussian blur, Otsu's threshold
image = cv2.imread('A1.jpg')
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
blur = cv2.GaussianBlur(gray, (3,3), 0)
thresh = cv2.threshold(blur, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)[1]

# Morph open to remove noise and invert image
kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (3,3))
opening = cv2.morphologyEx(thresh, cv2.MORPH_OPEN, kernel, iterations=1)
invert = 255 - opening


#read the image
#im = Image.open("B1.jpg")

#enhancer = ImageEnhance.Contrast(im)
#img = enhancer.enhance(2.70)

#read the image
#im = Image.open("B1.png")

#image brightness enhancer
#enhancer = ImageEnhance.Contrast(im)

#factor = 2 #increase contrast
#im_output = enhancer.enhance(factor)
#im_output.save('BF.png')


text = pytesseract.image_to_string(invert, lang='eng', config='--psm 6')
#text = pytesseract.image_to_string(Image.open('BF.png'))
print(text)

x1 = text.find("Bill No")
print(x1)
y1 = text.find("Regn No")
print(y1)
z1 = text[x1:y1]
print(z1)
z1 = z1.split()
print(z1)
billnum = z1[2]
billnum = billnum.split('-')
if billnum[0] == '1' or billnum[0] == 'l':
    print("change hobe")
    
    billnum[0] = 'I'
    billno = '-'
    billno = billno.join(billnum)
    print(billno)
else:
    print("ager")
    billno = '-'
    billno = billno.join(billnum)
    print(billno)


x1 = text.find("Bed No")
print(x1)
y1 = text.find("Discharge")
print(y1)
z1 = text[x1:y1]
print(z1)
z1 = z1.split()
print(z1)
roomno=z1[2]
roomno = roomno.split('/')
print(roomno)
roomno = roomno[0]
print(roomno)

x1 = text.find("Discharge Date")
print(x1)
y1 = text.find("Service Group")
print(y1)
z1 = text[x1:y1]
print(z1)
z1 = z1.split()
print(z1)
ddate = z1[2]
print(ddate)
dtime = z1[3]
dtime = dtime.split(':')
dhr = int(dtime[0])
dmin = int(dtime[1])
print(dhr)
print(dmin)

x1 = text.find("Consultant:")
print(x1)
y1 = text.find("Adm. Date:")
print(y1)
z1 = text[x1:y1]
print(z1)
z1 = z1.split()
print(z1)
length = len(z1)
x = []
fname = z1[1]
sname = z1[2]
if fname == 'OR.':
    fname = 'DR.'
x.append(fname)
x.append(sname)
print(x)


doc = ' '
doc = doc.join(x)
print(doc)

x2 = text.find("Net Bill Amount :")
print(x2)
y2 = text.find("Net Corporate Payable :")
print(y2)
z2 = text[x2:y2]
print(z2)
z2 = z2.split()
print(z2)
netbill = z2[4]
print(netbill)

x2 = text.find("Discharge Type:")
print(x2)
y2 = text.find("Service Group")
print(y2)
z2 = text[x2:y2]
print(z2)
z2 = z2.split()
print(z2)
if z2[3] == 'but' or z2[3] == 'Admitted':
    dtype = 'Normal Discharge'
    
elif z2[3] == 'against' or z2[3] == 'on':
    dtype = 'LAMA'

elif z2[3] == 'Dead':
    dtype = 'NA'

elif z2[3] == 'Birth' or z2[3] == 'Death' or z2[3] == 'Infant':
    dtype = 'Death Discharge'

else:
    
    dtype = z2[2]
print(dtype)


x2 = text.find("Bill Date:")
print(x2)
y2 = text.find("Consultant:")
print(y2)
z2 = text[x2:y2]
print(z2)
z2 = z2.split()
print(z2)
billdate = z2[2]
print(billdate)
billdate=billdate.split('-')
print(billdate)
billdin = int(billdate[0])
billmn = int(billdate[1])
billyr = int(billdate[2])
print(billdin)
print(billmn)
print(billyr)


dtype = 'Stable'
fun = pd.DataFrame(
        [[claim, ddate, dhr, dmin, dtype, roomno, doc, billno, billdin, billmn, billyr, netbill]],
        columns=['Claim_Id', 'Discharge_Date', 'Discharge_Hour', 'Discharge_Minute',
                 'Discharge_Type', 'Room_No', 'Consultant_Name', 'Bill_No', 'Bill_Day', 'Bill_Month', 'Bill_Year',
                 'Net_Bill_Amount'])

fun.to_csv('reader.csv', index=False, header=False, mode='a')
