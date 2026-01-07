import random

# Inteiros
array_int = [random.randint(1, 100) for _ in range(15)]
array_int.sort()
print(array_int)

array_int.sort(key=None, reverse=True)
print(array_int)

# Strings
array_str = ["nome", "dataNascimento", "cpf", "rg"]
array_str.sort()
print(array_str)

array_str.sort(key=None, reverse=True)
print(array_str)