from faker import Faker

faker = Faker()


def random_mes():
    return f"Hello, {faker.first_name()}"
