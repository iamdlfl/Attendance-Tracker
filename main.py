from modules.CountDictionary import CountDictionary #type: ignore

NUMBER_OF_TOP_CONTACTS = 100

result = CountDictionary(NUMBER_OF_TOP_CONTACTS)

result.write_csv()