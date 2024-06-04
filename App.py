#toplama işlemi
def add(x,y):
    return x + y
#çıkarma işlemi
def sub(x,y):
    return x - y
#çarpma işlemi
def mul(x,y):
    return x * y
#bölme işlemi
def div(x,y):
    return x / y

print("Select Operation")
print("1 = Add")
print("2 = Subtract")
print("3 = Multiply")
print("4 = Divide")

while True:
    #kullanıcıdan girdi al
    choice = input("Enter Operation: ")

    #verilen dört seçenekten biri olup olmadığını kontrol et
    if choice == "1":
        try:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
        except ValueError:
            print("Invalid Input")
            continue

        if choice == '1':
            print(num1, "+", num2, "=", add(num1, num2))

        elif choice == '2':
            print(num1, "-", num2, "=", sub(num1, num2))

        elif choice == "3":
            print(num1, "*", num2, "=", mul(num1, num2))

        elif choice == "4":
            print(num1, "/", num2, "=", div(num1, num2))

        break
    else:
        print("Invalid Input")
        break
