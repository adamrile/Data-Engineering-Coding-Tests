"""
Programme to provide assistance when searching for the closest desired
court type given a postcode and desired court type using the court tribunal finder API
"""
import csv
import json
import requests

def get_csv_list():
    """Function to create a structured list
    of the csv data found in people.csv"""
    with open('people.csv') as file:
        reader = csv.reader(file)
        next(reader)
        return [list(row) for row in reader]

def fetch_court_data(person_name: str, home_postcode:str, looking_for_court_type:str) -> dict:
    """Function that collects the data that matches the persons postcode to their nearest
    desired court type"""
    url = f"https://courttribunalfinder.service.gov.uk/search/results.json?postcode={home_postcode}"
    response = requests.get(url)
    json_data = response.content
    courts_list = json.loads(json_data)
    for court in courts_list:
        if 'types' in court and court['types'] and court['types'][0] == looking_for_court_type:
            postcode_court = court['addresses'][0]['postcode']
            court_name = court['name']
            distance = court['distance']
            dx_number = court['dx_number'] if 'dx_number' in court else None
            return {"name": person_name, \
                    "court_type": looking_for_court_type, \
                    "court_postcode": postcode_court, \
                    "court_name": court_name, \
                    "dx_number": dx_number, \
                    "distance": distance}

    return "No court in your area that matches your criteria."

if __name__ == "__main__":
    csv_list = get_csv_list()
    for item in csv_list:
        print(fetch_court_data(*item))
