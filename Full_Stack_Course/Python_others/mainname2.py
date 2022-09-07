import mainname1

print("TOP LEVEL TWO.PY")
mainname1.func()

if __name__ == '__main__':
    print("mainname2 has been directly executed.")
else:
    print("mainname2 has been imported.")