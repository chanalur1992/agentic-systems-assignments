def Elig_Checker(name,age):
    if type(age) != int:
        print("Invalid age input")
        return  # Exit the function if age is not an integer
    if age < 0:
        print("Age cannot be negative")
        return  # Exit the function if age is negative
    
    print("Hello", name)

    if age < 13:
        print("You are a Child")
    else:
        if age <= 17:
            print("You are a Teenager")
        else:
            if age <= 59:
                print("You are an Adult")
            else:
                print("You are a Senior Citizen")
    
    if age >= 18:
        print("You are eligible to vote") 
    else:
        print("You are not eligible to vote")

# Example usage
Elig_Checker("Alice", 25)