"""
MNIST Digit Classification using scikit-learn

This example shows:
- Real dataset usage
- Proper ML pipeline
- Training, testing, and evaluation
"""

# 1. Import libraries
from sklearn.datasets import load_digits
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report

# 2. Load dataset (digits dataset similar to MNIST)
digits = load_digits()
X = digits.data      # Features (pixel values)
y = digits.target    # Labels (0–9)

# 3. Split data into training and testing
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# 4. Create model
model = LogisticRegression(
    max_iter=1000,
    solver="lbfgs",
    multi_class="auto"
)

# 5. Train model
model.fit(X_train, y_train)

# 6. Make predictions
y_pred = model.predict(X_test)

# 7. Evaluate model
accuracy = accuracy_score(y_test, y_pred)
print("Model Accuracy:", accuracy)

print("\nClassification Report:")
print(classification_report(y_test, y_pred))
#actual implementation of ml

#executes the ml properly
#pip install scikit-learn to get started with this code