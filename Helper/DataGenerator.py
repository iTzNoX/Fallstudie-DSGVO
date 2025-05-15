import random
import faker
import os
import json

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

    project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
    user_data_path = os.path.join(project_root, "Server1", "User_Data")
    os.makedirs(user_data_path, exist_ok=True)

    filepath = os.path.join(user_data_path, "users.json")
    with open(filepath, "w") as f:
        json.dump(users, f, indent=4)

    return users

generate_Data(10)