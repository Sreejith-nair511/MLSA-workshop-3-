# Simple supervised learning example (no libraries)
# Predict Pass/Fail based on study hours

# Training data: (study_hours, result)
training_data = [
    (1, "Fail"),
    (2, "Fail"),
    (3, "Fail"),
    (4, "Pass"),
    (5, "Pass")
]

def train_model(data):
    for hours, result in data:
        if result == "Pass":
            return hours

threshold = train_model(training_data)

def predict(study_hours):
    if study_hours >= threshold:
        return "Pass"
    return "Fail"


print("Prediction for 2 hours:", predict(2))
print("Prediction for 5 hours:", predict(5))
# Improvements made:
# 1. Clear separation of training and prediction logic.
# 2. Simple model training function to determine threshold.
# 3. Reusable predict function for new data.
# 4. Conceptual alignment with ML thinking: training a model and making predictions.

# Note: This is a very basic example and does not represent real-world ML practices.
# In practice, one would use established ML libraries and techniques.