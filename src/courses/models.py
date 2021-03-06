from django.db import models
from django.contrib.postgres.fields import JSONField

# Create your models here.
class Course(models.Model):
    FALL = 'Fall'
    SPRING = 'Spring'
    BOTH = 'Both'

    SEMESTER_CHOICES = ((FALL, 'Fall'),(SPRING,'Spring'),(BOTH, 'Both'))

    courseID = models.PositiveSmallIntegerField()
    courseDept = models.CharField(max_length=4)
    name = models.CharField(max_length=100)
    prereqCount = models.PositiveSmallIntegerField()
    coreqCount = models.PositiveSmallIntegerField(default=0)
    category = models.CharField(max_length=50)
    hours = models.PositiveSmallIntegerField()
    semester = models.CharField(max_length=10, choices=SEMESTER_CHOICES, default=BOTH)
    description = models.TextField()

    def __str__(self):
        return (self.courseDept + " " + str(self.courseID) + ": " +  self.name)

class Prereq(models.Model):
        courseID = models.PositiveSmallIntegerField()
        courseDept = models.CharField(max_length=4)
        prereqCourses = JSONField()

        def __str__(self):
            return self.courseDept + ' ' + str(self.courseID) 

            ## delete migrations table
            ## make the models according to the attributes of the course table