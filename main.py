import pandas as pd
import gspread
from oauth2client.service_account import ServiceAccountCredentials
import datetime
from calendar import monthrange
import numpy as np
import matplotlib.pyplot as plt
import math as math

scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
credentials = ServiceAccountCredentials.from_json_keyfile_name('key/karczma-d1f59c06a458.json', scope)
gc = gspread.authorize(credentials)

wks = gc.open("Karczma Baniaka - Raporty z sesji").sheet1
data = wks.get_all_values()
headers = data.pop(0)
df = pd.DataFrame(data, columns=headers)

month = datetime.datetime.now().month-1
if month == 0:
    month = 12

year = datetime.datetime.now().year
if month == 12:
    year = year - 1
days = monthrange(year, month)

datastart = "{}-{}-01".format(year, month)
dataend = "{}-{}-{}".format(year, month, days[1])
last_month = df[(df['Data sesji'] >= datastart) & (df['Data sesji'] <= dataend)]

print(last_month)
