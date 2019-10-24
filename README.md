# Address-to-Cordinates-Script
Takes in a txt file of addresses and a google geocoder API key. Outputs a txt file with geographic cordinates.


To use this script.
pygeocoder must be installed with pip install pygeocoder
You need an api key from google cloud, either a general one or a geocoder one.
Place addresses on each line of a text file named addresses.txt. If the file doesn't exist, one will be generated when you run the file.
The first line of the addresses.txt is skippable when running the file.
If there is a REQUEST_DENIED error, follow the query link at the end of the error, and you will be able to see the api error.
