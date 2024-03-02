from dataclasses import dataclass
from typing import List

import faker
import datetime

fake = faker.Faker('uk_UA')

@dataclass
class RestaurantReview:
    id: int
    restaurant_name: str
    review_name: str
    review_text: str
    rating: int
    date_of_visit: datetime.date
    location: str


def generate_restraunt_reviews() -> List[RestaurantReview]:
    reviews = []

    for i in range(500):

        review = RestaurantReview(
            id=i,
            restaurant_name=fake.word(ext_word_list=['Rich', 'True Price', 'Bulvar', 'New Province', 'McDonald`s', 'KFC', 'Fabric`s', 'Pancake', 'Chelentano', 'Marine', 'Familia', 'Parla', 'Paris']),
            review_name=fake.text(max_nb_chars=20),
            review_text=fake.text(max_nb_chars=100),
            rating=fake.random_int(min=1, max=5),
            date_of_visit=fake.date_between(datetime.datetime.now() - datetime.timedelta(days=730), datetime.datetime.now()),
            location=fake.city_name()
        )
        reviews.append(review)

    return reviews


def save_restrauntreviews_to_csv(reviews: List[RestaurantReview]):
    with open('reviews.csv', 'w', encoding="utf-8") as f:
        f.write('id,restaurant_name,review_name,review_text,rating,date_of_visit,location\n')

        for review in reviews:
            f.write(f'{review.id},{review.restaurant_name},{review.review_name},{review.review_text},{review.rating},{review.date_of_visit},{review.location}\n')


if __name__ == '__main__':
    reviews = generate_restraunt_reviews()
    save_restrauntreviews_to_csv(reviews)