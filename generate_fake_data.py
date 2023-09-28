# from django.core.management.base import BaseCommand
# from faker import Faker
# from MyJobApp.models import JobTable
# from django.core.files import File
# import os

# class Command(BaseCommand):
#     help = 'Generate fake data for JobTable'

#     def handle(self, *args, **kwargs):
#         # Your code for generating fake data goes here
#         fake = Faker()
#         media_path = 'media/job_images/'

#         for _ in range(10):  # Generate data for 10 job entries (you can change the number as needed)
#             jobname = fake.job()
#             image_filename = 'image.jpg'  # Replace with the actual image filename
#             postdescription = fake.text()
#             people_required = fake.random_int(min=1, max=100)
#             job_type = fake.word()
#             salary = fake.random_int(min=20000, max=100000)  # Adjust salary range as needed

#             # Create a JobTable instance with the image
#             job = JobTable.objects.create(
#                 jobname=jobname,
#                 postdescription=postdescription,
#                 people_required=people_required,
#                 job_type=job_type,
#                 salary=salary
#             )

#             # Open the image file and assign it to the image field
#             with open(os.path.join(media_path, image_filename), 'rb') as f:
#                 job.image.save(image_filename, File(f))

#             job.save()
