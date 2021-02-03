import gspread
from oauth2client.service_account import ServiceAccountCredentials


# use creds to create a client to interact with the Google Drive API
# scope = ['https://spreadsheets.google.com/feeds']
scope = ['https://docs.google.com/spreadsheets/d/1j9GDRlecHupDR8jScDnIoPsrVdQojbmlfjujwsqPfJk/edit#gid=0']
creds = ServiceAccountCredentials.from_json_keyfile_name(
    'client_secret.json', scope)
client = gspread.authorize(creds)

# Find a workbook by name and open the first sheet
# Make sure you use the right name here.
sheet = client.open("New_Study_For_telegram bot").sheet1

# Extract and print all of the values
list_of_hashes = sheet.get_all_records()
print(list_of_hashes)
