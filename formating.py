from openpyxl import Workbook
from openpyxl.styles import Font

#new workbook
wb=Workbook()

#adding multiple sheets
ws1=wb.active
ws1.title="sheet1" #rename the worksheet
ws1['A1']="Bold text"
ws1['B1']="italic text"
ws1['C1']="underline text"
ws1['D1']="colour test"

bold_font=Font(bold=True)
italic_text=Font(italic=True)
underline=Font(underline='single')
color=Font(color='FF0000')

ws1['A1'].font=bold_font
ws1['B1'].font=italic_text
ws1['C1'].font=underline
ws1['D1'].font=color

wb.save("formatting.xlsx")