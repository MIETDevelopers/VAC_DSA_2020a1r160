Input: Postfix: AB-CD+f/*
Input: postfix: abc*de-/+f+
Input: Postfix: ABC*DEF^/H*-+

Input :  Prefix :  *+XY-ZA   After Revere : AZ-YX+*
Output : Infix : ?
    
Step      Data     Stack         Output
1         A        A
2         Z        A,Z
3         -        Z-A            Z-A
4         Y        Z-A,Y
5         X        Z-A,y,X
6         +        Z-A,x+y        (z-A) (x+Y)
7         *        x+Y)*(Z-A)     (x+Y)*(Z-A)
