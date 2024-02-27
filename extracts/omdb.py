from source import omdb_endpoint
from bs4 import BeautifulSoup
from urllib.request import Request, urlopen
import json, os, requests



# Get the directory of the current script
script_dir = os.path.dirname(os.path.abspath(__file__))

# Navigate up the directory structure
parent_dir = os.path.abspath(os.path.join(script_dir, "../"))

# Construct the custom file path
file_path = os.path.join(parent_dir, "output","baseinfo.json")

# Open the file in read mode
with open(file_path, 'r') as file:
    # Load the JSON data into a Python dictionary
    data = json.load(file)

movie_extra_info = {}

for counter in range(1,250):
    movie_id = data[str(counter)]['imdb_id']
    searchterm = "i={0}".format(movie_id)
    url = omdb_endpoint+searchterm
    # print("Querying ...", url)
    # Make the GET request
    response = requests.get(url)

    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        # Parse the JSON response
        extra_info = response.json()
        movie_extra_info[str(counter)] = extra_info
    else:
        print("Failed to fetch data from API")


# Get the directory of the current script
script_dir = os.path.dirname(os.path.abspath(__file__))

# Navigate up the directory structure
parent_dir = os.path.abspath(os.path.join(script_dir, "../"))

# Construct the custom file path
file_path = os.path.join(parent_dir, "output","extrainfo.json")

# Open the file in write mode
with open(file_path, 'w') as file:
    # Write the JSON data to the file
    json.dump(movie_extra_info, file, indent=4)

print("\nMovies Extra Data has been saved to", file_path)