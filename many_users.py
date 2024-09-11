users = {
    "user1": {
        "name": "John",
        "age": 25,
        "email": "john@example.com",
        "phone": "555-555-5555",
        "address": "123 Main St",
        "city": "Anytown",
        "state": "CA",
        "zipcode": "12345",
        "password": "password",
        "is_admin": False
    },
    "user2": {
        "name": "Jane",
        "age":30,
    }
}


def print_user_info(user):
    try:
        print(f"Name: {user['name']}")
        print(f"Age: {user['age']}")
        print(f"Email: {user['email']}")
        print(f"Phone: {user['phone']}")
        print(f"Address: {user['address']}")
        print(f"City: {user['city']}")
        print(f"State: {user['state']}")
        print(f"Zipcode: {user['zipcode']}")
    except KeyError as e:
        print(f"Warning: Missing key {e} for this user.")


for name, user in users.items():
    # print(f"Name: {user['name']}")
    # print(f"Age: {user['age']}")
    # print(f"Email: {user['email']}")
    # print(f"Phone: {user['phone']}")
    # print(f"Address: {user['address']}")
    # print(f"City: {user['city']}")
    # print(f"State: {user['state']}")
    # print(f"Zipcode: {user['zipcode']}")
    print_user_info(user)
    print("---")
