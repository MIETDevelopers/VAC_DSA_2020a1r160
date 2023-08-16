#Printing pascal triangle.
def pascal(n):
    if n==1:
        return [1]
    else: 
        line = [1]
        previousLine = pascal(n-1)
        for i in range(len(previousLine)-1):
            line.append(previousLine[i]+previousLine[i+1])
        line+=[1]
        print(line)
    return line
pascal(5)