# CRUD in files

# open

myFIle = open("testfile.txt", "w")

# get some info
print(myFIle.name, myFIle.closed, myFIle.mode)

# write
myFIle.write("I love Golang")
myFIle.write(" and I also love python")
myFIle.close()

# append
myFIle = open("testfile.txt", "a")
myFIle.write(" and I may also work with Java")

myFIle.close()

# read 
myFIle = open("testfile.txt", "r+")
txt = myFIle.read(1000)
print(txt)