print("Muhammad Bassam")
print("18B-077-CS(A)")
print("Lab - 04")
print("Question 1")

print("\n\nQuadratic Equation Solution")

def quadratic_sol():

    SUP = str.maketrans("0123456789", "⁰¹²³⁴⁵⁶⁷⁸⁹")
    print("\nax2+bx+c".translate(SUP))

    a= eval(input("\nPlease enter the value of 'a' :"))
    b= eval(input("Please enter the value of 'b' :"))
    c= eval(input("Please enter the value of 'c' :"))

    if a==0:
        print("The vaule of 'a' can never be zero. Please enter a valid value to continue")
        quadratic_sol()
    import math        
    x1 = ((-b)-(math.sqrt((b**2)-(4*a*c)))) / (2*a) 
    x2 = ((-b)+(math.sqrt((b**2)-(4*a*c)))) / (2*a) 

    print("The values of x in the equation is : (", str(x1),",",str(x2),")")

    user = input("\nDo you want to solve another equation?(press 'y' or 'q' to exit.")
    if user=='y':
        quadratic_sol()
    else:
        print("Goodbye!")

quadratic_sol()
