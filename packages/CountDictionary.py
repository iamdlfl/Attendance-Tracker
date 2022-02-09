from .CSVI.CSVImporter import CSVImporter #type: ignore
from .DirectoryFuncs.DirectorySearch import DirectorySearch #type: ignore
from .Writer.TXTWriter import TXTWriter #type: ignore

class CountDictionary():

    def __init__(self, top_contacts):
        print("init")
        self.dictionary = {}
        self.sorted_contact_list = []
        self.number_of_top_contacts = top_contacts
        self.csv_lines = []
        self.processed_lines = []
        self.top_contacts = []
        self.file_names = []
    
    def add_contact(self, contact):
        """Processes each contact and keeps track of how many times they have appeared in the list so far."""
        if contact not in self.dictionary.keys():
            self.dictionary[contact] = 1
        else:
            self.dictionary[contact] += 1
    
    def add_contact_list(self):
        """Uses add_contact() to add all people from current csv lines - based on their email currently. 
        This method adds the contents of self.csv_lines to self.processed lines once complete.
        This method then erases csv_lines (to prevent duplication if future CSVs are added)."""
        
        if not len(self.csv_lines):
            raise Exception('You have not processed a csv file yet, or it was empty. Please use the process_csv method first to add in a csv file.')
        for contact in self.csv_lines:
            try:
                self.add_contact(contact[3])
            except:
                raise Exception(f'There was a problem processing {contact}, which is located in line {self.csv_lines.index(contact)+1} of ' +
                'self.csv_lines. Please ensure that each contact has 4 pieces of data: Full name, first, last, email')
        print("adding contacts")
        self.processed_lines.append(self.csv_lines)
        self.csv_lines = []

    def count(self):
        print('getting count')
        self.set_file_names()
        for name in self.file_names:
            if not self.process_csv(name):
                print(f'Cancelling count() operation, will return results so far. Stopped at {name}')
                break
            self.add_contact_list()
            self.process_top_contacts()
        print('returning top contacts')
        return self.get_top_contacts()

    def get_dictionary(self):
        return self.dictionary

    def get_top_contacts(self):
        return self.top_contacts

    def process_top_contacts(self):
        """Sorts the dictionary keeping track of attendees and returns the top X contacts"""
        dictionary_copy = self.dictionary.copy()
        self.sorted_contact_list = [f'{k} - {v}' for k, v in sorted(dictionary_copy.items(), reverse=True, key=lambda item: item[1])]
        self.top_contacts = self.sorted_contact_list[:self.number_of_top_contacts]

    def process_csv(self, file_name):
        """Uses CSVImporter to process CSV files"""
        ImportedCSV = CSVImporter(file_name)
        ImportedCSV.import_csv()
        ImportedCSV.check_csv()
        if not len(ImportedCSV.csv_lines):
            raise Exception('There was an issue importing the CSV.')
    
        self.csv_lines = ImportedCSV.csv_lines[:]

        for processed in self.processed_lines:
            if self.csv_lines == processed:
                if input("It appears you have added an exact copy of a processed CSV, do you wish to continue? y/n: ") not in ['y', 'Y', 'yes', 'YES', 'Yes']:
                    print('You elected to not continue, resetting self.csv_lines now')
                    self.csv_lines = []
                    return False
        return True

    def set_file_names(self):
        DirSearch = DirectorySearch()
        self.file_names = DirSearch.search()

    def write_results(self):

        txt = TXTWriter(self.count())
        txt.write()    

if __name__ == "__main__":
    pass
else:
    print('Importing CountDictionary.py')

