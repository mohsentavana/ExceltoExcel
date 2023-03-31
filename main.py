# mohsenLinux
import pandas as pd
from openpyxl import load_workbook

# مشخص کردن فایل مبدا
file_path_src = "path/to/source_file.xlsx"
df_src = pd.read_excel(file_path_src)

# mohsenLinux
# مشخص کردن فایل مقصد
file_path_dst = "path/to/destination_file.xlsx"
book = load_workbook(file_path_dst)
writer = pd.ExcelWriter(file_path_dst, engine='openpyxl')
writer.book = book
writer.sheets = dict((ws.title, ws) for ws in book.worksheets)
# انتخاب ستون های مورد نظر
cols_to_transfer = ["نام", "نام خانوادگی"]

# انتقال داده ها
df_src[cols_to_transfer].to_excel(writer, index=False, sheet_name='Sheet1')
# writed by mohsenLinux
# ذخیره فایل مقصد
writer.save()
