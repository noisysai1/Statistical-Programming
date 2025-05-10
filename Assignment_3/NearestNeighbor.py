# kMeans.py

print("DATA-51100, FALL-2023")
print("Sai Kumar Murarishetti")
print("PROGRAMMING ASSIGNMENT #3")

# Import library
import num    py as np

# Assigning training and testing data to variables
train_data = "iris-training-data.csv"
test_data = "iris-testing-data.csv"

# Read in features and responses of training data using numpy
data_train = np.loadtxt(train_data, delimiter=",", usecols=(0, 1, 2, 3, 4), dtype="str")
xtrain_arr, ytrain_arr = data_train[:, :-1].astype(float), data_train[:, -1]

# Read in features and responses of test data using numpy
data_test = np.loadtxt(test_data, delimiter=",", usecols=(0, 1, 2, 3, 4), dtype="str")
xtest_arr, ytest_arr = data_test[:, :-1].astype(float), data_test[:, -1]

# Determine index of nearest neighbor for each data point in the test set
nn_index = np.argmin(np.linalg.norm(xtrain_arr[:, np.newaxis] - xtest_arr, axis=2), axis=0)

# Create a new array of predicted response for each test data point
pred = ytrain_arr[nn_index]

# Compare predictions to actual response for each data point, returns array of True/False
comp = pred == ytest_arr

# Calculate accuracy based on the number of True values divided by the total number of data points
accuracy = np.mean(comp)

# Print out true vs predicted
print("# , True, Predicted")
for i, (true, predicted) in enumerate(zip(ytest_arr, pred)):
    print(f"{i + 1} {true} {predicted}")

# Print accuracy
print(f"Accuracy: {accuracy * 100:.2f}%")
