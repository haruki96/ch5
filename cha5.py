#1
my_favorite_arthist = ["RADWIMPS", "Ed Sheeran", "Yonedu Kenshi",
                       "Suda Masaki", "Aimer", "ONE OK ROCK", "Ozaki Yutaka", 
					   "The Chainsmokers", ]

print("#1")					   
print("my_favorite_arthist = ", my_favorite_arthist)


#2
Ebina = (35.443916, 139.379479)
Tokorozawa = (35.78651, 139.506518)
Obihiro = (42.933946, 143.171958)
Naha = (26.233207, 127.686916)

Place = [Ebina, Tokorozawa, Obihiro, Naha]
print("#2")
print("Place = ", Place)


#3
profile = {"name":"Yanase Haruki",
           "height":"172cm", 
           "weight":"51kg", 
		   "university":"Sophia univ.",
		   "hobby":"seeing movies"
		   }
		   
profile["age"] = [22]

print("#3")
print("profile = ", profile)
##4
#key = input("type the key of profile:")
#if key in profile:
#    print(profile[key])
#else:
#    print("None")

	
#5
favorite = {
        "RADWIMPS":["September sann", "saidaikouyakusu"],
        "Yonedu Kenshi":["gray and blue"],
   		"Suda Masaki":["mitakotomonaikesiki", "bakaninattyattanokana"],
		"ONE OK ROCK":["Be the light", "The Beginning"]
		}
print(favorite)
print(favorite["ONE OK ROCK"])

