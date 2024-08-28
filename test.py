import gspread
from gspread.models import Worksheet
from oauth2client.service_account import ServiceAccountCredentials

# google sheet에 대한 사용자 인증
scope = ['https://spreadsheets.google.com/feeds']
json_file_nm = 'manageasset_test.json'
credentials = ServiceAccountCredentials.from_json_keyfile_name(json_file_nm, scope)
gc = gspread.authorize(credentials)
# URL로 sheet 불러오기
sheet_url = 'https://docs.google.com/spreadsheets/d/1jAyFCNyagIqWyan1rmFPRduOSg-RT4uhfKyNvJ_2ebs/edit#gid=2098151432'
doc = gc.open_by_url(sheet_url)

History_Cash = doc.worksheet("History_Cash").get_all_values()
# History_Stock = doc.worksheet("History_Stock").get_all_values()
# Asset_Code_Table = doc.worksheet("Asset_Code_Table").get_all_values()
# Asset_Timelapse = doc.worksheet("Asset_Timelapse").get_all_values()
# Hold_Stock = doc.worksheet("Hold_Stock").get_all_values()
# Stock_Price = doc.worksheet("Stock_Price").get_all_values()

print(History_Cash) 



