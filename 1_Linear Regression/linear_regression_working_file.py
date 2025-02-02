import pandas as pd
import numpy as np
import sklearn
from sklearn import linear_model
import matplotlib.pyplot as pyplot
import pickle
from matplotlib import style

data = pd.read_csv("student-mat.csv", sep=";")

data = data[["G1", "G2", "G3", "studytime", "failures", "absences"]]

predict = "G3"

x = np.array(data.drop([predict], 1))
y = np.array(data[predict])
x_train, x_test, y_train, y_test = sklearn.model_selection.train_test_split(x, y, test_size=0.1)
'''
best = 0
for _ in range(30):
    x_train, x_test, y_train, y_test = sklearn.model_selection.train_test_split(x, y, test_size=0.1)

    linear = linear_model.LinearRegression()

    linear.fit(x_train, y_train)
    accuracy = linear.score(x_test, y_test)
    print(accuracy)

    if accuracy > best:
        best = accuracy
        with open("studentmodel.pickle", "wb") as f:
            pickle.dump(linear, f) '''

pickle_in = open("studentmodel.pickle", "rb")
linear = pickle.load(pickle_in)

# print("Accuracy: %{}".format(accuracy * 100))
# print("-=" * 20)


print("Coefficients: \n", linear.coef_)
print("Intercept: \n", linear.intercept_)
print("-=" * 20)

predictions = linear.predict(x_test)

for x in range(len(predictions)):
    print("Student: {} | Prediction: {} | Actual: {} | Coefficients: {}".format(
            x, predictions[x].round(), y_test[x], x_test[x]))

p = 'G1'
style.use("ggplot")
pyplot.scatter(data[p], data["G3"])
pyplot.xlabel(p)
pyplot.ylabel("Final Grade")
pyplot.show()