from faker import Faker
import csv

fake = Faker()

with open('sample_data.csv', 'w', newline='') as csvfile:
    fieldnames = ['name', 'email', 'phone_number', 'address']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

    writer.writeheader()
    for _ in range(100):   # This generates 100 rows of data
        writer.writerow({
            'name': fake.name(),
            'email': fake.email(),
            'phone_number': fake.phone_number(),
            'address': fake.address()
        })

# Using below code to generate phone_number for a pecific country code

# def generate_phone_number():
#     return "+234" + fake.random_number(digits=10)

# with open('sample_data.csv', 'w', newline='') as csvfile:
#     fieldnames = ['name', 'email', 'phone_number', 'address']
#     writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

#     writer.writeheader()
#     for _ in range(100):   # This generates 100 rows of data
#         writer.writerow({
#             'name': fake.name(),
#             'email': fake.email(),
#             'phone_number': generate_phone_number(),
#             'address': fake.address()
#         })