infix to prefix:
Example :  a+b/c-(d*e)+f
Reverse :  f+(e*d)-c/b+a

Step       Data       Stack             Output
1          f                            f
2          +          +                 f
3          (          +(                f
4          e          +(                fe
5          *          +(*               fe
6          d          +(*               fed
7          )          +                 fed*
8          -          -                 fed*+
9          c          -                 fed*+c
10         /          -/                fed*+c
11         b          -/                fed*+cb
12         +          +                 fed*+cb/-
13         a          +                 fed*+cb/-a
14                                      fed*+cb/-a+
                        final ans : +a-/bc+*def
