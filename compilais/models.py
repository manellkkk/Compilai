from django.db import models

# Create your models here.

class User(models.Model):
    idUser = models.AutoField(primary_key=True)
    user_name = models.CharField(unique=True, max_length=12)
    name_complete = models.CharField(max_length=32)
    password = models.CharField(max_length=16)
    email = models.CharField(max_length=40, unique=True)
    date_of_birth = models.DateField()
    premium = models.BooleanField(default=False)

    def __str__(self):
        return self.user_name

class Course(models.Model):
    idCourse = models.AutoField(primary_key=True)
    course_name = models.CharField(max_length=32)
    price = models.FloatField()
    visibility = models.BooleanField(default=True)

    def __str__(self):
        return self.course_name

class UserCourses(models.Model):
    idUserCourses = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="courses")
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name="students")

    class Meta:
        unique_together = ("user", "course")

class Lesson(models.Model):
    idLesson = models.AutoField(primary_key=True)
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name="lessons")
    title = models.CharField(max_length=64)

    def __str__(self):
        return self.title

class UserProgressCourse(models.Model):
    idUserProgress = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="progress")
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE, related_name="users_who_completed")

    class Meta:
        unique_together = ("user", "lesson")

class Certificate(models.Model):
    idCertificate = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.DO_NOTHING)
    date_issued = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"Certificado para {self.user.user_name} - {self.course.course_name}"