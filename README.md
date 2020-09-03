# phonebook

Technology:
Django 3
DjangoRestFramework = 3.10


Step1:
clone the project on local system
Step2:
create a virtualenv and run the requirements.txt file
step3.
create super user
step4:
url is following:
to get all the contacts: 
GET localhost:8000/contact/
To create a contact
POST localhost:8000/contact
  {
  "name":"abc",
  "phone":8765434321,
  "user":"u1"
  }
  
 to get particular record
 GET localhost:8000/contactdetails/?name=abc
 
 Note: Authentication and Authorization classes has not implemented.
