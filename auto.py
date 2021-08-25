import os

os.system("pwd")
# os.system("python Python/PythonHeterodyning.py")

# File_object = open(r"Python/PythonHeterodyning.py", "r")
# print(File_object.readlines()[0])
# File_object.close

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

# os.system("cd ./C && make")

# Test
# for i in range(20):
os.system("cd ./Python/ && ./PythonHeterodyning.py")
