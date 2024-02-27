import json, os, pandas as pd



# Get the directory of the current script
script_dir = os.path.dirname(os.path.abspath(__file__))
# Navigate up the directory structure
parent_dir = os.path.abspath(os.path.join(script_dir, "../"))
# Construct the custom file path
output_path = os.path.join(parent_dir, "output")

basefile = os.path.join(output_path, "baseinfo.json")
extrafile = os.path.join(output_path, "extrainfo.json")


base_data = {}
extra_data = {}

# Open the file in read mode
with open(basefile, 'r') as file:
    # Load the JSON data into a Python dictionary
    base_data = json.load(file)

# Open the file in read mode
with open(extrafile, 'r') as file:
    # Load the JSON data into a Python dictionary
    extra_data = json.load(file)


# print(base_data)
# print("\n\n")
# print(extra_data)

'''
{
    1 : {
            'Movie Title':None,
            'Director':None,
            'Writer':None,
            'IMDB Rating':None,
            'Runtime':None,
            'Genre':None,
            'Country':None, 
            'Year':None,
            'Language':None,
        }
}
'''

movies_info = {}

for eachmov in range(1,250):
    # print(extra_data[str(eachmov)])
    # print(base_data[str(eachmov)])
    prebase = {'title':None,'director':None,'writer':None,'rating':None,'runtime':None,'genre':None,'country':None,'year':None,'language':None}
    prebase['title'] = extra_data[str(eachmov)]['Title']
    prebase['rating'] = base_data[str(eachmov)]['rating']
    prebase['runtime'] = base_data[str(eachmov)]['runtime']
    prebase['director'] = extra_data[str(eachmov)]['Director']
    prebase['writer'] = extra_data[str(eachmov)]['Writer']
    prebase['genre'] = extra_data[str(eachmov)]['Genre']
    prebase['year'] = extra_data[str(eachmov)]['Year']
    prebase['language'] = extra_data[str(eachmov)]['Language']
    prebase['country'] = extra_data[str(eachmov)]['Country']
    movies_info[eachmov] = prebase


# Get the directory of the current script
script_dir = os.path.dirname(os.path.abspath(__file__))
# Navigate up the directory structure
parent_dir = os.path.abspath(os.path.join(script_dir, "../"))
# Construct the custom file path
file_path = os.path.join(parent_dir, "output","movies.json")

# Open the file in write mode
with open(file_path, 'w') as file:
    # Write the JSON data to the file
    json.dump(movies_info, file, indent=4)

print("\nMovies Data has been saved to", file_path)