import requests
import base64
import json
import csv

API_ACCESS_ID = "1"
API_SECURE_KEY = ""   #api credentials
LOCATION_ID = ""
ORGANIZATION_ID = ""

#Sandbox URL
API_ENDPOINT = f"https://sandbox.forte.net/api/v3/organizations/org_{ORGANIZATION_ID}/locations/loc_{LOCATION_ID}/customers/"
#Live URL
#API_ENDPOINT= "https://api.forte.net/v3/organizations/org_{}/locations/loc_{}/customers/".format(LOCATION_ID,ORGANIZATION_ID)

#Authorization header formatting
authCred = f"{API_ACCESS_ID}:{API_SECURE_KEY}"
encodedBytes = base64.b64encode(authCred.encode("utf-8"))
encodedStr = str(encodedBytes, "utf-8")
print(encodedStr)
#client data

#Parameters for input
FIRSTNAME = "Ralph"
LASTNAME = "Higgins"
COMPANYNAME = "Krimby Krem"
ADDRESSES_FIRSTNAME = FIRSTNAME
ADDRESSES_LASTNAME = LASTNAME
ADDRESSES_COMPANYNAME = COMPANYNAME
ADDRESSES_PHONE = "2243435454"
ADDRESSES_EMAIL = "krem@krimby.com"
ADDRESSES_STREET1 = "1 house road"
ADDRESSES_STREET2 = ""
ADDRESSES_CITY = "Dallas"
ADDRESSES_STATE = "TX"
ADDRESSES_ZIP = "75214"
CARD_CARD = "4111111111111111"
CARD_EM = "12"
CARD_EY = "2022"
CARD_CVV = "123"
CARD_TYPE = "visa"
CARD_NAME = "Ralph Higgins"


PAYLOAD = "{\r\n       \"first_name\": \""+FIRSTNAME+"\",\r\n       \"last_name\": \""+LASTNAME+"\",\r\n       \"company_name\": \""+COMPANYNAME+"\",\r\n       \"addresses\": [\r\n          {\r\n             \"first_name\": \""+ADDRESSES_FIRSTNAME+"\",\r\n             \"last_name\": \""+ADDRESSES_LASTNAME+"\",\r\n             \"company_name\": \""+ADDRESSES_COMPANYNAME+"\",\r\n             \"phone\": \""+ADDRESSES_PHONE+"\",\r\n             \"email\": \""+ADDRESSES_EMAIL+"\",\r\n             \"address_type\": \"both\",\r\n             \"physical_address\": {\r\n                \"street_line1\": \""+ADDRESSES_STREET1+"\",\r\n                \"street_line2\": \""+ADDRESSES_STREET2+"\",\r\n                \"locality\": \""+ADDRESSES_CITY+"\",\r\n                \"region\": \""+ADDRESSES_STATE+"\",\r\n                \"postal_code\": \""+ADDRESSES_ZIP+"\"\r\n             }\r\n          },\r\n          ],\r\n          \"paymethod\": {\r\n             \"card\": {\r\n                \"account_number\": \""+CARD_CARD+"\",\r\n                \"expire_month\": "+CARD_EM+",\r\n                \"expire_year\": "+CARD_EY+",\r\n                \"card_verification_value\": \""+CARD_CVV+"\",\r\n                \"card_type\": \""+CARD_TYPE+"\",\r\n                \"name_on_card\": \""+CARD_NAME+"\"\r\n             }\r\n          }\r\n}"
HEADERS = {
    'X-Forte-Auth-organization-id': f"org_{ORGANIZATION_ID}",
    'Content-Type': "application/json",
    'Accept': "application/json",
    'Authorization' : f"Basic {encodedStr}",
    'cache-control': "no-cache"
}

results = requests.post(url = API_ENDPOINT, data = PAYLOAD, headers = HEADERS)
print(results)
print(results.text)
