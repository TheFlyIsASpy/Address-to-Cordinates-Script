from pygeocoder import Geocoder
skip = input("Skip first line?: y/n (default no)\n")
if skip == "y":
    skip = True
else:
    skip = False
GeocoderApi = input("Please enter a Geocoder API key from the google cloud console: \n")
f = open("addresses.txt","a+")
r = open("cordinates.txt","w+")
previous = ""
f.seek(0)
for line in f:
    if skip:
        skip = False
        continue
    else:
        if line != previous:
            r.write(str(Geocoder(GeocoderApi).geocode(line).coordinates))
            r.write("\n")
            previous = line
            print("Calculating cordinates for: " + line)
print("Done. No more addresses to consider")
f.close
r.close
