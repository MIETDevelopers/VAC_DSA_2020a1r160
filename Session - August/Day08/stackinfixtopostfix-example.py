()[]{}
^ - r to l
/ * - l to r
+ - - l to r















k+l-m*n+(o^p)*w/u/v*t+q

step      data        stack                 postfix exp storage
1         k                                  k
2         +           +                      k
3         l           +                      kl
4         -           -                      kl+
5         m           -                      kl+m
6         *           -*                     kl+m
7         n           -*                     kl+mn
8         +           +                      kl+mn*-
9         (           +(                     kl+mn*-
10        o           +(                     kl+mn*-o
11        ^           +(^                    kl+mn*-o
12        p           +(^                    kl+mn*-op
13        )           +                      kl+mn*-op^
14        *           +*                     kl+mn*-op^
15        w           +*                     kl+mn*-op^w
16        /           +/                     kl+mn*-op^w*
17        u           +/                     kl+mn*-op^w*u
18        /           +/                     kl+mn*-op^w*u/
19        v           +/                     kl+mn*-op^w*u/v
20        *           +*                     kl+mn*-op^w*u/v/                       
21        t           +*                     kl+mn*-op^w*u/v/t
22        +           +                      kl+mn*-op^*u/v/t*+
23        q           +                      kl+mn*-op^*u/v/t*+q
24                                           kl+mn*-op^*u/v/t*+q+                        
                                           

I/P
hi hello are you???
O/P
uo yerao lle hih???
                        
                        
                                             