import os

# 2 threads, 4 threads, 8 threads, 16 threads and 32 threads.
def setThreads(a):
    File_object = open(r"./C/src/CHeterodyning_threaded.h", "r+")
    files = File_object.readlines()
    File_object.close
    # print(files[14])
    File_object = open(r"./C/src/CHeterodyning_threaded.h", "w+")
    files[14] = "#define Thread_Count {}\n".format(a)
    File_object.writelines(files)

def setCFLAGS(a):
    File_object = open(r"c/makefile", "r+")
    files = File_object.readlines()
    File_object.close
    # print(files[2])
    File_object.close
    File_object = open(r"c/makefile", "w+")
    files[2] = "CFLAGS = -lm -lrt {}\n".format(a)
    File_object.writelines(files)

def setCC(a):
    File_object = open(r"c/makefile", "r+")
    files = File_object.readlines()
    File_object.close
    # print(files[1])
    File_object.close
    File_object = open(r"c/makefile", "w+")
    files[1] = "CC = arm-linux-gnueabihf-g++ {}\n".format(a)
    File_object.writelines(files)

def setBits(a):
    File_object = open(r"c/src/CHeterodyning_threaded.c", "r+")
    files = File_object.readlines()
    File_object.close
    # print(files[2])
    File_object.close
    File_object = open(r"c/src/CHeterodyning_threaded.c", "w+")
    files[2] = "{} result [SAMPLE_COUNT];\n".format(a)
    File_object.writelines(files)
    File_object.close
    #       
    File_object = open(r"c/src/CHeterodyning.c", "r+")
    files = File_object.readlines()
    File_object.close
    # print(files[2])
    File_object.close
    File_object = open(r"c/src/CHeterodyning.c", "w+")
    files[2] = "extern {} data [SAMPLE_COUNT];\n".format(a)
    File_object.writelines(files)
    File_object.close
    # 
    File_object = open(r"c/src/globals.h", "r+")
    files = File_object.readlines()
    File_object.close
    # print(files[4])
    # print(files[5])
    File_object = open(r"c/src/globals.h", "w+")
    files[4] = "{} carrier[SAMPLE_COUNT];\n".format(a)
    files[5] = "{} data[SAMPLE_COUNT];\n".format(a)
    File_object.writelines(files)
    File_object.close

# Set testing variables

# setThreads(1)
# setCFLAGS("")
# setBits("float")
# setCC("-mfp16-format=iee")

# Test

# for i in range(20):

print("Python measure:\n")
os.system("cd ./Python/ && python PythonHeterodyning.py")

print("C floats measure:\n")
setBits("float")
os.system("cd ./C && make")
os.system("cd ./C/bin && ./CHeterodyning")

print("C 1 thread measure:\n")
os.system("cd ./C/bin && ./CHeterodyning_threaded")

nums =[2,4,6,16,32]
for b in nums:
    print("C {} threads measure:\n".format(b))
    setThreads(b)
    os.system("cd ./C && make")
    os.system("cd ./C/bin && ./CHeterodyning_threaded")

print("pi has one core")

flags =["-O0","-O1","-O2","-O3","-Ofast","-Os","-Og"]
for b in flags:
    print("C {} flag measure:\n".format(b))
    setCFLAGS(b)
    os.system("cd ./C && make")
    os.system("cd ./C/bin && ./CHeterodyning_threaded")
flags =["-O0","-O1","-O2","-O3","-Ofast","-Os","-Og"]
for b in flags:
    print("C {} -funroll-loops flag measure:\n".format(b))
    setCFLAGS(b+" -funroll-loops")
    os.system("cd ./C && make")
    os.system("cd ./C/bin && ./CHeterodyning_threaded")
b="-O3 -Os"
print("C {} flag measure:\n".format(b))
setCFLAGS(b)
os.system("cd ./C && make")
os.system("cd ./C/bin && ./CHeterodyning_threaded")
b="-O3 -Os -funroll-loops"
print("C {} flag measure:\n".format(b))
setCFLAGS(b)
os.system("cd ./C && make")
os.system("cd ./C/bin && ./CHeterodyning_threaded")

setCFLAGS("")
print("float is 32-bits")

setBits("double")
print("double is 64-bits")

setBits("__fp16")
setCC("-mfp16-format=iee")
print("__fp16 is 16-bits")

print("Best combo is: \n")
