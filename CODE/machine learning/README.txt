



=====ML_main.ipynb=====

DESCRIPTION - This Jupyter Notebook is meant to read data in the designated .csv file (default name: output1.csv), and then use the data to train some machine learning model. Finally the model will be estimated and be saved as corresponding .pkl files for future use.

INSTALLATION - You will need Jupyter Notebook 6.0.1 and Python 3.7.6 to run this code.

EXECUTION - Launch Jupyter Notebook on your browser. Open ML_main.ipynb. CLick Cell and select Run All



=====use_model.py=====

DESCRIPTION - This .py file is meant to show JavasScript programmers an example how to use the trained machine learning model. It will read the KNN model in the current folder and predict and output two test data points given in this code (please execute ML_main.ipynb to get knnmodel.pkl first)


INSTALLATION - You will need Python 3.7.6 to run this code. Besides, you also need to install joblib version 0.13.2 to be able to run the code (in terminal, type the following: pip3 install joblib==0.13.2)

EXECUTION - Open use_model.py with Python's default IDLE and click Run, and then Run module. This should give you the predicted results (price) for two test data points
