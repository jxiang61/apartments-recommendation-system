#from sklearn.externals
import joblib

# read KNN model
knn_from_joblib = joblib.load('knnmodel.pkl')

# example of the input
mean_la = 33
mean_lo = -84
scl = 10000
t = [[33.864799600000005, -84.4718161, 1363, 4, 4.0],[33.864799600000005, -84.9718161, 1363, 4, 4.0]]
for i in range(len(t)):
    t[i][0] = (t[i][0] - mean_la) * scl
    t[i][1] = (t[i][1] - mean_lo) * scl

# use the model to predict
print(knn_from_joblib.predict(t))
