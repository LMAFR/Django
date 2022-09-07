try:
    # f = open("Python_others/test.txt", "a")
    f = open("Python_others/test.txt", "r")
    f.write("Adios mundo")
# except IOError:
except:
    print("ERROR: could not find file or read data")
else:
    print("SUCCESS")
    f.close()
finally:
    print("THIS WILL ALWAYS WORK, NO MATTER WHAT!")