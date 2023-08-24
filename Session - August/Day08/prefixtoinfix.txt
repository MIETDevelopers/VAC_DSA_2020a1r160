Prefix Expression:  +a-/bc+*def

Reverse : fed*+cb/-a+

Step   Data          Stack         Output
1      f             f
2      e             f e
3      d             f e(B) d(A)
4      *             f d*e         d*e
5      +             f+(d*e)       f+(d*e)
6      c             f+(d*e) c
7      b             f+(d*e) c b
8      /             f+(d*e) (b/c)  (b/c)
9      -             (b/c)-(f+(d*e))  ((b/c)-f+(d*e))
10     a             (b/c)-(f+(d*e)) a
11     +             a+(b/c)-(f+(d*e))