import random
import faker

fake = faker.Faker()

def generate_Data(amount = 1):
    users = []
    for i in range(amount):
        user = {
            "id": random.randint(1000, 9999),
            "first_name": fake.first_name(),
            "last_name": fake.last_name(),
            "email": fake.email(),
            "birth_date": fake.date(),
        }
        users.append(user)
    return users