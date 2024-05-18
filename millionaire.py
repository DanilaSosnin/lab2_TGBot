import openpyxl
import random


def loadquests(g_round):
    count = 0
    book = openpyxl.open("questions.xlsx", read_only=True)

    sheet = book.worksheets[g_round]
    for row in sheet.iter_rows():
        count += 1
    selected_q = random.randint(1, count)
    return (str(sheet[selected_q][0].value), str(sheet[selected_q][1].value), str(sheet[selected_q][2].value), str(sheet[selected_q][3].value), str(sheet[selected_q][4].value), str(sheet[selected_q][5].value))