import pandas as pd #type: ignore

class ExcelImporter():

    col_1_names = ["First Name", "First name", "first name", "first", "First", "FIRST", "FIRST NAME", "FIRST_NAME", "First_name", "Firstname", "firstname", "FIRSTNAME"]
    col_2_names = ["Last Name", "Last name", "last name", "last", "Last", "LAST", "LAST NAME", "LAST_NAME", "Last_name", "Lastname", "lastname", "LASTNAME"]
    col_3_names = ["Email", "E-mail", "EMAIL", "E-Mail", "email", "e-mail", "e-Mail"]

    def __init__(self, file_name):
        self.file_name = file_name
        self.excel_rows = []
        self.start = 0
        self.fname = 0
        self.lname = 0
        self.email = 0
        self.results = []

    def check_excel(self):
        """Checks and finds the column numbers for the necessary columns (First Name, Last Name, Email)"""
        for count, col_name in enumerate(self.excel_rows[self.start]):
            if col_name in self.col_1_names:
                self.fname = count
            if col_name in self.col_2_names:
                self.lname = count
            if col_name in self.col_3_names:
                self.email = count

    def import_excel(self):
        """Use Pandas to import Excel rows and convert to list of tuples"""
        df = pd.read_excel(self.file_name, header=None)
        records = df.to_records(index=False)
        results = list(records)
        for result in results:
            self.excel_rows.append((result))

    def get_attendee_start(self):
        """Goes through Excel file and finds at which row the attendee list starts
        This method then sets that start index as 'self.start' """
        start = 0
        if str(self.excel_rows[0][0]).strip().lower() == "attended": pass
        else:
            attendee_details = False
            for count, row in enumerate(self.excel_rows):
                if str(row[0]).strip().lower() == "panelist details":
                    attendee_details = False
                if str(row[0]).strip().lower() in ["attendee report", "attendee details"]:
                    attendee_details = True
                if (str(row[0]).strip().lower() == "attended") and attendee_details == True:
                    start = count
                    break

        self.start = start

    def package_relevant_rows(self):
        for row in self.excel_rows[self.start:]:
            if str(row[0]).strip().lower() == "yes":
                self.results.append((f'{row[self.fname]} {row[self.lname]}', row[self.fname], row[self.lname], row[self.email]))
    
    def process_excel(self):
        self.import_excel()
        self.get_attendee_start()
        self.check_excel()
        self.package_relevant_rows()
        return self.results
        




if __name__ == "__main__":
    import os 

    file_names = []
    direct = r'S:\ces\Staff-Restricted\David\Programs and Outreach\Coding\Utility\Attendees\CSV_FIles'

    for item in os.listdir(direct):
            item_name = os.path.join(direct, item)
            if os.path.isfile(item_name):
                file_names.append(item_name)
    for name in file_names[:1]:
        EI = ExcelImporter(name)
        print(EI.process_excel())

    
else:
    print('Importing ExcelImporter.py')
