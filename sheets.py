# sheets.py
import gspread
from oauth2client.service_account import ServiceAccountCredentials
from datetime import datetime

# Подключение к Google Sheets
scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
creds = ServiceAccountCredentials.from_json_keyfile_name("credentials.json", scope)
client = gspread.authorize(creds)

# Открытие таблицы
SHEET_NAME = "Заявки с Telegram"
sheet = client.open(SHEET_NAME).sheet1


# Добавление строки в таблицу
def add_lead_to_sheet(name: str, contact: str, task: str):
    now = datetime.now().strftime("%d.%m.%Y %H:%M")
    sheet.append_row([name, contact, task, now])
