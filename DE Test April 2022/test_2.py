import csv
import json
import requests


def fetch_court_data(person_name: str, home_postcode:str, looking_for_court_type:str) -> dict:
    url = f"https://courttribunalfinder.service.gov.uk/search/results.json?postcode={home_postcode}"
    response = requests.get(url)
    json_data = response.content
    obj = json.loads(json_data)
    postcode_court = obj[0]['addresses'][0]['postcode']
    court_name = obj[0]['name']
    distance = obj[0]['distance']
    dx_number = obj[0]['dx_number'] if 'dx_number' in obj[0] else None
    return {"name": person_name, "court_type": looking_for_court_type, "court_postcode": postcode_court,
            "court_name": court_name, "dx_number": dx_number, "distance": distance}


if __name__ == "__main__":
    with open('people.csv') as f:
        reader = csv.reader(f)
        next(reader)
        csv_list = [list(row) for row in reader]
    for item in csv_list:
        dict = fetch_court_data(*item)
        print(dict)

