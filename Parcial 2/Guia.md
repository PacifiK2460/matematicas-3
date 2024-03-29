### Subespacios Vectoriales

1. Determine si los siguientes conjuntos son sub-espacios vectoriales:

a) $V = M_{22}; H = \{ A = \begin{pmatrix} 0 & a \\ -a & 0\end{pmatrix}, a \in R \}$

b) $V = M_{22}; H = \{A = \begin{pmatrix}a& b \\ -b &c \end{pmatrix},a,b,c\in R\}$

c) $V = P_4; H = \{ p \in P_4: P(0) = 0\}$

d) $V = R^3; H = \{ \begin{pmatrix}a\\b\\c\end{pmatrix}, x^2 + y^2 + z^2 - (vt)^2 = 1 \}$

### Combinación Lineal

1. Dados los vectores $u = (2,1,4)$, $v = (1,-1,3)$ y $w = (3,2,5)$. Exprese los siguientes vectores como combinaciones lineales de $u$,$v$ y $w$.

a) $(5,5,9)$

$$
\left[\begin{matrix}2 & 1 & 3 & 5\\1 & -1 & 2 & 5\\4 & 3 & 5 & 9\end{matrix}\right]
\underrightarrow{ R_{3} \leftrightarrow R_{1} }
\left[\begin{matrix}4 & 3 & 5 & 9\\1 & -1 & 2 & 5\\2 & 1 & 3 & 5\end{matrix}\right]
\underrightarrow{ R_2 + (- \frac{1}{4})R_1 } \\
\left[\begin{matrix}4 & 3 & 5 & 9\\0 & - \frac{7}{4} & \frac{3}{4} & \frac{11}{4}\\2 & 1 & 3 & 5\end{matrix}\right]
\underrightarrow{ R_3 + (- \frac{1}{2})R_1 }
\left[\begin{matrix}4 & 3 & 5 & 9\\0 & - \frac{7}{4} & \frac{3}{4} & \frac{11}{4}\\0 & - \frac{1}{2} & \frac{1}{2} & \frac{1}{2}\end{matrix}\right]
\underrightarrow{ R_{2} \leftrightarrow R_{2} } \\
\left[\begin{matrix}4 & 3 & 5 & 9\\0 & - \frac{7}{4} & \frac{3}{4} & \frac{11}{4}\\0 & - \frac{1}{2} & \frac{1}{2} & \frac{1}{2}\end{matrix}\right]
\underrightarrow{ R_3 + (- \frac{2}{7})R_2 }
\left[\begin{matrix}4 & 3 & 5 & 9\\0 & - \frac{7}{4} & \frac{3}{4} & \frac{11}{4}\\0 & 0 & \frac{2}{7} & - \frac{2}{7}\end{matrix}\right]
\underrightarrow{ R_{3} \leftrightarrow R_{3} } \\
\left[\begin{matrix}4 & 3 & 5 & 9\\0 & - \frac{7}{4} & \frac{3}{4} & \frac{11}{4}\\0 & 0 & \frac{2}{7} & - \frac{2}{7}\end{matrix}\right]
\underrightarrow{ \frac{R_3}{\frac{2}{7}} }
\left[\begin{matrix}4 & 3 & 5 & 9\\0 & - \frac{7}{4} & \frac{3}{4} & \frac{11}{4}\\0 & 0 & 1 & -1\end{matrix}\right]
\underrightarrow{ R_2 + (- \frac{3}{4})R_3 } \\
\left[\begin{matrix}4 & 3 & 5 & 9\\0 & - \frac{7}{4} & 0 & \frac{7}{2}\\0 & 0 & 1 & -1\end{matrix}\right]
\underrightarrow{ R_1 + (-5)R_3 }
\left[\begin{matrix}4 & 3 & 0 & 14\\0 & - \frac{7}{4} & 0 & \frac{7}{2}\\0 & 0 & 1 & -1\end{matrix}\right]
\underrightarrow{ \frac{R_2}{- \frac{7}{4}} } \\
\left[\begin{matrix}4 & 3 & 0 & 14\\0 & 1 & 0 & -2\\0 & 0 & 1 & -1\end{matrix}\right]
\underrightarrow{ R_1 + (-3)R_2 }
\left[\begin{matrix}4 & 0 & 0 & 20\\0 & 1 & 0 & -2\\0 & 0 & 1 & -1\end{matrix}\right]
\underrightarrow{ \frac{R_1}{4} }
\left[\begin{matrix}1 & 0 & 0 & 5\\0 & 1 & 0 & -2\\0 & 0 & 1 & -1\end{matrix}\right]
$$

b) $(2,0,6)$

$$
\left[\begin{matrix}2 & 1 & 3 & 2\\1 & -1 & 2 & 0\\4 & 3 & 5 & 6\end{matrix}\right]
\underrightarrow{ R_{3} \leftrightarrow R_{1} }
\left[\begin{matrix}4 & 3 & 5 & 6\\1 & -1 & 2 & 0\\2 & 1 & 3 & 2\end{matrix}\right]
\underrightarrow{ R_2 + (- \frac{1}{4})R_1 }
\left[\begin{matrix}4 & 3 & 5 & 6\\0 & - \frac{7}{4} & \frac{3}{4} & - \frac{3}{2}\\2 & 1 & 3 & 2\end{matrix}\right]
\underrightarrow{ R_3 + (- \frac{1}{2})R_1 }
\\
\left[\begin{matrix}4 & 3 & 5 & 6\\0 & - \frac{7}{4} & \frac{3}{4} & - \frac{3}{2}\\0 & - \frac{1}{2} & \frac{1}{2} & -1\end{matrix}\right]
\underrightarrow{ R_{2} \leftrightarrow R_{2} }
\left[\begin{matrix}4 & 3 & 5 & 6\\0 & - \frac{7}{4} & \frac{3}{4} & - \frac{3}{2}\\0 & - \frac{1}{2} & \frac{1}{2} & -1\end{matrix}\right]
\underrightarrow{ R_3 + (- \frac{2}{7})R_2 }
\\
\left[\begin{matrix}4 & 3 & 5 & 6\\0 & - \frac{7}{4} & \frac{3}{4} & - \frac{3}{2}\\0 & 0 & \frac{2}{7} & - \frac{4}{7}\end{matrix}\right]
\underrightarrow{ R_{3} \leftrightarrow R_{3} }
\left[\begin{matrix}4 & 3 & 5 & 6\\0 & - \frac{7}{4} & \frac{3}{4} & - \frac{3}{2}\\0 & 0 & \frac{2}{7} & - \frac{4}{7}\end{matrix}\right]
\underrightarrow{ \frac{R_3}{\frac{2}{7}} }
\left[\begin{matrix}4 & 3 & 5 & 6\\0 & - \frac{7}{4} & \frac{3}{4} & - \frac{3}{2}\\0 & 0 & 1 & -2\end{matrix}\right]
\underrightarrow{ R_2 + (- \frac{3}{4})R_3 }
\left[\begin{matrix}4 & 3 & 5 & 6\\0 & - \frac{7}{4} & 0 & 0\\0 & 0 & 1 & -2\end{matrix}\right]
\underrightarrow{ R_1 + (-5)R_3 }
\\
\left[\begin{matrix}4 & 3 & 0 & 16\\0 & - \frac{7}{4} & 0 & 0\\0 & 0 & 1 & -2\end{matrix}\right]
\underrightarrow{ \frac{R_2}{- \frac{7}{4}} }
\left[\begin{matrix}4 & 3 & 0 & 16\\0 & 1 & 0 & 0\\0 & 0 & 1 & -2\end{matrix}\right]
\underrightarrow{ R_1 + (-3)R_2 }
\\
\left[\begin{matrix}4 & 0 & 0 & 16\\0 & 1 & 0 & 0\\0 & 0 & 1 & -2\end{matrix}\right]
\underrightarrow{ \frac{R_1}{4} }
\left[\begin{matrix}1 & 0 & 0 & 4\\0 & 1 & 0 & 0\\0 & 0 & 1 & -2\end{matrix}\right]
$$

c) $(2,2,3)$

$$
\left[\begin{matrix}2 & 1 & 3 & 2\\1 & -1 & 2 & 2\\4 & 3 & 5 & 3\end{matrix}\right]
\underrightarrow{ R_{3} \leftrightarrow R_{1} }
\left[\begin{matrix}4 & 3 & 5 & 3\\1 & -1 & 2 & 2\\2 & 1 & 3 & 2\end{matrix}\right]
\underrightarrow{ R_2 + (- \frac{1}{4})R_1 }
\left[\begin{matrix}4 & 3 & 5 & 3\\0 & - \frac{7}{4} & \frac{3}{4} & \frac{5}{4}\\2 & 1 & 3 & 2\end{matrix}\right]
\underrightarrow{ R_3 + (- \frac{1}{2})R_1 }
\\
\left[\begin{matrix}4 & 3 & 5 & 3\\0 & - \frac{7}{4} & \frac{3}{4} & \frac{5}{4}\\0 & - \frac{1}{2} & \frac{1}{2} & \frac{1}{2}\end{matrix}\right]
\underrightarrow{ R_{2} \leftrightarrow R_{2} }
\left[\begin{matrix}4 & 3 & 5 & 3\\0 & - \frac{7}{4} & \frac{3}{4} & \frac{5}{4}\\0 & - \frac{1}{2} & \frac{1}{2} & \frac{1}{2}\end{matrix}\right]
\underrightarrow{ R_3 + (- \frac{2}{7})R_2 }
\\
\left[\begin{matrix}4 & 3 & 5 & 3\\0 & - \frac{7}{4} & \frac{3}{4} & \frac{5}{4}\\0 & 0 & \frac{2}{7} & \frac{1}{7}\end{matrix}\right]
\underrightarrow{ R_{3} \leftrightarrow R_{3} }
\left[\begin{matrix}4 & 3 & 5 & 3\\0 & - \frac{7}{4} & \frac{3}{4} & \frac{5}{4}\\0 & 0 & \frac{2}{7} & \frac{1}{7}\end{matrix}\right]
\underrightarrow{ \frac{R_3}{\frac{2}{7}} }
\left[\begin{matrix}4 & 3 & 5 & 3\\0 & - \frac{7}{4} & \frac{3}{4} & \frac{5}{4}\\0 & 0 & 1 & \frac{1}{2}\end{matrix}\right]
\underrightarrow{ R_2 + (- \frac{3}{4})R_3 }
\left[\begin{matrix}4 & 3 & 5 & 3\\0 & - \frac{7}{4} & 0 & \frac{7}{8}\\0 & 0 & 1 & \frac{1}{2}\end{matrix}\right]
\underrightarrow{ R_1 + (-5)R_3 }
\\
\left[\begin{matrix}4 & 3 & 0 & \frac{1}{2}\\0 & - \frac{7}{4} & 0 & \frac{7}{8}\\0 & 0 & 1 & \frac{1}{2}\end{matrix}\right]
\underrightarrow{ \frac{R_2}{- \frac{7}{4}} }
\left[\begin{matrix}4 & 3 & 0 & \frac{1}{2}\\0 & 1 & 0 & - \frac{1}{2}\\0 & 0 & 1 & \frac{1}{2}\end{matrix}\right]
\underrightarrow{ R_1 + (-3)R_2 }
\\
\left[\begin{matrix}4 & 0 & 0 & 2\\0 & 1 & 0 & - \frac{1}{2}\\0 & 0 & 1 & \frac{1}{2}\end{matrix}\right]
\underrightarrow{ \frac{R_1}{4} }
\left[\begin{matrix}1 & 0 & 0 & \frac{1}{2}\\0 & 1 & 0 & - \frac{1}{2}\\0 & 0 & 1 & \frac{1}{2}\end{matrix}\right]
$$

d) $(-1,3,\frac{1}{2})$

$$
\left[\begin{matrix}2 & 1 & 3 & -1.0\\1 & -1 & 2 & 3.0\\4 & 3 & 5 & 0.5\end{matrix}\right]
\underrightarrow{ R_{3} \leftrightarrow R_{1} }
\left[\begin{matrix}4 & 3 & 5 & 0.5\\1 & -1 & 2 & 3.0\\2 & 1 & 3 & -1.0\end{matrix}\right]
\underrightarrow{ R_2 + (- \frac{1}{4})R_1 }
\left[\begin{matrix}4 & 3 & 5 & 0.5\\0 & - \frac{7}{4} & \frac{3}{4} & 2.875\\2 & 1 & 3 & -1.0\end{matrix}\right]
\underrightarrow{ R_3 + (- \frac{1}{2})R_1 }
\\
\left[\begin{matrix}4 & 3 & 5 & 0.5\\0 & - \frac{7}{4} & \frac{3}{4} & 2.875\\0 & - \frac{1}{2} & \frac{1}{2} & -1.25\end{matrix}\right]
\underrightarrow{ R_{2} \leftrightarrow R_{2} }
\left[\begin{matrix}4 & 3 & 5 & 0.5\\0 & - \frac{7}{4} & \frac{3}{4} & 2.875\\0 & - \frac{1}{2} & \frac{1}{2} & -1.25\end{matrix}\right]
\underrightarrow{ R_3 + (- \frac{2}{7})R_2 }
\\
\left[\begin{matrix}4 & 3 & 5 & 0.5\\0 & - \frac{7}{4} & \frac{3}{4} & 2.875\\0 & 0 & \frac{2}{7} & -2.07142857142857\end{matrix}\right]
\underrightarrow{ R_{3} \leftrightarrow R_{3} }
\left[\begin{matrix}4 & 3 & 5 & 0.5\\0 & - \frac{7}{4} & \frac{3}{4} & 2.875\\0 & 0 & \frac{2}{7} & -2.07142857142857\end{matrix}\right]
\underrightarrow{ \frac{R_3}{\frac{2}{7}} }
\left[\begin{matrix}4 & 3 & 5 & 0.5\\0 & - \frac{7}{4} & \frac{3}{4} & 2.875\\0 & 0 & 1 & -7.25\end{matrix}\right]
\underrightarrow{ R_2 + (- \frac{3}{4})R_3 }
\left[\begin{matrix}4 & 3 & 5 & 0.5\\0 & - \frac{7}{4} & 0 & 8.3125\\0 & 0 & 1 & -7.25\end{matrix}\right]
\underrightarrow{ R_1 + (-5)R_3 }
\\
\left[\begin{matrix}4 & 3 & 0 & 36.75\\0 & - \frac{7}{4} & 0 & 8.3125\\0 & 0 & 1 & -7.25\end{matrix}\right]
\underrightarrow{ \frac{R_2}{- \frac{7}{4}} }
\left[\begin{matrix}4 & 3 & 0 & 36.75\\0 & 1 & 0 & -4.75\\0 & 0 & 1 & -7.25\end{matrix}\right]
\underrightarrow{ R_1 + (-3)R_2 }
\\
\left[\begin{matrix}4 & 0 & 0 & 51.0\\0 & 1 & 0 & -4.75\\0 & 0 & 1 & -7.25\end{matrix}\right]
\underrightarrow{ \frac{R_1}{4} }
\left[\begin{matrix}1 & 0 & 0 & 12.75\\0 & 1 & 0 & -4.75\\0 & 0 & 1 & -7.25\end{matrix}\right]
$$

2. Si $p_1 = 2 + x + 4x^2$, $p_2 = 1 - x + 3x^2$ y $p_3 = 3+2x+5x^2$. Exprese los siguientes polinomios como una combinación de $p_1$, $p_2$ y $p_3$.

a) $9x+5-5x^2$

$$
\left[\begin{matrix}4 & 3 & 5 & -5\\1 & -1 & 2 & 9\\2 & 1 & 3 & 5\end{matrix}\right]
\underrightarrow{ R_{1} \leftrightarrow R_{1} }
\left[\begin{matrix}4 & 3 & 5 & -5\\1 & -1 & 2 & 9\\2 & 1 & 3 & 5\end{matrix}\right]
\underrightarrow{ R_2 + (- \frac{1}{4})R_1 }
\left[\begin{matrix}4 & 3 & 5 & -5\\0 & - \frac{7}{4} & \frac{3}{4} & \frac{41}{4}\\2 & 1 & 3 & 5\end{matrix}\right]
\underrightarrow{ R_3 + (- \frac{1}{2})R_1 }
\\
\left[\begin{matrix}4 & 3 & 5 & -5\\0 & - \frac{7}{4} & \frac{3}{4} & \frac{41}{4}\\0 & - \frac{1}{2} & \frac{1}{2} & \frac{15}{2}\end{matrix}\right]
\underrightarrow{ R_{2} \leftrightarrow R_{2} }
\left[\begin{matrix}4 & 3 & 5 & -5\\0 & - \frac{7}{4} & \frac{3}{4} & \frac{41}{4}\\0 & - \frac{1}{2} & \frac{1}{2} & \frac{15}{2}\end{matrix}\right]
\underrightarrow{ R_3 + (- \frac{2}{7})R_2 }
\\
\left[\begin{matrix}4 & 3 & 5 & -5\\0 & - \frac{7}{4} & \frac{3}{4} & \frac{41}{4}\\0 & 0 & \frac{2}{7} & \frac{32}{7}\end{matrix}\right]
\underrightarrow{ R_{3} \leftrightarrow R_{3} }
\left[\begin{matrix}4 & 3 & 5 & -5\\0 & - \frac{7}{4} & \frac{3}{4} & \frac{41}{4}\\0 & 0 & \frac{2}{7} & \frac{32}{7}\end{matrix}\right]
\underrightarrow{ \frac{R_3}{\frac{2}{7}} }
\left[\begin{matrix}4 & 3 & 5 & -5\\0 & - \frac{7}{4} & \frac{3}{4} & \frac{41}{4}\\0 & 0 & 1 & 16\end{matrix}\right]
\underrightarrow{ R_2 + (- \frac{3}{4})R_3 }
\left[\begin{matrix}4 & 3 & 5 & -5\\0 & - \frac{7}{4} & 0 & - \frac{7}{4}\\0 & 0 & 1 & 16\end{matrix}\right]
\underrightarrow{ R_1 + (-5)R_3 }
\\
\left[\begin{matrix}4 & 3 & 0 & -85\\0 & - \frac{7}{4} & 0 & - \frac{7}{4}\\0 & 0 & 1 & 16\end{matrix}\right]
\underrightarrow{ \frac{R_2}{- \frac{7}{4}} }
\left[\begin{matrix}4 & 3 & 0 & -85\\0 & 1 & 0 & 1\\0 & 0 & 1 & 16\end{matrix}\right]
\underrightarrow{ R_1 + (-3)R_2 }
\\
\left[\begin{matrix}4 & 0 & 0 & -88\\0 & 1 & 0 & 1\\0 & 0 & 1 & 16\end{matrix}\right]
\underrightarrow{ \frac{R_1}{4} }
\left[\begin{matrix}1 & 0 & 0 & -22\\0 & 1 & 0 & 1\\0 & 0 & 1 & 16\end{matrix}\right]
$$

b) $2+6x^2$

$$
\left[\begin{matrix}4 & 3 & 5 & 6\\1 & -1 & 2 & 0\\2 & 1 & 3 & 2\end{matrix}\right]
\underrightarrow{ R_{1} \leftrightarrow R_{1} }
\left[\begin{matrix}4 & 3 & 5 & 6\\1 & -1 & 2 & 0\\2 & 1 & 3 & 2\end{matrix}\right]
\underrightarrow{ R_2 + (- \frac{1}{4})R_1 }
\left[\begin{matrix}4 & 3 & 5 & 6\\0 & - \frac{7}{4} & \frac{3}{4} & - \frac{3}{2}\\2 & 1 & 3 & 2\end{matrix}\right]
\underrightarrow{ R_3 + (- \frac{1}{2})R_1 }
\\
\left[\begin{matrix}4 & 3 & 5 & 6\\0 & - \frac{7}{4} & \frac{3}{4} & - \frac{3}{2}\\0 & - \frac{1}{2} & \frac{1}{2} & -1\end{matrix}\right]
\underrightarrow{ R_{2} \leftrightarrow R_{2} }
\left[\begin{matrix}4 & 3 & 5 & 6\\0 & - \frac{7}{4} & \frac{3}{4} & - \frac{3}{2}\\0 & - \frac{1}{2} & \frac{1}{2} & -1\end{matrix}\right]
\underrightarrow{ R_3 + (- \frac{2}{7})R_2 }
\\
\left[\begin{matrix}4 & 3 & 5 & 6\\0 & - \frac{7}{4} & \frac{3}{4} & - \frac{3}{2}\\0 & 0 & \frac{2}{7} & - \frac{4}{7}\end{matrix}\right]
\underrightarrow{ R_{3} \leftrightarrow R_{3} }
\left[\begin{matrix}4 & 3 & 5 & 6\\0 & - \frac{7}{4} & \frac{3}{4} & - \frac{3}{2}\\0 & 0 & \frac{2}{7} & - \frac{4}{7}\end{matrix}\right]
\underrightarrow{ \frac{R_3}{\frac{2}{7}} }
\left[\begin{matrix}4 & 3 & 5 & 6\\0 & - \frac{7}{4} & \frac{3}{4} & - \frac{3}{2}\\0 & 0 & 1 & -2\end{matrix}\right]
\underrightarrow{ R_2 + (- \frac{3}{4})R_3 }
\left[\begin{matrix}4 & 3 & 5 & 6\\0 & - \frac{7}{4} & 0 & 0\\0 & 0 & 1 & -2\end{matrix}\right]
\underrightarrow{ R_1 + (-5)R_3 }
\\
\left[\begin{matrix}4 & 3 & 0 & 16\\0 & - \frac{7}{4} & 0 & 0\\0 & 0 & 1 & -2\end{matrix}\right]
\underrightarrow{ \frac{R_2}{- \frac{7}{4}} }
\left[\begin{matrix}4 & 3 & 0 & 16\\0 & 1 & 0 & 0\\0 & 0 & 1 & -2\end{matrix}\right]
\underrightarrow{ R_1 + (-3)R_2 }
\\
\left[\begin{matrix}4 & 0 & 0 & 16\\0 & 1 & 0 & 0\\0 & 0 & 1 & -2\end{matrix}\right]
\underrightarrow{ \frac{R_1}{4} }
\left[\begin{matrix}1 & 0 & 0 & 4\\0 & 1 & 0 & 0\\0 & 0 & 1 & -2\end{matrix}\right]
$$

c) $3-2^{-1}x^2 + x$

$$
\left[\begin{matrix}4 & 3 & 5 & -0.5\\1 & -1 & 2 & 1.0\\2 & 1 & 3 & 3.0\end{matrix}\right]
\underrightarrow{ R_{1} \leftrightarrow R_{1} }
\left[\begin{matrix}4 & 3 & 5 & -0.5\\1 & -1 & 2 & 1.0\\2 & 1 & 3 & 3.0\end{matrix}\right]
\underrightarrow{ R_2 + (- \frac{1}{4})R_1 }
\left[\begin{matrix}4 & 3 & 5 & -0.5\\0 & - \frac{7}{4} & \frac{3}{4} & 1.125\\2 & 1 & 3 & 3.0\end{matrix}\right]
\underrightarrow{ R_3 + (- \frac{1}{2})R_1 }
\\
\left[\begin{matrix}4 & 3 & 5 & -0.5\\0 & - \frac{7}{4} & \frac{3}{4} & 1.125\\0 & - \frac{1}{2} & \frac{1}{2} & 3.25\end{matrix}\right]
\underrightarrow{ R_{2} \leftrightarrow R_{2} }
\left[\begin{matrix}4 & 3 & 5 & -0.5\\0 & - \frac{7}{4} & \frac{3}{4} & 1.125\\0 & - \frac{1}{2} & \frac{1}{2} & 3.25\end{matrix}\right]
\underrightarrow{ R_3 + (- \frac{2}{7})R_2 }
\\
\left[\begin{matrix}4 & 3 & 5 & -0.5\\0 & - \frac{7}{4} & \frac{3}{4} & 1.125\\0 & 0 & \frac{2}{7} & 2.92857142857143\end{matrix}\right]
\underrightarrow{ R_{3} \leftrightarrow R_{3} }
\left[\begin{matrix}4 & 3 & 5 & -0.5\\0 & - \frac{7}{4} & \frac{3}{4} & 1.125\\0 & 0 & \frac{2}{7} & 2.92857142857143\end{matrix}\right]
\underrightarrow{ \frac{R_3}{\frac{2}{7}} }
\left[\begin{matrix}4 & 3 & 5 & -0.5\\0 & - \frac{7}{4} & \frac{3}{4} & 1.125\\0 & 0 & 1 & 10.25\end{matrix}\right]
\underrightarrow{ R_2 + (- \frac{3}{4})R_3 }
\left[\begin{matrix}4 & 3 & 5 & -0.5\\0 & - \frac{7}{4} & 0 & -6.5625\\0 & 0 & 1 & 10.25\end{matrix}\right]
\underrightarrow{ R_1 + (-5)R_3 }
\\
\left[\begin{matrix}4 & 3 & 0 & -51.75\\0 & - \frac{7}{4} & 0 & -6.5625\\0 & 0 & 1 & 10.25\end{matrix}\right]
\underrightarrow{ \frac{R_2}{- \frac{7}{4}} }
\left[\begin{matrix}4 & 3 & 0 & -51.75\\0 & 1 & 0 & 3.75\\0 & 0 & 1 & 10.25\end{matrix}\right]
\underrightarrow{ R_1 + (-3)R_2 }
\\
\left[\begin{matrix}4 & 0 & 0 & -63.0\\0 & 1 & 0 & 3.75\\0 & 0 & 1 & 10.25\end{matrix}\right]
\underrightarrow{ \frac{R_1}{4} }
\left[\begin{matrix}1 & 0 & 0 & -15.75\\0 & 1 & 0 & 3.75\\0 & 0 & 1 & 10.25\end{matrix}\right]
$$

d) $7x-2x^2+1$

$$
\left[\begin{matrix}4 & 3 & 5 & -2\\1 & -1 & 2 & 7\\2 & 1 & 3 & 1\end{matrix}\right]
\underrightarrow{ R_{1} \leftrightarrow R_{1} }
\left[\begin{matrix}4 & 3 & 5 & -2\\1 & -1 & 2 & 7\\2 & 1 & 3 & 1\end{matrix}\right]
\underrightarrow{ R_2 + (- \frac{1}{4})R_1 }
\left[\begin{matrix}4 & 3 & 5 & -2\\0 & - \frac{7}{4} & \frac{3}{4} & \frac{15}{2}\\2 & 1 & 3 & 1\end{matrix}\right]
\underrightarrow{ R_3 + (- \frac{1}{2})R_1 }
\\
\left[\begin{matrix}4 & 3 & 5 & -2\\0 & - \frac{7}{4} & \frac{3}{4} & \frac{15}{2}\\0 & - \frac{1}{2} & \frac{1}{2} & 2\end{matrix}\right]
\underrightarrow{ R_{2} \leftrightarrow R_{2} }
\left[\begin{matrix}4 & 3 & 5 & -2\\0 & - \frac{7}{4} & \frac{3}{4} & \frac{15}{2}\\0 & - \frac{1}{2} & \frac{1}{2} & 2\end{matrix}\right]
\underrightarrow{ R_3 + (- \frac{2}{7})R_2 }
\\
\left[\begin{matrix}4 & 3 & 5 & -2\\0 & - \frac{7}{4} & \frac{3}{4} & \frac{15}{2}\\0 & 0 & \frac{2}{7} & - \frac{1}{7}\end{matrix}\right]
\underrightarrow{ R_{3} \leftrightarrow R_{3} }
\left[\begin{matrix}4 & 3 & 5 & -2\\0 & - \frac{7}{4} & \frac{3}{4} & \frac{15}{2}\\0 & 0 & \frac{2}{7} & - \frac{1}{7}\end{matrix}\right]
\underrightarrow{ \frac{R_3}{\frac{2}{7}} }
\left[\begin{matrix}4 & 3 & 5 & -2\\0 & - \frac{7}{4} & \frac{3}{4} & \frac{15}{2}\\0 & 0 & 1 & - \frac{1}{2}\end{matrix}\right]
\underrightarrow{ R_2 + (- \frac{3}{4})R_3 }
\left[\begin{matrix}4 & 3 & 5 & -2\\0 & - \frac{7}{4} & 0 & \frac{63}{8}\\0 & 0 & 1 & - \frac{1}{2}\end{matrix}\right]
\underrightarrow{ R_1 + (-5)R_3 }
\\
\left[\begin{matrix}4 & 3 & 0 & \frac{1}{2}\\0 & - \frac{7}{4} & 0 & \frac{63}{8}\\0 & 0 & 1 & - \frac{1}{2}\end{matrix}\right]
\underrightarrow{ \frac{R_2}{- \frac{7}{4}} }
\left[\begin{matrix}4 & 3 & 0 & \frac{1}{2}\\0 & 1 & 0 & - \frac{9}{2}\\0 & 0 & 1 & - \frac{1}{2}\end{matrix}\right]
\underrightarrow{ R_1 + (-3)R_2 }
\\
\left[\begin{matrix}4 & 0 & 0 & 14\\0 & 1 & 0 & - \frac{9}{2}\\0 & 0 & 1 & - \frac{1}{2}\end{matrix}\right]
\underrightarrow{ \frac{R_1}{4} }
\left[\begin{matrix}1 & 0 & 0 & \frac{7}{2}\\0 & 1 & 0 & - \frac{9}{2}\\0 & 0 & 1 & - \frac{1}{2}\end{matrix}\right]
$$

3. Escriba a $B$ como una combinación lineal del conjunto de vectores A.

a) $B = \begin{pmatrix} -1 \\ -2 \\ 4\end{pmatrix}, A = \{\begin{pmatrix}-2 \\ -1 \\ -5\end{pmatrix}, \begin{pmatrix}4 \\ -1 \\ -2\end{pmatrix}, \begin{pmatrix}3 \\ 1 \\ -3\end{pmatrix}\}$

$$
\left[\begin{matrix}-2 & 4 & 3 & -1\\-1 & -1 & 1 & -2\\-5 & -2 & -3 & 4\end{matrix}\right]
\underrightarrow{ R_{3} \leftrightarrow R_{1} }
\left[\begin{matrix}-5 & -2 & -3 & 4\\-1 & -1 & 1 & -2\\-2 & 4 & 3 & -1\end{matrix}\right]
\underrightarrow{ R_2 + (- \frac{1}{5})R_1 }
\left[\begin{matrix}-5 & -2 & -3 & 4\\0 & - \frac{3}{5} & \frac{8}{5} & - \frac{14}{5}\\-2 & 4 & 3 & -1\end{matrix}\right]
\underrightarrow{ R_3 + (- \frac{2}{5})R_1 }
\\
\left[\begin{matrix}-5 & -2 & -3 & 4\\0 & - \frac{3}{5} & \frac{8}{5} & - \frac{14}{5}\\0 & \frac{24}{5} & \frac{21}{5} & - \frac{13}{5}\end{matrix}\right]
\underrightarrow{ R_{3} \leftrightarrow R_{2} }
\left[\begin{matrix}-5 & -2 & -3 & 4\\0 & \frac{24}{5} & \frac{21}{5} & - \frac{13}{5}\\0 & - \frac{3}{5} & \frac{8}{5} & - \frac{14}{5}\end{matrix}\right]
\underrightarrow{ R_3 + (\frac{1}{8})R_2 }
\\
\left[\begin{matrix}-5 & -2 & -3 & 4\\0 & \frac{24}{5} & \frac{21}{5} & - \frac{13}{5}\\0 & 0 & \frac{17}{8} & - \frac{25}{8}\end{matrix}\right]
\underrightarrow{ R_{3} \leftrightarrow R_{3} }
\left[\begin{matrix}-5 & -2 & -3 & 4\\0 & \frac{24}{5} & \frac{21}{5} & - \frac{13}{5}\\0 & 0 & \frac{17}{8} & - \frac{25}{8}\end{matrix}\right]
\underrightarrow{ \frac{R_3}{\frac{17}{8}} }
\left[\begin{matrix}-5 & -2 & -3 & 4\\0 & \frac{24}{5} & \frac{21}{5} & - \frac{13}{5}\\0 & 0 & 1 & - \frac{25}{17}\end{matrix}\right]
\underrightarrow{ R_2 + (- \frac{21}{5})R_3 }
\left[\begin{matrix}-5 & -2 & -3 & 4\\0 & \frac{24}{5} & 0 & \frac{304}{85}\\0 & 0 & 1 & - \frac{25}{17}\end{matrix}\right]
\underrightarrow{ R_1 + (3)R_3 }
\\
\left[\begin{matrix}-5 & -2 & 0 & - \frac{7}{17}\\0 & \frac{24}{5} & 0 & \frac{304}{85}\\0 & 0 & 1 & - \frac{25}{17}\end{matrix}\right]
\underrightarrow{ \frac{R_2}{\frac{24}{5}} }
\left[\begin{matrix}-5 & -2 & 0 & - \frac{7}{17}\\0 & 1 & 0 & \frac{38}{51}\\0 & 0 & 1 & - \frac{25}{17}\end{matrix}\right]
\underrightarrow{ R_1 + (2)R_2 }
\\
\left[\begin{matrix}-5 & 0 & 0 & \frac{55}{51}\\0 & 1 & 0 & \frac{38}{51}\\0 & 0 & 1 & - \frac{25}{17}\end{matrix}\right]
\underrightarrow{ \frac{R_1}{-5} }
\left[\begin{matrix}1 & 0 & 0 & - \frac{11}{51}\\0 & 1 & 0 & \frac{38}{51}\\0 & 0 & 1 & - \frac{25}{17}\end{matrix}\right]
$$

b) $B = -x^2+2x, A = \{x^2-1, x^2+1, x^2-x-1, x^2+5x\}$:

$$
\begin{bmatrix} 1 & 1 &1 &1 & -1 \\ 0 & 0& -1 & 5 & 2 \\ -1 & 1 &-1 & -1 & 0 \end{bmatrix} \underrightarrow{R_3 \rightarrow R_1 + R_3} \begin{bmatrix}1 & 1&1&1&-1\\0&0&-1&5&2\\0&2&0&0&-1\end{bmatrix} \underrightarrow{R_2 \leftrightarrow R_3}  \\ \begin{bmatrix}1&0&1&1&-\frac{1}{2} \\ 0 & 1&0&0&-\frac{1}{2} \\ 0 & 0&-1&5&2\end{bmatrix} \underrightarrow{-R_3} \begin{bmatrix}1&0&1&1&-\frac{1}{2}\\0&1&0&0&-\frac{1}{2}\\0&0&1&5&-2\end{bmatrix} \rightarrow{R_1 \rightarrow -R_3 + R_1} \\ \begin{bmatrix}1&0&0&6&\frac{3}{2} \\ 0&1&0&0&-\frac{1}{2}\\0&0&1&5&-2\end{bmatrix} \therefore c_1 =  \frac{3}{2}, c_2 = -\frac{1}{2}, c_3 = -2, c_4 = 0
$$

### Vectores Linealmente Independientes y Dependientes

1. Determine los valores de $k$ para que el conjunto $H = \{\begin{pmatrix}k \\ -2 \\3 \end{pmatrix}, \begin{pmatrix}2 \\ -2k \\ -1\end{pmatrix}, \begin{pmatrix}k \\ 0 \\3\end{pmatrix}\}$ sea lineal-mente independiente.

$$
A = \begin{bmatrix}k&2&k\\-2&-2k&0\\3&-1&3\end{bmatrix}
$$

$$
|A| \rightarrow -6k^2+2k-(-6k^2-12) \rightarrow6k^2+2k+6k^2-12\rightarrow 2k+12 \therefore K = -6
$$

2. Sea $V$ el espacio vectorial de todas las funciones con valore real definidas sobre la recta real completa. ¿Cuáles de los siguientes conjuntos de vectores en $V$ son lineal-mente dependientes?

a) $\{2,4\sin^2{x},\cos^2{x}\}$ Nos da un sistema incosistente, por lo tanto es linealmente dependiente.

b) $\{x, \cos{x}\}$

$$
\begin{bmatrix}x & \cos{x} & 0  \\ 1 & -\sin{x} & 0\end{bmatrix} \underrightarrow{R_1 \leftrightarrow R_2} \begin{bmatrix}1 & -\sin{x} & 0 \\ x & \cos{x} & 0\end{bmatrix} \underrightarrow{-xR_1 + R_2} \begin{bmatrix}1&\sin{x}&0 \\ 0 & \cos{x} +x\sin{x}&0\end{bmatrix}\ \underrightarrow{\frac{1}{\cos{x} + x\sin{x}}}R_2 \\ \begin{bmatrix}1 & -\sin{x} & 0\\ 0&1&0\end{bmatrix} \underrightarrow{\sin{x}R_2 + R_1} \begin{bmatrix}1&0&0\\0&1&0\end{bmatrix} \therefore C_1 = C_2 = 0 \therefore \text{ Solución consistente, por lo tanto es linealmente independiente.}
$$

c) $\{1,\sin{x},\sin{2x}\}$

$$
\begin{bmatrix}0\\0\\0\end{bmatrix} \rightarrow \begin{bmatrix}1\\\sin{x}\\\sin{2x}\end{bmatrix} \therefore \begin{bmatrix}1&\sin{x}&\sin{2x} &0\\ 0 & \cos{x} & 2\cos{2x} & 0 \\ 0 & -\sin{x} & -4\sin{2x}&0\end{bmatrix} \underrightarrow{\frac{1}{\cos{x}}R_2} \begin{bmatrix}1 & \sin{x} & \sin{2x} & 0 \\ 0&1&2\frac{\cos{2x}}{\cos{x}}&0\\0&-\sin{x}&-4\sin{2x}\end{bmatrix} \underrightarrow{-\sin{x}R_2 + R_1 \\ \sin{x}R-2 + R_3} \\ \dots \\ \begin{bmatrix}1&0&0&0\\0&1&0&0\\0&0&1&0\end{bmatrix} \therefore \text{Solución consistente donde } c_1 = c_2 = c_3 = 0 \text{ Por lo tanto es linealmente independiente}
$$

d) $\{\cos{2x}, \sin^2{x}, \cos^2{x}\}$ El sistema es linealmente independiente por ser un sistema consistente con soluciones infinitas.

3. Para que los valores de $k$, las siguientes matrices son linealmente independientes de $M_
  {22}$ $\begin{bmatrix}1 & 0\\ 1 & k\end{bmatrix}, \begin{bmatrix}-1 & 0 \\ k & 1\end{bmatrix}, \begin{bmatrix}2 & 0 \\ 1 & 3\end{bmatrix}$

$$
\begin{bmatrix}1&-1&2&a\\0&0&0&b\\1&k&1&c\\k&0&3&d\end{bmatrix} \therefore \text{}
$$

4. Construya un conjunto de vectores $H = \{v_1, v_2, v_3\} \in R^3$ tal que sean linealmente independientes y $v_1^TV_2 = v_2^Tv_3 = 0$.

$$
V_1 = \begin{bmatrix}1\\0\\0\end{bmatrix} , V_2 = \begin{bmatrix}0\\1\\0\end{bmatrix}, V_3 = \begin{bmatrix}0\\0\\1\end{bmatrix}
$$

$$
A = \begin{bmatrix}1&0&0\\0&1&0\\0&0&1\end{bmatrix} \therefore |A| = 0
$$

$$
V_1^T V_2 = \begin{bmatrix}1&0&0\end{bmatrix} \begin{bmatrix}0\\1\\0\end{bmatrix} = 0 \\ V_2^TV_3 = \begin{bmatrix}0&1&0\end{bmatrix} \begin{bmatrix}0\\0\\1\end{bmatrix} = 0 \\ \therefore \\ V_1^TV_2 = V_2^TV_1 = 0
$$

5. Sea $H = \{v_1, v_2, v_3\} \in R^3$. Demuestre que si $det(H) = det( [v_1, v_2, v_3] ) = 0$, entonces $H$ es lineal-mente independiente.

### Bases y Cambios de Base

1. Determine una base para el espacio de funciones que satisface: $\frac{dy}{dx}-2y=0$.

2. Considera las bases $B = \{u_1,u_2\}$ y $B' = \{u'_1,u'_2\}$ para R^2, donde: $u_1 = \begin{pmatrix}2\\2\end{pmatrix}, u_2 = \begin{pmatrix}4\\-1\end{pmatrix}, u'_1 = \begin{pmatrix}1\\3\end{pmatrix}, u'_2 = \begin{pmatrix}-1\\-1\end{pmatrix}$

a) Calcula la matriz de transición de $B'$ hacia $B$.

$$
\left[\begin{matrix}2 & 4 & 1 & -1\\2 & -1 & 3 & -1\end{matrix}\right]
\underrightarrow{ R_{1} \leftrightarrow R_{1} }
\left[\begin{matrix}2 & 4 & 1 & -1\\2 & -1 & 3 & -1\end{matrix}\right]
\underrightarrow{ R_2 + (-1)R_1 }
\left[\begin{matrix}2 & 4 & 1 & -1\\0 & -5 & 2 & 0\end{matrix}\right]
\underrightarrow{ R_{2} \leftrightarrow R_{2} }
\left[\begin{matrix}2 & 4 & 1 & -1\\0 & -5 & 2 & 0\end{matrix}\right]
\underrightarrow{ \frac{R_2}{-5} }
\left[\begin{matrix}2 & 4 & 1 & -1\\0 & 1 & - \frac{2}{5} & 0\end{matrix}\right]
\underrightarrow{ R_1 + (-4)R_2 }
\\
\left[\begin{matrix}2 & 0 & \frac{13}{5} & -1\\0 & 1 & - \frac{2}{5} & 0\end{matrix}\right]
\underrightarrow{ \frac{R_1}{2} }
\left[\begin{matrix}1 & 0 & \frac{13}{10} & - \frac{1}{2}\\0 & 1 & - \frac{2}{5} & 0\end{matrix}\right]
$$

b) Calcula la matriz de transición de $B$ hacia $B'$.

$$
\left[\begin{matrix}1 & -1 & 2 & 4\\3 & -1 & 2 & -1\end{matrix}\right]
\underrightarrow{ R_{2} \leftrightarrow R_{1} }
\left[\begin{matrix}3 & -1 & 2 & -1\\1 & -1 & 2 & 4\end{matrix}\right]
\underrightarrow{ R_2 + (- \frac{1}{3})R_1 }
\left[\begin{matrix}3 & -1 & 2 & -1\\0 & - \frac{2}{3} & \frac{4}{3} & \frac{13}{3}\end{matrix}\right]
\underrightarrow{ R_{2} \leftrightarrow R_{2} }
\left[\begin{matrix}3 & -1 & 2 & -1\\0 & - \frac{2}{3} & \frac{4}{3} & \frac{13}{3}\end{matrix}\right]
\underrightarrow{ \frac{R_2}{- \frac{2}{3}} }
\left[\begin{matrix}3 & -1 & 2 & -1\\0 & 1 & -2 & - \frac{13}{2}\end{matrix}\right]
\underrightarrow{ R_1 + (1)R_2 }
\\
\left[\begin{matrix}3 & 0 & 0 & - \frac{15}{2}\\0 & 1 & -2 & - \frac{13}{2}\end{matrix}\right]
\underrightarrow{ \frac{R_1}{3} }
\left[\begin{matrix}1 & 0 & 0 & - \frac{5}{2}\\0 & 1 & -2 & - \frac{13}{2}\end{matrix}\right]
$$

c) Dado el vector $w = \begin{pmatrix}3\\-5\end{pmatrix}$, calcula $[w]_B$ y $[w]_{B'}$.

$$
[W]_B =
\left[\begin{matrix}2 & 4 & 3\\2 & -1 & -5\end{matrix}\right]
\underrightarrow{ R_{1} \leftrightarrow R_{1} }
\left[\begin{matrix}2 & 4 & 3\\2 & -1 & -5\end{matrix}\right]
\underrightarrow{ R_2 + (-1)R_1 }
\left[\begin{matrix}2 & 4 & 3\\0 & -5 & -8\end{matrix}\right]
\underrightarrow{ R_{2} \leftrightarrow R_{2} }
\left[\begin{matrix}2 & 4 & 3\\0 & -5 & -8\end{matrix}\right]
\underrightarrow{ \frac{R_2}{-5} }
\left[\begin{matrix}2 & 4 & 3\\0 & 1 & \frac{8}{5}\end{matrix}\right]
\underrightarrow{ R_1 + (-4)R_2 }
\\
\left[\begin{matrix}2 & 0 & - \frac{17}{5}\\0 & 1 & \frac{8}{5}\end{matrix}\right]
\underrightarrow{ \frac{R_1}{2} }
\left[\begin{matrix}1 & 0 & - \frac{17}{10}\\0 & 1 & \frac{8}{5}\end{matrix}\right]
$$

$$
[W]_{B'} = \left[\begin{matrix}1 & -1 & 3\\3 & -1 & -5\end{matrix}\right]
\underrightarrow{ R_{2} \leftrightarrow R_{1} }
\left[\begin{matrix}3 & -1 & -5\\1 & -1 & 3\end{matrix}\right]
\underrightarrow{ R_2 + (- \frac{1}{3})R_1 }
\left[\begin{matrix}3 & -1 & -5\\0 & - \frac{2}{3} & \frac{14}{3}\end{matrix}\right]
\underrightarrow{ R_{2} \leftrightarrow R_{2} }
\left[\begin{matrix}3 & -1 & -5\\0 & - \frac{2}{3} & \frac{14}{3}\end{matrix}\right]
\underrightarrow{ \frac{R_2}{- \frac{2}{3}} }
\left[\begin{matrix}3 & -1 & -5\\0 & 1 & -7\end{matrix}\right]
\underrightarrow{ R_1 + (1)R_2 }
\\
\left[\begin{matrix}3 & 0 & -12\\0 & 1 & -7\end{matrix}\right]
\underrightarrow{ \frac{R_1}{3} }
\left[\begin{matrix}1 & 0 & -4\\0 & 1 & -7\end{matrix}\right]
$$

3. Sean los polinomios $p_1 = x^2 + x - 2$, $p_2 = 3x^2-x$, realiza los siguientes ejercicios:

a) $p_3 = 2p_1 - p_2$

$$
2x^2 + 2x - 4 - 3x^2 - x = -x^2+3x-4
$$

b) El conjunto $\{p_1,p_2,p_3\}$, ¿forman una base? Justifica.

$$
A = \begin{bmatrix}1 & 1 & -2 \\ 3&-1&0\\-1&3&-4\end{bmatrix} \therefore |A| = 0 \therefore \text{ No es base y es linealmente dependiente}
$$

4. Dado el siguiente sistema de ecuaciones lineales homogéneo: $$\begin{align*}-x+3y+z = 0 \\ 2x+2y-z=0\\3x-y-2z=0\end{align*}$$ Determina la base(si es que existe) del conjunto solución del problema.

$$
\begin{bmatrix}-1&3&1&0\\2&2&-1&0\\3&-1&-2&0\end{bmatrix} \underrightarrow{-R1}\begin{bmatrix}1&-3&1&0\\2&2&-1&0\\3&-1&-2&0\end{bmatrix} \underrightarrow{-2R_1 + R_2 \\ -3R_1 + R_3} \\ \begin{bmatrix}1&-3&-1&0\\0&8&1&0\\0&8&1&0\end{bmatrix} \underrightarrow{\frac{1}{8}R_2}\begin{bmatrix}1&-3&-1&0\\0&1&\frac{1}{8}&0\\0&8&1&0\end{bmatrix}\underrightarrow{3R_2 + R_1 \\ -8R_2 +R_3} \\\begin{bmatrix}1 &0&-\frac{5}{6}&0\\0&1&\frac{1}{8}&0\\0&0&0&0\end{bmatrix} \therefore x = \frac{5}{8}z, y = -\frac{1}{8}z, z\in R
$$

$$
z\begin{bmatrix}\frac{5}{8} \\ -\frac{5}{8} \\1\end{bmatrix} = S \\ dim(S) =1
$$

5. Dados los vectores y bases siguientes: $$V = \begin{pmatrix}-1\\3\end{pmatrix}, Z = \left\{ \begin{bmatrix}-1\\-3\end{bmatrix}, \begin{bmatrix}1\\0\end{bmatrix} \right\}, W = \left\{ \begin{bmatrix}1\\-1\end{bmatrix}, \begin{bmatrix}0\\1\end{bmatrix} \right\}$$

a) Calcula $[V]_W$.

$$
\left[\begin{matrix}1 & 0 & -1\\-1 & 1 & 3\end{matrix}\right]
\underrightarrow{ R_{1} \leftrightarrow R_{1} }
\left[\begin{matrix}1 & 0 & -1\\-1 & 1 & 3\end{matrix}\right]
\underrightarrow{ R_2 + (1)R_1 }
\left[\begin{matrix}1 & 0 & -1\\0 & 1 & 2\end{matrix}\right]
\underrightarrow{ R_{2} \leftrightarrow R_{2} }
\left[\begin{matrix}1 & 0 & -1\\0 & 1 & 2\end{matrix}\right]
\underrightarrow{ \frac{R_2}{1} }
\left[\begin{matrix}1 & 0 & -1\\0 & 1 & 2\end{matrix}\right]
\underrightarrow{ R_1 + (0)R_2 }
\\
\left[\begin{matrix}1 & 0 & -1\\0 & 1 & 2\end{matrix}\right]
\underrightarrow{ \frac{R_1}{1} }
\left[\begin{matrix}1 & 0 & -1\\0 & 1 & 2\end{matrix}\right]
$$

b) Calcula la matriz de transición de $W$ hacia $Z$.

$$
\left[\begin{matrix}-1 & 1 & 1 & 0\\-3 & 0 & -1 & 1\end{matrix}\right]
\underrightarrow{ R_{2} \leftrightarrow R_{1} }
\left[\begin{matrix}-3 & 0 & -1 & 1\\-1 & 1 & 1 & 0\end{matrix}\right]
\underrightarrow{ R_2 + (- \frac{1}{3})R_1 }
\left[\begin{matrix}-3 & 0 & -1 & 1\\0 & 1 & \frac{4}{3} & - \frac{1}{3}\end{matrix}\right]
\underrightarrow{ R_{2} \leftrightarrow R_{2} }
\left[\begin{matrix}-3 & 0 & -1 & 1\\0 & 1 & \frac{4}{3} & - \frac{1}{3}\end{matrix}\right]
\underrightarrow{ \frac{R_2}{1} }
\left[\begin{matrix}-3 & 0 & -1 & 1\\0 & 1 & \frac{4}{3} & - \frac{1}{3}\end{matrix}\right]
\underrightarrow{ R_1 + (0)R_2 }
\\
\left[\begin{matrix}-3 & 0 & -1 & 1\\0 & 1 & \frac{4}{3} & - \frac{1}{3}\end{matrix}\right]
\underrightarrow{ \frac{R_1}{-3} }
\left[\begin{matrix}1 & 0 & \frac{1}{3} & - \frac{1}{3}\\0 & 1 & \frac{4}{3} & - \frac{1}{3}\end{matrix}\right]
$$

c) Calcula $[V]_Z$ utilizando la matriz de transición del inciso anterior.

$$
\left[\begin{matrix}\frac{1}{3} & - \frac{1}{3}\\\frac{4}{3} & - \frac{1}{3}\end{matrix}\right] \left[\begin{matrix}-1 \\ 3\end{matrix}\right] = \left[\begin{matrix}-\frac{2}{3} \\ \frac{1}{3}\end{matrix}\right]
$$

6. Dado el siguiente conjunto de vectores: $(\frac{1}{2},-7,0), (-\frac{1}{3},0,2),(0,-7,\frac{1}{5})$.

a) Determine si el conjunto genera a $R^3$.

$$
  \begin{bmatrix}\frac{1}{3} & -\frac{1}{3} & 0 & a\\ -7 & 0&-7&b\\0&2&\frac{1}{5}&c\end{bmatrix} \underrightarrow{2R_1} \begin{bmatrix}1 & -\frac{2}{3} & 0 & 2a \\ -7 &0&-7&b\\0&2&\frac{1}{5}&c\end{bmatrix} \underrightarrow{7R1 + R_2} \\\begin{bmatrix}1&-\frac{2}{3} & 0&2a\\0&-\frac{14}{3}&-7&14a+b\\0&2&\frac{1}{5}&c\end{bmatrix} \underrightarrow{-\frac{3}{14}R_2} \begin{bmatrix}1&-\frac{2}{3}&0&2a\\0&1&\frac{2}{3}&-3a-\frac{3}{14}b\\0&2&\frac{1}{5}&c\end{bmatrix} \underrightarrow{\frac{2}{3}R_2 + R1 \\-2R_2 + R_3}\\\begin{bmatrix}1&0&1&-2a-\frac{1}{7}b\\0&1&\frac{3}{2}&-3a-\frac{3}{14}b\\0&0&-\frac{14}{5}&6a+\frac{3}{7}b-2c\end{bmatrix} \underrightarrow{-\frac{5}{14}R_3} \begin{bmatrix}1&0&1&-2a-\frac{1}{7}b\\0&1&\frac{3}{2}&-3a-\frac{3}{4}bb\\0&0&1&6a+\frac{3}{7}b-c\end{bmatrix} \underrightarrow{-R_3 + R_1 \\ - \frac{3}{2}R_3 + R_2} \begin{bmatrix}1&0&0&8a-\frac{4}{7}b +2c\\0&1&0&12a-\frac{6}{7}b+3c\\0&0&1&6s+\frac{3}{7}b-2c\end{bmatrix} \\ \therefore \text{Si es consistente, genera } R^3
$$

b) Genere un espacio vectorial de 3 elementos usando el conjunto de vectores.
c) Con los vectores, construya un sistema de ecuaciones lineales homogéneo y determine la base de las soluciones del sistema.

$$
\begin{bmatrix}0\\0\\0\end{bmatrix} = C_1\begin{bmatrix}\frac{1}{2} \\ -7 \\ 0\end{bmatrix} + C_2\begin{bmatrix}-\frac{1}{3}\\0\\2\end{bmatrix} + C_3\begin{bmatrix}0\\-7\\\frac{1}{5}\end{bmatrix}
$$

$$
\left[\begin{matrix}0.5 & -0.333333333333333 & 0 & 0\\-7.0 & 0 & -7.0 & 0\\0 & 2.0 & 0.2 & 0\end{matrix}\right]
\underrightarrow{ R_{2} \leftrightarrow R_{1} }
\left[\begin{matrix}-7.0 & 0 & -7.0 & 0\\0.5 & -0.333333333333333 & 0 & 0\\0 & 2.0 & 0.2 & 0\end{matrix}\right]
\underrightarrow{ R_2 + (0.0714285714285714)R_1 }
\left[\begin{matrix}-7.0 & 0 & -7.0 & 0\\0 & -0.333333333333333 & -0.5 & 0\\0 & 2.0 & 0.2 & 0\end{matrix}\right]
\underrightarrow{ R_3 + (0)R_1 }
\\
\left[\begin{matrix}-7.0 & 0 & -7.0 & 0\\0 & -0.333333333333333 & -0.5 & 0\\0 & 2.0 & 0.2 & 0\end{matrix}\right]
\underrightarrow{ R_{3} \leftrightarrow R_{2} }
\left[\begin{matrix}-7.0 & 0 & -7.0 & 0\\0 & 2.0 & 0.2 & 0\\0 & -0.333333333333333 & -0.5 & 0\end{matrix}\right]
\underrightarrow{ R_3 + (0.166666666666667)R_2 }
\\
\left[\begin{matrix}-7.0 & 0 & -7.0 & 0\\0 & 2.0 & 0.2 & 0\\0 & 0 & -0.466666666666667 & 0\end{matrix}\right]
\underrightarrow{ R_{3} \leftrightarrow R_{3} }
\left[\begin{matrix}-7.0 & 0 & -7.0 & 0\\0 & 2.0 & 0.2 & 0\\0 & 0 & -0.466666666666667 & 0\end{matrix}\right]
\underrightarrow{ \frac{R_3}{-0.466666666666667} }
\left[\begin{matrix}-7.0 & 0 & -7.0 & 0\\0 & 2.0 & 0.2 & 0\\0 & 0 & 1.0 & 0\end{matrix}\right]
\underrightarrow{ R_2 + (-0.2)R_3 }
\left[\begin{matrix}-7.0 & 0 & -7.0 & 0\\0 & 2.0 & 0 & 0\\0 & 0 & 1.0 & 0\end{matrix}\right]
\underrightarrow{ R_1 + (7.0)R_3 }
\\
\left[\begin{matrix}-7.0 & 0 & 0 & 0\\0 & 2.0 & 0 & 0\\0 & 0 & 1.0 & 0\end{matrix}\right]
\underrightarrow{ \frac{R_2}{2.0} }
\left[\begin{matrix}-7.0 & 0 & 0 & 0\\0 & 1.0 & 0 & 0\\0 & 0 & 1.0 & 0\end{matrix}\right]
\underrightarrow{ R_1 + (0)R_2 }
\\
\left[\begin{matrix}-7.0 & 0 & 0 & 0\\0 & 1.0 & 0 & 0\\0 & 0 & 1.0 & 0\end{matrix}\right]
\underrightarrow{ \frac{R_1}{-7.0} }
\left[\begin{matrix}1.0 & 0 & 0 & 0\\0 & 1.0 & 0 & 0\\0 & 0 & 1.0 & 0\end{matrix}\right]
$$

$$
 \therefore \\
 C_1 = C_2 = C_3 = 0
$$

Sistema consistente, que genera a $R^3$

7. Sea $V = \begin{pmatrix}-1\\5\end{pmatrix}$ y $[V]_W = \begin{pmatrix}-2\\7\end{pmatrix}$ determine la base $W$, sabiendo que $W = \left\{ \begin{pmatrix}x\\2y\end{pmatrix}, \begin{pmatrix}-y\\-3x\end{pmatrix} \right\}$

8. Sea $[V]_S = \begin{pmatrix}-\frac{1}{2}\\2\end{pmatrix}$ y $[V]_W = \begin{pmatrix}-3\\7\end{pmatrix}$, sabiendo que $W = \left\{ \begin{pmatrix}3\\y\end{pmatrix}, \begin{pmatrix}x\\5\end{pmatrix} \right\}$ y $S = \left\{ \begin{pmatrix}1\\0\end{pmatrix}, \begin{pmatrix}0\\1\end{pmatrix} \right\}$, determine:
   a) $W$
   b) Matriz de transición de la base $S$ hacia $W$
   c) Matriz de transición de la base $W$ hacia $S$.

9. Calcular las coordenadas de $V = \begin{pmatrix} -2 \\ 3 \\ 3 \end{pmatrix}$ en términos de base $H = \left\{ \begin{pmatrix} 1 \\ -2 \\3 \end{pmatrix}, \begin{pmatrix}2 \\ -2 \\ -1 \end{pmatrix}, \begin{pmatrix}1\\1\\4\end{pmatrix} \right\}$. Calcule $||V||$ y $||V_H||$. ¿Porué $||V|| \ne ||V_H||$?

### Rango y Nulidad de una matriz

1. Determine el valor de $k$ para que la matriz $M$ tenga $V=2$

$$
M = \begin{bmatrix}1&-1&1&4\\3&-1&3k&1\\5&-5&7&9\end{bmatrix} \therefore |M| \rightarrow k = \frac{5}{3}
$$

$$
M = \begin{bmatrix}1&-2&1&4\\3&-1&5&1\\5&-5&7&9\end{bmatrix} \underrightarrow{2R_2 + R_1 \\ -5R_2 + R_3} \begin{bmatrix}1&0&\frac{9}{5}&-\frac{2}{5}\\0&1&\frac{2}{5} & -\frac{11}{5} \\ 0&0&0&0\end{bmatrix} \\ \therefore \\ x = -\frac{9}{5}z + \frac{2}{5}w \\ y = -\frac{2}{5}z + \frac{11}{5}w \\ z \in R \\ w \in R \\ \therefore \\ z\begin{bmatrix}-\frac{9}{5} \\ -\frac{2}{5}\\1\\0\end{bmatrix}, w = \begin{bmatrix}\frac{2}{5}\\\frac{4}{5}\\0\\1\end{bmatrix} : V = 2
$$

2.  Encuentre todos los valores posibles del rango de la matriz $A$ y $P(A)$, si $k$ es una variable.

$$
A = \begin{bmatrix}1&2&k\\-2&4k&2\\k&-2&1\end{bmatrix}, |A| \rightarrow k = \begin{cases}-1\\2\end{cases}
$$

K = -1

$$
\begin{bmatrix}1&2&-1\\-2&-4&2\\-1&-2&1\end{bmatrix} \underrightarrow{2R_1 + R-2 \\ R_1 + R_2} \begin{bmatrix}1&2&-1\\0&0&0\\0&0&0\end{bmatrix} \\ \therefore \\ x = -2y + z \\ y \in R \\ z \in R\\ \therefore \\ \begin{bmatrix}x\\y\\z\end{bmatrix} = \begin{bmatrix}-2y+z\\y\\z\end{bmatrix} \therefore y\begin{bmatrix}-2\\1\\0\end{bmatrix}, z\begin{bmatrix}1\\0\\1\end{bmatrix}\\V(A)= 2, P(A) = 1
$$

K = 2

$$
\begin{bmatrix}1&2&2\\-2&8&2\\2&-2&1\end{bmatrix} \underrightarrow{2R_1 + R_2 \\ -2R_1 + R_3} \begin{bmatrix}1&2&2\\0&12&8\\0&-6&-3\end{bmatrix} \underrightarrow{ \frac{1}{12}R_2 } \\ \begin{bmatrix}1&2&2\\0&1&\frac{2}{3}\\0&-6&-3\end{bmatrix} \underrightarrow{ -2R_2 + R_1 \\ 6R_2+R_3 } \begin{bmatrix}1&0&\frac{2}{3}\\0&0&\frac{2}{3}\\0&0&1\end{bmatrix} \underrightarrow{-\frac{2}{3}R_3 + R_1 \\ - \frac{2}{3}R_3 + R_2} \\ \begin{bmatrix}1&0&1\\0&1&\frac{1}{2}\\0&0&1\end{bmatrix} \\ \therefore \\ x = 2 \\ y = -\frac{1}{2}z \\ z = 0 \\ \therefore \\ \begin{bmatrix}x\\y\\z\end{bmatrix} = \begin{bmatrix}-2\\-\frac{1}{2}z \\0\end{bmatrix} = z\begin{bmatrix}-1\\-\frac{1}{2}\\0\end{bmatrix}
$$
