import csv
import re
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

        with open('places.csv', mode='a', newline='', encoding='utf-8') as places_file:
            place_writer = csv.writer(places_file, delimiter=';', quotechar='"', quoting=csv.QUOTE_MINIMAL)

            for place in places:
                place_writer.writerow(place)

    @staticmethod
    def getPlacesReviews():
        places_reviews = []

        with open('hotel_id3.csv', newline='') as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=';')
            for row in csv_reader:
                place_id = row[1].strip()

                reviews = GoogleMaps.getPlaceReviews(place_id)
                for review in reviews:
                    text_review = re.sub(r'\r\n|\r|\n', ' ', review["text"])
                    place_review = [place_id, text_review, review["rating"]]

                    places_reviews.append(place_review)

        with open('hotel_reviews3.csv', mode='a', newline='', encoding='utf-8') as places_file:
            place_writer = csv.writer(places_file, delimiter=';', quotechar='"', quoting=csv.QUOTE_MINIMAL)

            for place in places_reviews:
                place_writer.writerow(place)

GetDataset.getPlacesReviews()