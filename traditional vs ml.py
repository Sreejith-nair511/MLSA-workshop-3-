# Traditional Programming vs Machine Learning (Conceptual Example)

# Traditional Programming
# Rule is written by the programmer

def is_pass_traditional(marks):
    if marks >= 40:
        return "Pass"
    else:
        return "Fail"


# "Machine Learning style" (simulated learning using examples)
# Rule is inferred from data

training_data = [
    (30, "Fail"),
    (45, "Pass"),
    (60, "Pass"),
    (20, "Fail")
]

def is_pass_ml(marks):
    # Simple learned rule from examples
    threshold = 40
    return "Pass" if marks >= threshold else "Fail"


print("Traditional:", is_pass_traditional(35))
print("ML style:", is_pass_ml(35))
