def main():
    x = float(input("Enter the first number: "))
    y = float(input("Enter the second number: "))
    z = float(input("Enter the thrid number: "))
    print("Ascending" if (x <= y) and (y <= z) else "Not Ascending")

main()