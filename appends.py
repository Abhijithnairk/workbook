from openpyxl import Workbook

wb=Workbook()

ws=wb.active

data = [
    ["name","age","city"],
    ["sanjay",22,"pattambi"],
    ["rohith",24,"waynad"],
    ["sooraj",25,"balussery"]
]

for row_data in data:
    ws.append(row_data)
    
wb.save('text.xlsx')