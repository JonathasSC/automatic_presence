from datetime import date
from openpyxl import load_workbook
import re


class Spreadsheet:

    def __init__(self, filename: str):
        self.filename = filename

        self.TEACHER_LABEL_POSITION = 'A1'
        self.TEACHER_NAME_POSITION = 'B1'

        self.DATE_LABEL_POSITION = 'A2'
        self.DATE_POSITION = 'B2'

        self.NAME_LINE = 'A'
        self.PRESENCE_LINE = 'B'

    def load_file(self):
        spreadsheet_file = load_workbook(self.filename)
        spreadsheet_file.active

        try:
            spreadsheet_file.save(self.filename)
        except PermissionError as error:
            print(error)
            return False
        else:
            return spreadsheet_file

    def update_file(self):
        file = self.load_file()

        if file != False:
            sheet = file.active

            teacher_name = input('Teacher name: ').upper()
            today = date.today().strftime("%Y/%m/%d")

            sheet[self.TEACHER_LABEL_POSITION] = 'Professor'
            sheet[self.TEACHER_NAME_POSITION] = teacher_name

            sheet[self.DATE_LABEL_POSITION] = 'Data'
            sheet[self.DATE_POSITION] = today

            file.save(self.filename)

    def be_presence(self, name: str):
        file = self.load_file()

        if file != False:
            sheet = file.active

            for cell in sheet[self.NAME_LINE]:
                if cell.value == name:
                    match = re.search(r'\.([A-Za-z]+\d+)>', str(cell))

                    if match:
                        name_position = match.group(1).split(self.NAME_LINE)
                        mark_position = self.PRESENCE_LINE + name_position[1]

                        if sheet[mark_position].value != 'X':
                            sheet[mark_position].value = 'X'
                            file.save(self.filename)

                            print(f'{name} marcou presença')
