from django.db import models

# Create your models here.
class Course(models.Model):
    name = models.CharField(max_length=255)
    Description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

# class CourseManager(models.Manager):
#     def basic_validator(self, postData):
#         errors = {}
#         # add keys and values to errors dictionary for each invalid field
#         if len(postData['name']) < 5:
#             errors["name"] = "Blog name should be at least 5 characters"
#         if len(postData['Description']) < 15:
#             errors["Description"] = "Blog description should be at least 15 characters"
#         return errors
