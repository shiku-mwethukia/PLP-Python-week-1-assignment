num_1 = int(input("Enter the first number: "))
num_2 = int(input("Enter the second number: "))
operator = input("Enter an operator: ")
if operator == "+":
   answer = num_1 + num_2
elif operator == "*":
   answer = num_1 * num_2
elif operator == "-":
   answer = num_1 - num_2
elif operator == "/":
   answer = num_1 / num_2
print(num_1, operator, num_2, "=", answer)