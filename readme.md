# Using with  desktop:
1. Make sure you have puthon 3.7 and above
2. download this repository and make sure you have following liberaries - 
```
pip3 install argparse
pip3 install requests
pip3 install json
pip3 install datetime
```
3. through terminal go to the folder where the files are and run ` python3 findSlots.py --h `, you will get followign output
```
usage: findSlots.py [-h] pincode {18,45}

positional arguments:
  pincode     Pincode of your location
  {18,45}     Age limit, choose for 18 or 45

optional arguments:
  -h, --help  show this help message and exit
  ```
  4. now call the function once agian with the arguments ` python3 findSlots.py 313001 45 ` 
  if there are slots available it will show you the list else the function will exit.
  ```
  ['06-06-2021', 'Jagdish Chowk UPHC', 'Free', 45, 'COVISHIELD', ['10:00AM-11:00AM', '11:00AM-12:00PM', '12:00PM-01:00PM', '01:00PM-04:00PM'], 49]
['06-06-2021', 'Dhanmandi UPHC', 'Free', 45, 'COVAXIN', ['10:00AM-11:00AM', '11:00AM-12:00PM', '12:00PM-01:00PM', '01:00PM-04:00PM'], 17]
['06-06-2021', 'SSB RNT Medical College', 'Free', 45, 'COVISHIELD', ['10:00AM-11:00AM', '11:00AM-12:00PM', '12:00PM-01:00PM', '01:00PM-04:00PM'], 47]
['06-06-2021', 'Bacchar PHC', 'Free', 45, 'COVISHIELD', ['09:00AM-10:00AM', '10:00AM-11:00AM', '11:00AM-12:00PM', '12:00PM-04:30PM'], 20]
['06-06-2021', 'G.S.S.S. SAVINA', 'Free', 45, 'COVISHIELD', ['09:00AM-10:00AM', '10:00AM-11:00AM', '11:00AM-12:00PM', '12:00PM-04:30PM'], 14]
['06-06-2021', 'Bhuwana Urban CHC', 'Free', 45, 'COVAXIN', ['10:00AM-11:00AM', '11:00AM-12:00PM', '12:00PM-01:00PM', '01:00PM-04:00PM'], 14]
['06-06-2021', 'Manchla Magra UPHC', 'Free', 45, 'COVISHIELD', ['10:00AM-11:00AM', '11:00AM-12:00PM', '12:00PM-01:00PM', '01:00PM-04:00PM'], 42]
['06-06-2021', 'Fatehpura UPHC', 'Free', 45, 'COVISHIELD', ['10:00AM-11:00AM', '11:00AM-12:00PM', '12:00PM-01:00PM', '01:00PM-04:00PM'], 43]
['06-06-2021', 'UPHC Bhopalpura', 'Free', 45, 'COVAXIN', ['10:00AM-11:00AM', '11:00AM-12:00PM', '12:00PM-01:00PM', '01:00PM-04:00PM'], 44]
['06-06-2021', 'Ayad UPHC', 'Free', 45, 'COVAXIN', ['10:00AM-11:00AM', '11:00AM-12:00PM', '12:00PM-01:00PM', '01:00PM-04:00PM'], 12]
['06-06-2021', 'Satelite Hospital Chandpol', 'Free', 45, 'COVISHIELD', ['10:00AM-11:00AM', '11:00AM-12:00PM', '12:00PM-01:00PM', '01:00PM-04:00PM'], 45]
```


# Using in app
1. Directly use finderlogic.py in your app