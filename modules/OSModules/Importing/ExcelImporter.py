import pandas as pd #type: ignore

class ExcelImporter():

    col_1_names = ["Full Name", "Full name", "full name", "full", "Full", "FULL", "FULL NAME", "FULL_NAME", "Full_name", "Fullname", "fullname", "FULLNAME"]
    col_2_names = ["First Name", "First name", "first name", "first", "First", "FIRST", "FIRST NAME", "FIRST_NAME", "First_name", "Firstname", "firstname", "FIRSTNAME"]
    col_3_names = ["Last Name", "Last name", "last name", "last", "Last", "LAST", "LAST NAME", "LAST_NAME", "Last_name", "Lastname", "lastname", "LASTNAME"]
    col_4_names = ["Email", "E-mail", "EMAIL", "E-Mail", "email", "e-mail", "e-Mail"]

    def __init__(self, file_name):
        self.file_name = file_name
        self.excel_rows = []

    def import_excel(self):
        """Use Pandas to import Excel rows and convert to list of tuples"""
        print("importing Excel")
        df = pd.read_excel(self.file_name)
        records = df.to_records(index=False)
        results = list(records)
        for result in results:
            self.excel_rows.append((result[0], result[1], result[2], result[3]))

    def check_excel(self):
        print('checking excel')
        col_1, col_2, col_3, col_4 = self.excel_rows[0]
        if col_1.strip() not in self.col_1_names:
            self.excel_rows = []
            raise Exception("Please ensure that the first column is titled 'Full Name' and contains the full names of attendees. Self.excel_rows has been reset.")
        if col_2.strip() not in self.col_2_names:
            self.excel_rows = []
            raise Exception("Please ensure that the second column is titled 'First Name' and contains the first names of attendees. Self.excel_rows has been reset.")
        if col_3.strip() not in self.col_3_names:
            self.excel_rows = []
            raise Exception("Please ensure that the third column is titled 'Last Name' and contains the last names of attendees. Self.excel_rows has been reset.")
        if col_4.strip() not in self.col_4_names:
            self.excel_rows = []
            raise Exception("Please ensure that the fourth column is titled 'Email' and contains the emails of attendees. Self.excel_rows has been reset.")

    def get_excel_rows(self):
        return self.excel_rows[1:]

if __name__ == "__main__":
    pass
else:
    print('Importing ExcelImporter.py')
