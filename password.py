password = input("Clave: ")

# Agregar prints para investigar
print(f"DEBUG tipo: {type(password)}")
print(f"DEBUG valor: [{password}]")
print(f"DEBUG len: {len(password)}")

# BUG: se compara string con int
if password == "1234":
    print("Acceso concedido")
else:
    print("Acceso denegado")