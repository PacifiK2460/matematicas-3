# Matemáticas III
## Matrices
### Equipo

| Integrante | Matricula |
| ---------- | --------- |
| Martínez Lara Santiago de la cruz | 177685 |
| Cabrera Meza Juan Antonio | 175166 |

### Definición: 
Una matriz $A$ de tamaño $m \times n$ es un arreglo rectangular de números reales con $m$ renglones y $n$ columnas. Si $A$ es una matriz de tamaño $m \times n$, entonces $A$ se denota como $A_{m \times n}$.

### Igualdad de matrices:
Sean las matrices $A = (a_{ij})$ de $m_1$ y $B = (b_{ij})$ de $m_2$ de tamaño $m \times n$. Entonces $A = B$ si y solo si:
- Son del mismo tamaño, es decir: $m_1 = m_2 = m$, $n_1 = n_2 = n$.
- Los componentes correspondientes son iguales, es decir: $a_{ij} = b_{ij}$ para todo $i \in[1,2 \dots m]$ y $j \in[1,2 \dots n]$.

### Tamaño de una matriz:
El tamaño de una matriz se define por $m \times n$, donde $m$ es el número de renglones y $n$ es el número de columnas.

### Notación:
Las matrices se representan dentro de paréntesis cuadrados en lugar de paréntesis normales, por ejemplo:

$$
A = \begin{bmatrix}
    1 & 2 & 3 \\
    4 & 5 & 6
\end{bmatrix}
$$

### Clasificación de matrices:

- **Rectangular**: Una matriz es rectangular si el número de renglones es diferente al número de columnas. $m \neq n$.
- **Cuadrada**: Una matriz es cuadrada si el número de renglones es igual al número de columnas. $m = n$.
- **Diagonal**: Una matriz es diagonal si todos sus componentes son cero, excepto los de la diagonal principal.
- **Identidad**: Una matriz es identidad si es cuadrada y todos sus componentes son cero, excepto los de la diagonal principal, los cuales son iguales a 1.
- **Transpuesta**: La transpuesta de una matriz $A$ de tamaño $m \times n$ es una matriz $B$ de tamaño $n \times m$ tal que $b_{ij} = a_{ji}$ para todo $i \in[1,2 \dots m]$ y $j \in[1,2 \dots n]$.
- **Simétrica**: Una matriz es simétrica si es cuadrada y es igual a su transpuesta.
- **Asimétrica**: Una matriz es asimétrica si es cuadrada y es igual al opuesto de su transpuesta.
- **Nula**: Una matriz es nula si todos sus componentes son cero.
- **Triangular superior**: Una matriz es triangular superior si todos sus componentes por debajo de la diagonal principal son cero.
- **Triangular inferior**: Una matriz es triangular inferior si todos sus componentes por encima de la diagonal principal son cero.
- **Escalar Unitaria**: Una matriz es escalar unitaria si es cuadrada y todos sus componentes son iguales a 1.

## Bibliografía
- Grossman, S. I. (2018). Álgebra lineal.