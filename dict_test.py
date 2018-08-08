#dict
my_dict = dict()
print(my_dict)
my_dict = {}
print(my_dict)


fruits = {"Apple":"Red", 
          "Banana":"Yellow"}
print("fruits = ", fruits)

#tsuika
facts = dict()
facts["code"] = "fun"
print("code =", facts["code"])
facts["Bill"] = "Gates"
facts["founded"] = "1776"
print("facts = ", facts)
print("founded = ", facts["founded"])

#in
bill = {"Bill Gates":"charitable"}
print("Bill Gates" in bill) #True
#not in 
print("Bill Doors" not in bill) #True

#del
books = {"Dracula":"Stoker",
         "1984":"Orwell",
		 "The Trial":"Kafka"}

del books["The Trial"]
print("books = ", books)


###dict_program
songs = {1:"fun",
         2:"bulue",
		 3:"me",
		 4:"floor",
		 5:"live"
		}
		
n = input("type a number.:")
if n in songs:
    print("song =", songs[n])
  
else:
    print("None")
###


###list_program
lists = []

rap = ["Kanie West", "Jei.Z", "Eminem", "Nazu"]
rock = ["Bob.D", "The Beatles", "Red"]
djs = ["Zeds Ded", "Tiest"]

lists.append(rap)
lists.append(rock)
lists.append(djs)
print("lists = ", lists)

rap = lists[0]
print("rap = ", rap)

rap.append("Kendrick Lammer")
print("rap = ", rap)
print("lists = ", lists)
###


