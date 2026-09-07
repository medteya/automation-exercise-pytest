from faker import Faker

fake = Faker()

class DataGenerator:
    @staticmethod
    def get_user_registration_data():
        return {
            "name": fake.name(),
            "email": fake.email(),
            "password": fake.password(length=10, special_chars=True, digits=True, upper_case=True),
            "first_name": fake.first_name(),
            "last_name": fake.last_name(),
            "company": fake.company(),
            "address1": fake.street_address(),
            "address2": "Apt 4B",
            "country": "Canada",
            "state": fake.state(),
            "city": fake.city(),
            "zipcode": "K1P 1J1",
            "mobile": fake.numerify("##########")
        }
    
    @staticmethod
    def get_invalid_credentials():
        return {
            "email": fake.email(),
            "password": fake.password()
        }