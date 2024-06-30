# This application calculates Simple Interest

def simple_interest(P, N, R):
    I = (P*N*R)/100
    A = P + I
    return I, A

# Take Principal , Period and Rate of Interest as input from user
P = float(input("PLease enter Principal in INR : "))
N = float(input("PLease enter years : "))
R = float(input("Please enter rate of interest in % p.a. : " ))

# Print the interest and amount
I, A = simple_interest(P, N, R)
print(f'The Simple Interest is : {I:.2f} INR')
print(f'Total Amount is : {A:.2f} INR')
