import csv
from google_maps import GoogleMaps
class GetDataset:
    @staticmethod
    def getPlacesId():
        places = []

        with open('hotel.csv', newline='') as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=';')
            for row in csv_reader:
                hotel_name = row[0].strip()

                place_id = GoogleMaps.find_place(hotel_name)
                place = [hotel_name, place_id]
                places.append(place)

        with open('places.csv', mode='a', newline='') as places_file:
            place_writer = csv.writer(places_file, delimiter=';', quotechar='"', quoting=csv.QUOTE_MINIMAL)

            for place in places:
                place_writer.writerow(place)
