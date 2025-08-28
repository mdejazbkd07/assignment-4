try:
    file=open('sample.txt','r')
    r=file.read()
    print(r)
    file.close()
except FileNotFoundError:
    print("Error : the file 'sample.txt' was not found.")