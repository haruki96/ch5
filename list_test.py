#list

fruit = list()
print(fruit)


fruit = []
print(fruit)

fruit = ["Apple", "Orange", "Pear"]
print(fruit)

#toridasi
fruit.append("Baanana")
fruit.append("Peach")
print("fruit = ", fruit)
print("fruit_0 = ", fruit[0])
print(fruit[1])
print(fruit[2])


#append
random =[]
random.append(True)
random.append(100)
random.append(1.1)
random.append("Hello")
print("random = ", random)


#henkoukanou
colors = ["blue", "green", "yellow"]
colors[2] = "red"
print("colors = ", colors)
#pop
item = colors.pop()
print("item = ", item) #pop sarerumono
print("colors= ", colors)
#in
print("green" in colors) #True
print("black" not in colors) #True
#len
print(len(colors))



#plus
colors1 = ["blue", "green", "yellow"]
colors2 = ["orange", "pink", "black"]
print("colors1 = ", colors1, "colors2 = ", colors2)
print("(colors1 + colors2) = ", colors1 + colors2)


