
#Enter full file name along with the path in which you want to write and append

filename = input("Enter file name: ")
text = input("Enter text to write to the file: ")

file1 = open(filename,'w')
writefile = file1.write(text)
file1.close()
print("Data successfully written to ", filename)

append = input("Enter additional text to append: ")

file2 = open(filename,'a')
writefile = file2.write(append)
file2.close()
print("Data successfully appended ", filename)


print("Final content of '",filename,"':")
file1 = open(filename,'r')
readfile = file1.read()
print(readfile)
file1.close()

