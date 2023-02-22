

# Aadhar card name
name = input("Enter name : ")

# upload profile pic
image = input("Upload image path : ")
from bson.binary import Binary

with open("profile.png", "rb") as p:
    image_data = p.read()
binary_image = Binary(image_data)

dob = input("Enter DOB DD-MM-YYYY : ")
# address
no_street = input("Enter building no and street : ")
city = input("Enter city : ")
state = input("Enter state : ")
pincode = input("Enter pincode : ")
gender = input("Enter gender : ")
education_qualification = input("Enter educational qualification (NA, 10, 12th, bachelors, master, doctrate) : ")
education_stream = input("Enter education stream : ")
email_id = input("Enter email id : ")

# unique aadhar no generate
import secrets
aadharno = secrets.randbelow(1000000000000)

# generate qr code for aadhar card
import qrcode

img = qrcode.make(aadharno)
with open("qrcode.png", "wb") as f:
    img.save(f)

with open("qrcode.png", "rb") as f:
    img_data = f.read()

# generate renewal date
import datetime

now = datetime.datetime.now()
renewal_date = now + datetime.timedelta(days=365)
formatted_renewal_date = renewal_date.strftime("%d-%m-%Y")

# connect mongodb server
import pymongo

client = pymongo.MongoClient("mongodb+server/here")
db = client.data
records =db.aadhar

new_aadhar = {
    "name" : name,
    "profile_pic" : binary_image,    
    "dob" : dob,
    "address" : {
        "no,street" : no_street,
        "city" : city,
        "state" : state,
        "pincode" : pincode
    },
    "gender" : gender,
    "education qualification" : {
        "education" : education_qualification,
        "stream" : education_stream
    },
    "email_id" : email_id,
    "aadhar_no" : aadharno,
    "qr code" : img_data,
    "renewal date" : formatted_renewal_date
}

x = records.insert_one(new_aadhar)
if x != None:
  print("Aadhar created successfully!")
else :
  print("Aadhar created unsuccessfully!")

# edit aadhar card details
aadhar_name = {"name" : input("Enter aadhar name : ")}

edit_aadhar = {
    "$set" :
    {
         "name" : input("Enter name : "),
    "profile_pic" : input("Upload image path : "),
    "address" : {
        "no,street" : input("Enter building no and street : "),
        "city" : input("Enter city : "),
        "state" : input("Enter state : "),
        "pincode" : input("Enter pincode : ")
    },
    "gender" : input("Enter gender : "),
    "education qualification" : {
        "education" : input("Enter education qualification : "),
        "stream" : input("Enter education stream : ")
    },
    "email_id" : input("Enter email id : ")
    }
}

y = records.update_one(aadhar_name, edit_aadhar)
if y != None:
  print("Your Aahar card update successfully!")
else :
  print("Your Aadhar card update unsuccessfully!")


# create PDF file for aadhar card details
from fpdf import FPDF

pdf = FPDF()
pdf.add_page()

pdf.set_font("Arial", size=12)

data = records.find({"name" : name})

for record in data:
    pdf.cell(0, 10, txt=str(record), ln=1)

pdf.output("Aadhar.pdf")
