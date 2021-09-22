


#   Write a program which accept principle,rate and time from user and print the simple interest.
# The formula to calculate simple interest is: simple interest = principle x rate x time / 100 Solution


p=int(input("enter the principle: "))
r=int(input("enter the Rate: "))
t=int(input("enter the Time: "))
Si=(p*r*t)/100
print("simple interest is: {}".format(Si))
