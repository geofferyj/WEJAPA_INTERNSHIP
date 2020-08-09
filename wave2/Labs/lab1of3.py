# Use this playground to experiment with list methods, using Test Run
list_a = range(10)
list_b = [2, 4, 5, 6, 7, 5, 4, 4, 4, 55, 3, 2, 2, 23, 3, 4, 5, 6]
list_c = ["cat", "dog", "goat", "ken", "chicken", "bond", "james bond"]

# join
print(" -|- ".join(list_c))

# sort
list_b.sort()
print(list_b)

# append
list_b.append(45)
print(list_b)

# extend
list_c.extend(["kittens", "puppies", "kids", "chicks"])
print(list_c)

# sorted
print(sorted(list_c))


