from comtypes.client import CreateObject
import os

project_dir = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
xl = CreateObject('Excel.Application')
xl.Visible = 1
wb = xl.Workbooks.Add()
for i in range(10):
    xl.Range[f'A{i+1}'].Value[()] = f'group {i}'
wb.SaveAs(os.path.join(project_dir, 'data/groups.xlsx'))
xl.Quit()
