# Inputs are strings by deafult unless casted to some other type in this case integer.
n = int(input("Number: "))

# indentation lies at the heart of the python's syntax!
# pytohn force you to write pretty(well-indented) code

if n > 0:
    print("n is positive.")
elif n < 0:
    print("n is negative.")
else:
    print("n is zero.")
