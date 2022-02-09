import csv

class CSVImporter():

    col_1_names = ["Full Name", "Full name", "full name", "full", "Full", "FULL", "FULL NAME", "FULL_NAME", "Full_name", "Fullname", "fullname", "FULLNAME"]
    col_2_names = ["First Name", "First name", "first name", "first", "First", "FIRST", "FIRST NAME", "FIRST_NAME", "First_name", "Firstname", "firstname", "FIRSTNAME"]
    col_3_names = ["Last Name", "Last name", "last name", "last", "Last", "LAST", "LAST NAME", "LAST_NAME", "Last_name", "Lastname", "lastname", "LASTNAME"]
    col_4_names = ["Email", "E-mail", "EMAIL", "E-Mail", "email", "e-mail", "e-Mail"]

    def __init__(self, file_name):
        self.file_name = file_name
        self.csv_lines = []

    def import_csv(self):
        with open(self.file_name, 'r', encoding='utf-8-sig') as list_file:
            csv_file = csv.reader(list_file)
            for line in csv_file:
                self.csv_lines.append(line)

    def check_csv(self):
        col_1, col_2, col_3, col_4 = self.csv_lines[0]
        if col_1.strip() not in self.col_1_names:
            self.csv_lines = []
            raise Exception("Please ensure that the first column is titled 'Full Name' and contains the full names of attendees. Self.csv_lines has been reset.")
        if col_2.strip() not in self.col_2_names:
            self.csv_lines = []
            raise Exception("Please ensure that the second column is titled 'First Name' and contains the first names of attendees. Self.csv_lines has been reset.")
        if col_3.strip() not in self.col_3_names:
            self.csv_lines = []
            raise Exception("Please ensure that the third column is titled 'Last Name' and contains the last names of attendees. Self.csv_lines has been reset.")
        if col_4.strip() not in self.col_4_names:
            self.csv_lines = []
            raise Exception("Please ensure that the fourth column is titled 'Email' and contains the emails of attendees. Self.csv_lines has been reset.")
        
    def get_csv_lines(self):
        return self.csv_lines[1:]
        

if __name__ == "__main__":
    pass
else:
    print('Importing CSVImporter.py')

