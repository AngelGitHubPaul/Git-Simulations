print("\n Helloworld \n") 

print("Python calculator")

#print("Choose which operation do you want to use: ")

#operation = int (input("Choose the number which operation do you want to use: "))

def add(firstNum, secondNum):
    return firstNum + secondNum
def subtract(firstNum, secondNum):
    return firstNum - secondNum
def multiply(firstNum, secondNum):
    return firstNum * secondNum
def divide(firstNum, secondNum):
    return firstNum / secondNum
def modulo(firstNum, secondNum):
    return firstNum % secondNum

while True:
    print("\nChoose the number which operation do you want to use: \n" \
    	"1. Additon + \n" \
    	"2. Subtraction - \n" \
    	"3. Multiplication * \n" \
    	"4. Division / \n"\
    	"5. Modulo % \n")

 

    operation = input("Enter the number of the operation you want to use: ")

    if operation in ('1', '2', '3', '4', '5'):
        firstNum = float(input("\nEnter first number: "))
        secondNum = float(input("Enter second number: "))

        if operation == '1':
            print(firstNum, "+", secondNum, "=", add(firstNum, secondNum))

        elif operation == '2':
            print(firstNum, "-", secondNum, "=", subtract(firstNum, secondNum))

        elif operation == '3':
            print(firstNum, "*", secondNum, "=", multiply(firstNum, secondNum))

        elif operation == '4':
            print(firstNum, "/", secondNum, "=", divide(firstNum, secondNum))

        elif operation == '5':
            print(firstNum, "%", secondNum, "=", modulo(firstNum, secondNum))        
 
        doAgain = input("Let's do next calculation? (yes/no): ")
        if doAgain in ("yes"):
         	True
        else:
         	break
#        if doAgain == "no":
#            break
    else:
        print("\nInvalid Input DO IT AGAIN")


