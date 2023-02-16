

!pip install dnspython

!pip install pymongo[srv]

!pip install qrcode

import pymongo
client = pymongo.MongoClient("mongodb+srv://lakshmi:Lachunov2@cluster0.9kjx5ob.mongodb.net/?retryWrites=true&w=majority")
db = client.d30
records=db.aadhaar

a={"name":"lakshmi","address":"TN"}
records.insert_one(a)

aadhar_data={
   "name": "Gajalakshmi Karthikeyan",
   "profile_pic": "laksh\Downloads\GAJALAKSHMI (1).jpeg",
   "dob": "02/11/1992",
   "address": {
      "no": "123",
      "street": "Main Street",
      "city": "vellore",
      "state": "TN",
      "pincode": "632401"
   },
   "gender": "Female",
   "education": {
      "qualification": "Bachelor's degree",
      "stream": "Computer Science"
   },
   "email": "Lakshmikarthikeyan235@gmail.com"
}
records.insert_one(aadhar_data)

import random
import qrcode
import string

# Generate a unique 12-digit Aadhar number
aadhar_number = ''.join(random.choices( string.digits, k=12))
print(aadhar_number)

# Create a QR code with the details of the Aadhar number
qr_code = qrcode.make(aadhar_number)

# Save the QR code as an image file
qr_code.save('aadhar_qr_code.png', scale=8)
qr_code

# Set the renewal date to one year from today
renewal_date = datetime.datetime.now() + datetime.timedelta(days=365)

# Update the document with the generated values
records.update_one(
    {"_id": aadhar_data["_id"]},
    {"$set": {"aadhaar_number": aadhar_number, "qr_code": qr_code, "renewal_date": renewal_date}})
