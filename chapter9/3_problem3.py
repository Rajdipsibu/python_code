def MultiplicationTable_Generator(n):
    table=''
    for i in range(1,11):
        table = table + f"{n} X {i} = {n*i}\n"
    with open(f'Multiplication_Table/Table{n}.txt','w') as f:
        f.write(table)
        

for i in range(2,21):
    MultiplicationTable_Generator(i)