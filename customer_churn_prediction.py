# Customer Churn Prediction using Logistic Regression
# Auto-generated from the Jupyter Notebook


# ------------------------------------------------------------
# ## Import the Libraries

# Cell 2
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix,accuracy_score,classification_report,ConfusionMatrixDisplay
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import StandardScaler
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder


# ------------------------------------------------------------
# ## Import the Datset

# Cell 4
df=pd.read_csv("customer_churn_dataset-testing-master.csv")
X = df.drop(['CustomerID', 'Churn'], axis=1)
y = df['Churn']


# ------------------------------------------------------------
# # Exploratory Data Analysis (EDA)

# Cell 6
df.info()


# Cell 7
df.describe()


# Cell 8
pd.set_option('display.max_rows',None)
df.isnull().sum().sort_values(ascending=False)


# Cell 9
df.dtypes


# ------------------------------------------------------------
# ## Split the Data into Training and Testing

# Cell 11
X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.2,random_state=42)


# ------------------------------------------------------------
# ## Data Preprocessing

# ------------------------------------------------------------
# - ###  Encoding

# Cell 14
categorical_columns=X_train.select_dtypes(include=[object]).columns
print(categorical_columns)
numerical_columns = X_train.select_dtypes(include=['int64', 'float64']).columns
print(numerical_columns)


# Cell 15
ct=ColumnTransformer(transformers=[('encoder',OneHotEncoder(),categorical_columns)],remainder='passthrough')
X_train = ct.fit_transform(X_train)
X_test = ct.transform(X_test)


# Cell 16
print(X_train.shape)


# Cell 17
print(X_test.shape)


# ------------------------------------------------------------
# ## Feature Scaling

# Cell 19
sc = StandardScaler()
X_train = sc.fit_transform(X_train)
X_test = sc.transform(X_test)


# ------------------------------------------------------------
# ## Train the Model

# Cell 21
classifier=LogisticRegression(random_state=42)
classifier.fit(X_train,y_train)


# ------------------------------------------------------------
# ## Predict Test Set

# Cell 23
y_pred=classifier.predict(X_test)


# Cell 24
print(y_pred)


# ------------------------------------------------------------
# ## Confusion Matrix

# Cell 26
cm = confusion_matrix(y_test, y_pred)
ConfusionMatrixDisplay.from_predictions(y_test, y_pred)
plt.show()


# ------------------------------------------------------------
# ## Accuracy

# Cell 28
accuracy = accuracy_score(y_test, y_pred)
print(f'Accuracy: {accuracy:.2%}')


# ------------------------------------------------------------
# ## Classification Report

# Cell 30
print(classification_report(y_test, y_pred))
