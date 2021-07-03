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

History_Cash = doc.worksheet("History_Cash")
History_Stock = doc.worksheet("History_Stock").get_all_values()

# def subcash()
update_rows = []
update_idx = len(History_Cash.get_all_values())

for idx in range(len(History_Stock)-1):
    row = History_Stock[idx+1] 
    new_date = row[0]
    from_asset = row[2]
    deal_type = "Buy_Stock"
    value = "-"+row[4]
    related_asset = row[1]
    update_rows.append([new_date, from_asset, deal_type, value, related_asset])
History_Cash.insert_rows(update_rows, update_idx+1)
    
