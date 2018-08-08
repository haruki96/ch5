#P85
#tuple in list
locations = []

la = (34.0522, 188.2437)
chicago = (41.8781, 87.6298)

locations.append(la)
locations.append(chicago)

print("locations = ", locations)

#list in tuple
eights = ["Edgar Allan Poe", "Charles Dickens"]
nines = ["Hemingway", "Fitzerald", "Orwell"]

authors = (eights, nines)
print("authors = ", authors)

#dict in tuple, dict in list
bday = {"Hemingway":"7.21.1899",
        "Fitzerald":"9.24.1896"}
		
my_list = [bday]
print("my_list = ", my_list)
my_tuple = (bday,)
print("my_tuple = ", my_tuple)

