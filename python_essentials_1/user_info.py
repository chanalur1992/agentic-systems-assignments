def User_Info(first_name, last_name, age):
    if type(age) != int:
        print("Invalid age input")
        return  # Exit the function if age is not an integer
    if age < 0:
        print("Age cannot be negative")
        return  # Exit the function if age is negative
    print("Full Name: ", first_name + " " + last_name)
    print("You will be ", age + 1, " next year")

# Example usage
User_Info("John", "Doe", 30)