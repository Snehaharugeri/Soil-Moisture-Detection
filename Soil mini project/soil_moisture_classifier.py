import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report
import joblib

data = {
    'moisture': [100, 110, 115, 125, 130, 140, 145, 150, 155, 160, 170, 180, 190, 200],
    'label': ['Dry', 'Dry', 'Dry', 'Dry', 'Dry', 'Dry', 'Wet', 'Wet', 'Wet', 'Wet', 'Wet', 'Wet', 'Wet', 'Wet']
}

df = pd.DataFrame(data)

X = df[['moisture']]
y = df['label']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
model = DecisionTreeClassifier()
model.fit(X_train, y_train)

y_pred = model.predict(X_test)
print("Accuracy:", accuracy_score(y_test, y_pred))
print("\nClassification Report:\n", classification_report(y_test, y_pred))

cm = confusion_matrix(y_test, y_pred, labels=["Dry", "Wet"])
print("Confusion Matrix:")
print("      Predicted")
print("        Dry  Wet")
print(f"Actual Dry  {cm[0][0]:>4}  {cm[0][1]:>3}")
print(f"       Wet  {cm[1][0]:>4}  {cm[1][1]:>3}")

joblib.dump(model, 'moisture_classifier.pkl')
