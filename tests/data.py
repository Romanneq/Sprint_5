import faker
def get_registration_data():
    fake = faker.Faker()
    email = fake.email()
    password = fake.password()
    return email, password