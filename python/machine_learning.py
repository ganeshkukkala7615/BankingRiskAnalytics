import pandas as pd
import joblib

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report

print("=" * 70)
print("BANKING RISK ANALYTICS - MACHINE LEARNING")
print("=" * 70)

# Load Dataset
df = pd.read_csv("../data/raw/bank-full.csv", sep=";")

# Convert target column to numeric
df["y"] = df["y"].map({"yes": 1, "no": 0})

# One-Hot Encode all categorical columns
X = pd.get_dummies(df.drop("y", axis=1), drop_first=True)

# Target
y = df["y"]

# Train-Test Split
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.20,
    random_state=42,
    stratify=y
)

# Models
models = {
    "Logistic Regression": LogisticRegression(max_iter=3000),
    "Decision Tree": DecisionTreeClassifier(random_state=42),
    "Random Forest": RandomForestClassifier(
        n_estimators=200,
        random_state=42
    )
}

best_model = None
best_accuracy = 0

for name, model in models.items():

    model.fit(X_train, y_train)

    predictions = model.predict(X_test)

    accuracy = accuracy_score(y_test, predictions)

    print("\n" + "=" * 60)
    print(name)
    print("=" * 60)

    print(f"Accuracy: {accuracy * 100:.2f}%\n")

    print(classification_report(y_test, predictions))

    if accuracy > best_accuracy:
        best_accuracy = accuracy
        best_model = model

# Save Best Model
joblib.dump(best_model, "../models/saved_models/best_model.pkl")

print("\n" + "=" * 70)
print("BEST MODEL SAVED SUCCESSFULLY")
print(f"Best Accuracy: {best_accuracy * 100:.2f}%")
print("=" * 70)