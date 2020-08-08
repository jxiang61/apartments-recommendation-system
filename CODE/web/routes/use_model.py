from sklearn.externals import joblib

# read KNN model
knn_from_joblib = joblib.load('knnmodel.pkl')

# example of the input
X = [33.864799600000005, -84.4718161, 1363, 10, 4.0]

# use the model to predict
if __name__ == "__main__":
    tmp = knn_from_joblib.predict([X])
    print(tmp)
