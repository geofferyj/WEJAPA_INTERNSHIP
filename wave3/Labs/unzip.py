#Unzip Tuples
#Unzip the cast tuple into two names and heights tuples.

cast = (("Barney", 72), ("Robin", 68), ("Ted", 72), ("Lily", 66), ("Marshall", 76))

# define names and heights here
unzip = [x for x in zip(*cast)]
names = unzip[0]
heights = unzip[1]
print(names)
print(heights)