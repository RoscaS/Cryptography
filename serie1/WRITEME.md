# Algèbre modulaire

## Introduction
* $3+4+5\equiv 1 \quad (mod\;11)$
* $3+4+5\equiv 0 \quad (mod\;12)$
* $6\cdot 7\equiv 9 \quad (mod\;11)$
* $6\cdot 7\equiv 6 \quad (mod\;12)$
* $6^{10}\equiv 1 \quad (mod\;11)$
* $6^{10}= 6^{2}\cdot6^{8}\equiv 0 \quad (mod\;12)$
* $6^{11}= 6^{2}\cdot6^{9}\equiv 0 \quad (mod\;12)$
* $3-7\equiv  7\quad (mod\;11)$
* $2-7-9\equiv 10 \quad (mod\;12)$
* $6(-9)\equiv 1 \quad (mod\;11)$
* $7(-3)\equiv 3 \quad (mod\;12)$
  
## Petit théorème de Fermat
* $6^{1010}=(6^{10})^{101}=1 \quad (mod\;11)$
* $n^{p\cdot10}=(n^{10})^{p} = 1 \quad (mod\;11)$
* $\quad " \quad \quad " \quad \quad "$ 
* $\quad " \quad \quad " \quad \quad "$ 
* $\quad " \quad \quad " \quad \quad "$ 
* $\quad " \quad \quad " \quad \quad "$ 
* $6^{1011}=6^{1011}\cdot6=6 \quad (mod\;11)$
* $6^{3024}=6^{1010\cdot3+4}=6^{1010}\cdot6^2\cdot6^2\equiv 9 \quad(mod\;11)$

## Modulo inverse
* $3^{-1}=4 \quad\quad(mod\;11) \quad = \emptyset \quad (mod\;12) \quad gcd(3,12) \neq 1$
* $5^{-1}=9 \quad\quad(mod\;11) \quad = 5 \quad (mod\;12)$
* $7^{-1}=8 \quad\quad(mod\;11) \quad = 7 \quad (mod\;12)$
* $2^{-1}=6 \quad\quad(mod\;11) \quad = \emptyset \quad (mod\;12) \quad gcd(2,12) \neq 1$
* $6^{-1}=2 \quad\quad(mod\;11) \quad = \emptyset \quad (mod\;12) \quad gcd(6,12) \neq 1$
* $10^{-1}=10 \quad(mod\;11) \quad = \emptyset \quad (mod\;12) \quad gcd(10,12) \neq 1$


## Divisions discrètes
* $4\cdot3^{-1}=4\cdot4=5 \quad(mod\;11)$
* $2\cdot3^{-1}=2\cdot4=8 \quad(mod\;11)$
* $10\cdot7^{-1}=10\cdot8=3 \quad(mod\;11)$
* $7\cdot2^{-1}=7\cdot6=9 \quad(mod\;11)$
* $3\cdot9^{-1}=3\cdot5=4 \quad(mod\;11)$
* $7\cdot10^{-1}=7\cdot10=4 \quad(mod\;11)$
* $7\cdot8^{-1}=7\cdot7=5 \quad(mod\;11)$
* $4\cdot3^{-1}=\emptyset\quad(mod\;12)$
* $2\cdot5^{-1}=2\cdot5=10 \quad(mod\;12)$
* $8\cdot7^{-1}=8\cdot7=8 \quad(mod\;12)$
* $9\cdot2^{-1}=\emptyset\quad(mod\;12)$
* $9\cdot10^{-1}=\emptyset\quad(mod\;12)$
* $7\cdot8^{-1}=\emptyset\quad(mod\;12)$
* $5\cdot9^{-1}=\emptyset\quad(mod\;12)$


## Racines carrées discrètes
* $\sqrt{5}=4;7 \quad(mod\;11)$
* $\sqrt{3}=5;6 \quad(mod\;11)$
* $\sqrt{9}=8;3 \quad(mod\;11)$
* $\sqrt{4}=9;2 \quad(mod\;11)$
* $\sqrt{1}=10;1 \quad(mod\;11)$
* $\sqrt{6}= \emptyset \quad(mod\;11)$ 

## Logarithmes discrets
* $log_{2}(3)=8\quad(mod\;11) \quad\quad 2^{8}=3\quad(mod\;11)$
* $log_{2}(4)=2\quad(mod\;11) \quad\quad 2^{2}=4\quad(mod\;11)$
* $log_{2}(5)=4\quad(mod\;11) \quad\quad 2^{4}=5\quad(mod\;11)$
* $log_{2}(6)=9\quad(mod\;11) \quad\quad 2^{9}=6\quad(mod\;11)$
* $log_{2}(7)=7\quad(mod\;11) \quad\quad 2^{7}=7\quad(mod\;11)$
* $log_{2}(9)=6\quad(mod\;11) \quad\quad 2^{6}=9\quad(mod\;11)$
* $log_{2}(10)=5\quad(mod\;11) \quad\quad 2^{5}=10\quad(mod\;11)$
* $log_{5}(3)=2 \quad(mod\;11) \quad\quad 5^{2}=3\quad(mod\;11)$
* $log_{5}(4)=3 \quad(mod\;11) \quad\quad 5^{3}=4\quad(mod\;11)$
* $log_{5}(9)=4 \quad(mod\;11) \quad\quad 5^{4}=9\quad(mod\;11)$
* $log_{5}(5)=6 \quad(mod\;11) \quad\quad 5^{6}=5\quad(mod\;11)$
* $log_{2}(8)=3 \quad(mod\;11) \quad\quad 5^{3}=8\quad(mod\;11)$


## Exercise 7

Write a program (choose your language) that computes:

$z^{b^k} \; mod\;n$

```python
lambda z, b, k, n: pow(z, b**k, n)
```
