#assigning elements to different lists
fruits = ["Apple", "Dragonfruit"]
cars = ["Audi", "Tesla", "Kia"]
print(cars + fruits)
fruits.insert(1, "Banana")
fruits.extend(("Mango", "Kiwi"))
cars.append("BMW")
cars.insert(0, "Jaguar")
print(fruits)
print(cars)
del cars[2]
del fruits[0]
print(fruits)
print(cars)
print(fruits.index("Mango"))
print("----------------------------------------")
#accessing elements from a tuple
lang = ("Java", "Python", "C")
print("This is the tuple = ", lang)
print("Element at index 1 = ", lang[1])
print("Element at index 0 = ", lang[0])
print("Length of tuple, lang = ", len(lang))
print("----------------------------------------")
#deleting different dictionary elements
marks = {
    "Math":89,
    "Science":81,
    "History":90,
    "Art":99
}
print(marks)
del marks["History"]
print(marks)
del marks["Math"]
print(marks)
