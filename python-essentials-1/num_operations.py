def Number_operations(n1,n2):
    if type(n1) == int and type(n2) == int:
        if n2 != 0:
            print("Sum: ", n1 + n2)
            print("Division result: ", n1 / n2)
        else:
            print("Cannot divide by zero")
    else:
        print("Invalid input")

# Example usage
Number_operations(10, 5)