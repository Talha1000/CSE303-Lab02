string = "Patience Problems to Drill List Comprehension in your Head"
words = string.split(" ")
s = [word for word in words if len(word) < 5]
print(s)