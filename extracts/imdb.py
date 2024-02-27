from source import imdb_endpoint
from bs4 import BeautifulSoup
from urllib.request import Request, urlopen
import json, os


req = Request(imdb_endpoint, headers={'User-Agent': 'XYZ/3.0'})
webpage = urlopen(req, timeout=10).read()
soup = BeautifulSoup(webpage, 'html.parser')

# Variable  to store the movie title and rating information
movie_info = {}
movie_counter = 0

# Find all <li> elements with the specified class
movie_elements = soup.find_all('li', class_='ipc-metadata-list-summary-item sc-1364e729-0 caNpAE cli-parent')

# Iterate through each movie element
for movie in movie_elements:
    movie_counter += 1

    href = movie.find('a', class_='ipc-title-link-wrapper')['href']
    # Extract the IMDb ID from the href attribute
    imdb_id = href.split('/title/')[1].split('/')[0]

    # Extract movie name
    movie_name = movie.find('h3', class_='ipc-title__text').text.strip().split('.')[1].strip()
    movie_name = movie_name.encode('ascii', 'ignore').decode('ascii')
    # print("Movie Name:", movie_name)

    # Extract movie rating
    movie_rating_element = movie.find('span', class_='ipc-rating-star ipc-rating-star--base ipc-rating-star--imdb ratingGroup--imdb-rating')
    if movie_rating_element:
        movie_rating = ''.join(movie_rating_element.find_all(text=True, recursive=False)).strip()
        # print("Movie Rating:", movie_rating)
    else:
        movie_rating = 'N/A'
        # print("Movie Rating: N/A")

    # Extract movie runtime
    runtime_elements = movie.find_all('span', class_='sc-be6f1408-8 fcCUPU cli-title-metadata-item')
    if len(runtime_elements) >= 2:
        movie_runtime = runtime_elements[1].text.strip()
        # print("Movie Runtime:", movie_runtime)
    else:
        movie_runtime = 'N/A'
        # print("Movie Runtime: N/A")
        
    # print('-' * 30)
        
    movie_info[movie_counter] = {'name':movie_name, 'rating':movie_rating, 'runtime':movie_runtime, 'imdb_id':imdb_id}

# print(movie_info)

# Get the directory of the current script
script_dir = os.path.dirname(os.path.abspath(__file__))

# Navigate up the directory structure
parent_dir = os.path.abspath(os.path.join(script_dir, "../"))

# Construct the custom file path
file_path = os.path.join(parent_dir, "output","baseinfo.json")

# Open the file in write mode
with open(file_path, 'w') as file:
    # Write the JSON data to the file
    json.dump(movie_info, file, indent=4)

print("\n\nMovies Data has been saved to", file_path)