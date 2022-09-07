def func():
    print("func() in mainname1.py")

print("TOP LEVEL ONE.PY")

if __name__ == '__main__':
    print("mainname1 has been directly executed.")
else:
    print("mainname1 has been imported.")