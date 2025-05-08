
#Enter full file name along with the path

filename = input("Enter file name: ")

try:
    file1 = open(filename,'r')
    readfile = file1.read()
    print(readfile)
    file1.close()

except:
    print("The file '", filename, "' was not found")