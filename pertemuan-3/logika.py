# Operator logika menggabungkan atau membalik nilai boolean.
# Hasil dari operator logika selalu berupa True atau False.

# NOT
# not membalik nilai boolean: True menjadi False, dan False menjadi True.
print(not True)   # False
print(not False)  # True

# AND
# and menghasilkan True hanya jika kedua operand bernilai True.
# Jika salah satu atau keduanya False, hasilnya adalah False.
print(True and True)    # True
print(True and False)   # False
print(False and True)   # False
print(False and False)  # False

# OR
# or menghasilkan True jika setidaknya satu operand bernilai True.
# Hanya menghasilkan False jika kedua operand bernilai False.
print(True or True)    # True
print(True or False)   # True
print(False or True)   # True
print(False or False)  # False