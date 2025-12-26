from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.datasets import load_iris
import numpy as np
import pdb

df = load_iris()
X = df['data']
y = df['target']

# misaligned labels with features
np.random.shuffle(y)

# wrong label encoding (change label into float)
y = y * 1.5 

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

pdb.set_trace()

scaler = StandardScaler()

X_train = scaler.fit_transform(X_train)
# also fit transform on test set
X_test = scaler.fit_transform(X_test)

model = LogisticRegression()

# incorrectly fit X_test with y_train (inequal dimension)
model.fit(X_test, y_train)

y_pred = model.predict(X_test)
