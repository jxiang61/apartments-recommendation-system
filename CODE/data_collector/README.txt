CSE6242 Data Collection

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
