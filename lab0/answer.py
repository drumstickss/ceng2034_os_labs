import os

os.chdir("/home/ozan")

os.mkdir("os_lab_0")

os.chdir("/home/ozan/os_lab_0")

os.mknod("drum.txt")

os.mknod("guitar.txt")

os.mknod("band.py")

os.system("ls -l")

os.chdir("/home/ozan/os_lab_0")

text_files = [f for f in os.listdir("/home/ozan/os_lab_0") if f.endswith('.txt')]

print(text_files)

# docs = os.listdir()

# for doc in docs:
#	if doc.endswith(".txt") :
#		print(doc)
