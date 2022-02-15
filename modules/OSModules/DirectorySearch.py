import os

class DirectorySearch():
    
    def __init__(self, directory_location = r"S:\ces\Staff-Restricted\David\Programs and Outreach\Coding\Utility\Attendees\CSV_Files" ):
        self.dir_loc = directory_location
        self.file_names = []

    def search(self):
        print("doing search")
        self.set_csv_file_names()
        return self.get_file_names()

    def set_csv_file_names(self):
        """Set the directory path and then get all CSV files from that directory"""
        self.set_dir()
        for item in os.listdir(self.dir):
            item_name = os.path.join(self.dir, item)
            if os.path.isfile(item_name):
                self.file_names.append(item_name)

    def set_dir(self):
        self.dir = os.fspath(self.dir_loc)

    def get_dir(self):
        return self.dir

    def get_file_names(self):
        return self.file_names

if __name__ == "__main__":
    d=DirectorySearch()
    d.set_csv_file_names()
    print(d.get_file_names())
else:
    print("Importing DirectorySearch.py")