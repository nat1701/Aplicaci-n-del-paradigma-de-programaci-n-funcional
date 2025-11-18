Punto 9.
1. ¿Qué retorna el bloque de código? Retorna el conjunto final: {1, 3, 4}
2. ¿Cuántas funciones se declararon? Se declararon 2 funciones: agregar_elemento y eliminar_elemento
3. ¿Qué imprime en consola? El código no imprime nada, porque no tiene instrucciones print().
Punto 10.
a. ¿Cuál es el resultado? El resultado impreso es: [12, 15, 18]
b. ¿Qué hizo la función map con la función lambda? (explicación paso a paso)
map tomó la función lambda x, y, z: x + y + z y las tres listas.
Recorrió las listas en paralelo tomando un elemento de cada una:(1,4,7),(2,5,8),(3,6,9)
En cada iteración aplicó la función lambda:
1 + 4 + 7 = 12, 2 + 5 + 8 = 15, 3 + 6 + 9 = 18
print(list(resultado)) convirtió el resultado en una lista y lo imprimió.
El resultado final es:[12, 15, 18]
