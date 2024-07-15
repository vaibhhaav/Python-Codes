# Using imput function
variable = input("Enter a string: ")

# Using eval function
# Evaluating a specific expression
try:
    result = eval("51 + (54 * (3+2))")
    print("The result of the expression '51 + (54 * (3+2))' is:", result)
except Exception as e:
    print("Error in evaluating the specific expression:", e)