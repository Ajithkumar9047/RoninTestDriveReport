from Config import *


def create_excel(rows_query):
    current_date = datetime.now().strftime('%d_%m_%Y')
    excel_file_name = os.path.join(path, f"TVS_roinin_leads_{current_date}.xlsx")
    
    wb = Workbook()
    ws_query = wb.active
    ws_query.title = "Report for morning"
    
    header_query1 = ["Dealer_ID", "Dealer_Name", "Zone", "Area", "State", "City", "Teri", "Indus_town", "total"]
    ws_query.append(header_query1)
    
    for cell in ws_query['1']:
        cell.fill = PatternFill(start_color='7EC0EE', end_color='7EC0EE', fill_type='solid')
    
    for row in rows_query:
        # Assuming the order of columns matches the header_query1
        row_values = [row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8]]
        ws_query.append(row_values)
    
    border_style = Side(style='thin')
    border = Border(left=border_style, right=border_style, top=border_style, bottom=border_style)
    
    for row in ws_query.iter_rows():
        for cell in row:
            cell.border = border
    
    wb.save(excel_file_name)
    logging.info("Excel file saved: %s", excel_file_name)
    return excel_file_name