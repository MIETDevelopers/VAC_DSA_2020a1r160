infix: a+b/c-d+(e*f-g)+h
postfix:
    
step    Data     Stack        Output
1       a                     a
2       +        +            a
3       b        +            ab
4       /        +/           ab
5       c        +/           abc
6       -        -            abc/+
7       d        -            abc/+d
8       +        +            abc/+d-
9       (        +(           abc/+d-
10      e        +(           abc/+d-e
11      *        +(*          abc/+d-e
12      f        +(*          abc/+d-ef
13      -        +(*-         abc/+d-ef
14      g        +(*-         abc/+d-efg
15      )        +            abc/+d-efg-*
16      +        +            abc/+d-efg-*+
17      h        +            abc/+d-efg-*+h
18                            abc/+d-efg-*+h+
                   
                   
                   
                   
Infix: a/b-c*d+e/f+(g/h/i*j)+k
Postfix output: ab/cd*-ef/+ghij*//+k+

Infix: a+b*c-d/e/f/g-h-i*(j+k)-m
Prefix Output: +a-*bc-/d/e/f-h-*i+jkm
                   
                   
                   
                   
                   
                   
                   