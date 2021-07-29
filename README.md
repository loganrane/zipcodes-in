# zipcodes-in
<img width="811" alt="zipcode" align="middle" src="https://user-images.githubusercontent.com/44089458/127119397-8ce57b68-d03c-4d2e-b0a2-a4a19ab58309.png">

## ✍ Description of the project 

Zipcodes-in is a Python library built for querying India zipcodes, post offices and particular state/UT. Py Package can be installed from [here](https://pypi.org/project/zipcodes-in/).

## 📊 Data description and preparation 
- Data was extracted from [here](https://github.com/Zeeshanahmad4/Zip-code-of-all-countries-cities-in-the-world-CSV-TXT-SQL-DATABASE)
- Cleaned the data and extracted all the values for India (IN). Script can be found [here](https://github.com/ArpitFalcon/zipcodes-in/tree/main/make_data/extract%20data)
- Finally, the data was converted from CSV to JSON. The data can be found [here](https://github.com/ArpitFalcon/zipcodes-in/tree/main/make_data)

## 📍 Functionalities
- Query if a zipcode matches or not 
- List random zipcodes 
- Validate of a zipcode exists or not
- List top N zipcodes
- List any random N zipcodes 
- List all the zipcodes in the dataset (absolutely NOT recommended!)

## 💻 Installation 
```python
# Install the package 
>>> pip install zipcodes-in
```
Zipcodes-in supports Python 3.6+

## 👩‍💻 Running Scripts
```python
>>> from zipcode_script import zipcode
>>> print(zipcode)
Zipcode class to validate and fetch data of provided India zipcode

>>> # Zipcode matching
>>> print(zipcode.matching('834001'))
[{'zipcode': '834001', 
'region': 'Ranchi', 
'state_ut': 'Jharkhand', 
'country': 'India', 
'latitude': '23.3505', 
'longitude': '85.2927', 
'post_office': 'Argora.'}]

# Print random zipcodes 
>>> print(zipcode.random())
{'zipcode': '177601', 
'region': 'Hamirpur(HP)', 
'state_ut': 'Himachal Pradesh', 
'country': 'India', 
'latitude': '31.7124', 
'longitude': '76.4841', 
'post_office': 'Badhani'}

>>> # Print N random zipcodes 
>>> print(zipcode.listRandomN(3))
[{'zipcode': '711410', 
'region': 'Howrah', 
'state_ut': 'West Bengal', 
'country': 'India', 
'latitude': '22.526', 
'longitude': '88.0676', 
'post_office': 'Paikpara'}, 
{'zipcode': '585107', 
'region': 'Kalaburagi', 
'state_ut': 'Karnataka', 
'country': 'India', 
'latitude': '17.2967', 
'longitude': '76.6671', 
'post_office': 'Kalaburagi HCB'}, 
{'zipcode': '688539', 
'region': 'Alappuzha', 
'state_ut': 'Kerala', 
'country': 'India', 
'latitude': '9.7869', 
'longitude': '76.3235', 
'post_office': 'Varanad'}]

>>> # Print top N zipcodes
>>> print(zipcode.listTopN(2))
[{'zipcode': '110001', 
'region': 'New Delhi', 
'state_ut': 'Delhi', 
'country': 'India', 
'latitude': '28.6369', 
'longitude': '77.2183', 
'post_office': 'New Delhi G.P.O.'}, 
{'zipcode': '110002', 
'region': 'New Delhi', 
'state_ut': 'Delhi', 
'country': 'India', 
'latitude': '28.6453', 
'longitude': '77.2456', 
'post_office': 'Civic Centre'}]

NOTE: Version 1.0 is tested on Windows10. 
## If you face any issue while running, please raise an issue on this repository
```

⚠️ The zipcode data was last updated on: **Jul. 27th, 2021** ⚠️

## Looking forward to make the project better? 🤔
We are open to suggestions and ideas! Feel free to raise an issue and we shall get back to you super soon! 

## 📑 LICENSE 
[MIT LICENSE](https://github.com/ArpitFalcon/zipcodes-in/blob/main/LICENSE)
