#!/usr/bin/env python
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
    File_object = open(r"C/makefile", "r+")
    files = File_object.readlines()
    File_object.close
    # print(files[2])
    File_object.close
    File_object = open(r"C/makefile", "w+")
    files[2] = "CFLAGS = -lm -lrt {}\n".format(a)
    File_object.writelines(files)

def setCC(a):
    File_object = open(r"C/makefile", "r+")
    files = File_object.readlines()
    File_object.close
    # print(files[1])
    File_object.close
    File_object = open(r"C/makefile", "w+")
    files[1] = "CC = arm-linux-gnueabihf-g++ {}\n".format(a)
    File_object.writelines(files)

def setBits(a):
    File_object = open(r"C/src/CHeterodyning_threaded.c", "r+")
    files = File_object.readlines()
    File_object.close
    # print(files[2])
    File_object.close
    File_object = open(r"C/src/CHeterodyning_threaded.c", "w+")
    files[2] = "{} result [SAMPLE_COUNT];\n".format(a)
    File_object.writelines(files)
    File_object.close
    #       
    File_object = open(r"C/src/CHeterodyning.c", "r+")
    files = File_object.readlines()
    File_object.close
    # print(files[2])
    File_object.close
    File_object = open(r"C/src/CHeterodyning.c", "w+")
    files[2] = "extern {} data[SAMPLE_COUNT];\n".format(a)
    files[3] = "extern {} carrier[SAMPLE_COUNT];\n".format(a)
    File_object.writelines(files)
    File_object.close
    # 
    File_object = open(r"C/src/globals.h", "r+")
    files = File_object.readlines()
    File_object.close

    editC=files[4].split('=')[0]
    carrier=files[4].split('=')[1]
    editC="{} carrier[SAMPLE_COUNT]".format(a)
    files[4]= editC+" ="+carrier

    editD=files[5].split('=')[0]
    data=files[5].split('=')[1]
    # print(editD)
    editD="{} data[SAMPLE_COUNT]".format(a)
    files[5]= editD+" ="+data

    File_object = open(r"C/src/globals.h", "w+")
    File_object.writelines(files)
    File_object.close

# Test
print("\nxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")
print("Python measure:\n")
print("xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx\n")
for i in range(4):
    os.system("cd ./Python/ && python PythonHeterodyning.py > /dev/null")
os.system("cd ./Python/ && python PythonHeterodyning.py")

print("\nxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")
print("C floats measure:\n")
print("xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx\n")
setBits("float")
os.system("cd ./C && make")
for i in range(4):
    os.system("cd ./C && make run  > /dev/null")
os.system("cd ./C && make run")

print("\nxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")
print("C 1 thread measure:\n")
print("xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx\n")
os.system("cd ./C && make threaded")
for i in range(4):
    os.system("cd ./C && make run_threaded > /dev/null")
os.system("cd ./C && make run_threaded")

nums =[2,4,8,16,32]
for b in nums:
    print("\nxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")
    print("C {} threads measure:\n".format(b))
    print("xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx\n")
    setThreads(b)
    os.system("cd ./C && make threaded")
    for i in range(4):
        os.system("cd ./C && make run_threaded > /dev/null")
    os.system("cd ./C && make run_threaded")

print("pi has one core")
print("16 threads works best")
setThreads(16)

flags =["-O0","-O1","-O2","-O3","-Ofast","-Os","-Og"]
for b in flags:
    print("\nxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")
    print("C {} flag measure:\n".format(b))
    print("xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx\n")
    setCFLAGS(b)
    os.system("cd ./C && make")
    for i in range(4):
        os.system("cd ./C && make run_threaded > /dev/null")
    os.system("cd ./C && make run_threaded")
flags =["-O0","-O1","-O2","-O3","-Ofast","-Os","-Og"]
for b in flags:
    print("\nxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")
    print("C {} -funroll-loops flag measure:\n".format(b))
    print("xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx\n")
    setCFLAGS(b+" -funroll-loops")
    os.system("cd ./C && make")
    for i in range(4):
        os.system("cd ./C && make run_threaded > /dev/null")
    os.system("cd ./C && make run_threaded")

setCFLAGS("")
print("float is 32-bits [CHECK THREAD 1 FOR RESULT]")

print("double is 64-bits")
print("\nxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")
print("C double measure:\n")
print("xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx\n")
setBits("double")
os.system("cd ./C && make")
for i in range(4):
    os.system("cd ./C && make run_threaded > /dev/null")
os.system("cd ./C && make run_threaded")

print("\nxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")
print("C __fp16 measure:\n")
print("xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx\n")
setBits("__fp16")
setCC("-mfp16-format=ieee")
os.system("cd ./C && make")
for i in range(4):
    os.system("cd ./C && make run_threaded > /dev/null")
os.system("cd ./C && make run_threaded")

# print("Best combo is: 16 threads with no extra compiler flags\n")
