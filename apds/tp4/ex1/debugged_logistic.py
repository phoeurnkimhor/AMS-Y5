from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.datasets import load_iris
from sklearn.metrics import classification_report

df = load_iris()
X = df['data']
y = df['target']
# remove randomly shhuffling y and multiplying y by 1.5

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

scaler = StandardScaler()

X_train = scaler.fit_transform(X_train)
# only transform x-test not fit transform
# X_test = scaler.transform(X_test)

model = LogisticRegression()

# fit var with the same dimension
model.fit(X_train, y_train)

y_pred = model.predict(X_test)

print(classification_report(y_pred, y_test))

# accuracy: 1.00, samples: 30