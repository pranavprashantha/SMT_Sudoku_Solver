for i in range(1, 10):
    for j in range(1, 10):
        for n in range(1, 10):
            print("(declare-const P_" + str(i) + "_" + str(j) + "_" + str(n) + " Bool)")
print(";--------------------------")            
while True:
    num = input(";Enter row number, column number, and value as (r,c,n). Enter 'STOP' if there are no more inputs ")
    if num == 'STOP':
        break
    r, c, n = num.split(',')
    print(f'(assert P_{r}_{c}_{n})')
print(";--------------------------")
for i in range(1, 10):
    for n in range(1, 10):
        row = "(assert (or"
        for j in range(1, 10):
            row += " " + "P_" + str(i) + "_" +str(j) + "_" + str(n)
            
        row += "))"
        print(row)
print(";--------------------------")      
for j in range(1, 10):
    for n in range(1, 10):
        column = "(assert (or"
        for i in range(1, 10):
            column += " " + "P_" + str(i) + "_" +str(j) + "_" + str(n)
            
        column += "))"
        print(column)
print(";--------------------------")        
for r in range(0, 3):
    for c in range(0, 3):
        for n in range(1, 10):
            block = "(assert (or"
            for i in range(1, 4):
                for j in range(1, 4):
                    block += " " + "P_" + str(3*r+i) + "_" + str(3*c+j) + "_" + str(n)
            block += "))"
            print(block)
print(";--------------------------")            
for i in range(1, 10):
    for j in range(1, 10):
        for n in range(1, 10):
            cell = "(assert (or (not " + "P_" + str(i) + "_" + str(j) +"_" + str(n) +  ") (not (or"
            for n1 in range(1, 10):
                if n == n1:
                    continue
                cell += " " + "P_" + str(i) + "_" + str(j) +"_" + str(n1)
            cell += "))))"
            print(cell)
            
            
print("(check-sat)")
print("(get-model)")