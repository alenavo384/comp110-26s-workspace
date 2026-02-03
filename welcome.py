"""A welcoming test program to start COMP110"""

__author__ = "01234567"

print("Welcome to COMP110!")
print("You are in for a fun adventure into programming!")
print("<3, the COMP110 Team!")


def total_cost(price: int, tax_rate: float) -> float:
    print(price + (price * tax_rate))


print(total_cost(price=100, tax_rate=0.07))
