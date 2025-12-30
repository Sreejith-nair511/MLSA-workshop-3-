# Supervised Learning Example
# Predict whether a student passes based on study hours

# Training data (input, output)
training_data = [
    (1, "Fail"),
    (2, "Fail"),
    (3, "Fail"),
    (4, "Pass"),
    (5, "Pass")
]

# Simple model: learn decision boundary
def train_model(data):
    for hours, result in data:
        if result == "Pass":
            return hours
    return None

threshold = train_model(training_data)

def predict(study_hours):
    if study_hours >= threshold:
        return "Pass"
    else:
        return "Fail"


print("Prediction for 2 hours:", predict(2))
print("Prediction for 5 hours:", predict(5))
