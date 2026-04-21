frutas = ["manzana", "banana", "naranja", "pera", "uva"]
print(frutas)
print(f"Tamaño de frutas: {len(frutas)}")
frutas.append("kiwi") # Agrega "kiwi" al final de la lista
print(frutas)
frutas.insert(2, "kiwi") # Inserta "kiwi" en la posición 2 (desplazando los elementos posteriores)
print(frutas)
frutas[2] = "aguacate" # Reemplaza el elemento en la posición 2 con "aguacate"
print(frutas)
frutas.reverse() # Invierte el orden de los elementos en la lista
print(frutas)
frutas.sort() # Ordena los elementos de la lista alfabéticamente
print(frutas)
#del frutas # Elimina la lista completa de frutas
frutas.append("kiwi") # Agrega "kiwi" al final de la lista
print(frutas.count("kiwi")) # Cuenta cuántas veces aparece "kiwi" en la lista
a = frutas.pop(1) # Elimina y devuelve el elemento en la posición 1 de la lista
print(a) # Imprime el elemento eliminado

frutas.remove("naranja") # Elimina la primera aparición de "naranja" en la lista
print(frutas)