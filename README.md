
Our final product is a website so there is no need to execute or install it. The service is deployed to Heroku. The link is https://final6242.herokuapp.com. For our website using guiding, user should sign up on our website first, then click the location on the map that you want to predict the price around and enter the desired information. The red pinged points are apartments in our dataset and you can move the cursor on it to view the detail of that apartment. Then you will get the predicted price near that spot.

The whole project consists 5 parts: data collection, data cleaning, google map api, machine learning, web implementation. Below are short descriptions of each parts and you can test them separately.

=========Data Collection==========

Description:
This package includes the code needed for data collection, we extract over 2000 houses infos in five counties of Atlanta by copy the return information from Zillow.com, and store it in json folder.
all the information will be written into House_info.csv.
the package contains two Python3 scripts:
1. get_detail_url_list.py: this script will extract all the URLs from .json file in json folder, and write them into a variable list.
2. get_home_detail.py: this script will extract information of apartment based on the URL list from get_detail_url_list.py. all the information will be written into House_info.csv.

Installation:
use Python3 environment

Execution
Directly run the following line in the terminal:

    python get_detail_url_list.py
    python get_home_detail.py

and the output will be written in House_info.csv


=========data cleaning===========

DESCRIPTION - This Jupyter Notebook is meant to clean the data we collected and stored in the .csv file (default name: House_info2.csv, you can use House_info3.csv, which is also included), and output the cleaned data into another .csv file (default name: house_info_cleaned2.csv)

INSTALLATION - You will need Jupyter Notebook 6.0.1 and Python 3.7.6 to run this code

EXECUTION - Launch Jupyter Notebook on your browser. Open Initial_clean_0.ipynb. CLick Cell and select Run All


=========google map api=========

Description - The file map_get_geo.ipynb can read the rental properties' address information and output the geo-location including latitute and longitute.

Installation - Python 3.7.6 and packages including json, requests, csv, pandas and googlemaps are required. And your own google map api is required.

Execution - Launch Jupyter Notebook on your browser. Open map_get_geo.ipynb CLick Cell and select Run All


=====machine learning------ML_main.ipynb=====

DESCRIPTION - This Jupyter Notebook is meant to read data in the designated .csv file (default name: output1.csv), and then use the data to train some machine learning model. Finally the model will be estimated and be saved as corresponding .pkl files for future use.

INSTALLATION - You will need Jupyter Notebook 6.0.1 and Python 3.7.6 to run this code.

EXECUTION - Launch Jupyter Notebook on your browser. Open ML_main.ipynb. CLick Cell and select Run All



=====machine learning-----use_model.py=====

DESCRIPTION - This .py file is meant to show JavasScript programmers an example how to use the trained machine learning model. It will read the KNN model in the current folder and predict and output two test data points given in this code (please execute ML_main.ipynb to get knnmodel.pkl first)


INSTALLATION - You will need Python 3.7.6 to run this code. Besides, you also need to install joblib version 0.13.2 to be able to run the code (in terminal, type the following: pip3 install joblib==0.13.2)

EXECUTION - Open use_model.py with Python's default IDLE and click Run, and then Run module. This should give you the predicted results (price) for two test data points

=========web implementation============
Description:
A simple Web service is developed to show all the data we have and porvide for user. There are three main components. First one is the user authentication using passport module in Node.js. The second component is to enable user to review apartments infomation from the map. The third part is to predict apartment price based on user's specification.

Installation and execution:
There is no installation or execution needed. The service is deployed to Heroku. The link is https://final6242.herokuapp.com. 


