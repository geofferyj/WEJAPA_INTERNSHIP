# Browse the complete list of string methods at:
# https://docs.python.org/3/library/stdtypes.html#string-methods 
#and try them out here. Endeavor to copy the link without the first # comment sign beginning it.
a = "bee sting" 
print(a.capitalize())
print(a.casefold())
print(a.center(12, "-"))
print(a.count("e"))
print(a.encode())
print(a.endswith("a"))
print(a.expandtabs())
print(a.find("e"))
print("{} and {}".format("me", "you"))
lunch = {"Food": "Pizza", "Drink": "Wine"}
print("Lunch: {Food}, {Drink}".format_map(lunch))
print(a.index("n"))
print(a.isalpha())
print(a.isdecimal())
print(a.isdigit())
print(a.isnumeric())
print(a.isidentifier())
print(a.islower())
print(a.isprintable())
print(a.isspace())
print(a.istitle())
print(a.isupper())
print("|".join(a))
print(a.ljust(12, "-"))
print(a.lower())
print(a.lstrip())
print(a.rstrip())
print(a.strip())
frm = "SecrtCod"
to = "12345678"
trans_table = str.maketrans(frm, to)
secret_code = "Secret Code".translate(trans_table)
print(secret_code)
print(a.partition(" "))
print(a.replace("e", "a"))
print(a.rjust(12, "-"))
print(a.rpartition(" "))
print(a.lstrip())
print(a.rstrip())
print(a.strip())
print(a.splitlines())
print(a.startswith("b"))
print(a.swapcase())
print(a.title())
print(a.upper())
print(a.zfill(5))








