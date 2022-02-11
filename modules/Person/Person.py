class Person():

    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.__count = 1
    
    def __repr__(self):
        return self.email

    def __str__(self):
        return self.email

    @property
    def count(self):
        return self.__count

    @count.setter
    def count(self, number):
        self.__count = number

    def add(self):
        self.count += 1



if __name__ == "__main__":
    myPerson = Person("David", "djlynch@ufl.edu")
    myPerson2 = Person("David", "dlynch@ufl.edu")
    print(myPerson.count)
    myPerson.count += 1
    print(myPerson.count)
    my_list = [myPerson, myPerson2]

else:
    print("importing Person")