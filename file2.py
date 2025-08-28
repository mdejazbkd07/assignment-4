file=open('sample2.txt','r+')

no_of_input=int(input("enter the number of input : "))
for i in range(1,no_of_input+1):
    lines=input(f" enter input {i} : ")
    file.write(lines)
    file.write("\n")
file.close()

file=open('sample2.txt','r+')
rd=file.read()
print(rd)
file.close()