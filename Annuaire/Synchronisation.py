import pandas as pd
import gspread
from oauth2client.service_account import ServiceAccountCredentials
import mysql.connector

# 1) Configuration de google sheet

champ_application = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
References = ServiceAccountCredentials.from_json_keyfile_name("Credentials.json", champ_application)
client = gspread.authorize(References)

# Ouverture du classeur
spreadsheet = client.open_by_url("https://docs.google.com/spreadsheets/d/10-BCkQZltFQWibW4gFz9Wfj8dED4-hEVjwcBNRf7FKM/edit?usp=sharing")
worksheet = spreadsheet.worksheet('Réponses au formulaire 3')

# Lire les données
records = worksheet.get_all_records()
df = pd.DataFrame(records)

df