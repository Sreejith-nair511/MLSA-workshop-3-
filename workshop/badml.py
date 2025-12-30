# Bad ML-style code (conceptually wrong + poor practice)

data = [1, 2, 3, 4, 5]
result = []

for i in data:
    if i > 3:
        result.append("Pass")
    else:
        result.append("Fail")

print(result)
