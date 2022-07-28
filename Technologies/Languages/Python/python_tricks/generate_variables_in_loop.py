# create variables with a loop and assign to them different names
# Useful link about globals() in python: https://www.programiz.com/python-programming/methods/built-in/globals

for i in ['1', '2', '3', '4', '5']:
    globals()[f"var_{i}"] = i
for var in [var_1, var_2, var_3, var_4, var_5]:
    print(var)