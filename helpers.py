import faker
def get_registration_data():
    fake = faker.Faker()
    name = fake.name()
    email = fake.email()
    password = fake.password(length=10)
    return name, email, password