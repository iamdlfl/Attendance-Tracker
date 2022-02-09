import os

class TXTWriter():

    def __init__(self, list_to_write, location= r"S:\ces\Staff-Restricted\David\Programs and Outreach\Coding\Utility\Attendees"):
        self.results = list_to_write
        self.location = location

    def write(self):
        print("writing txt")
        path = os.path.join(self.location, 'Results.txt')
        with open(path, 'w') as my_file:
            print('writing results')
            for item in self.results:
                print(item)
                my_file.write(f'{item} \n')
        