from django.contrib import admin
from compilais.models import *

# Register your models here.

admin.site.register(User)
admin.site.register(Course)
admin.site.register(UserCourses)
admin.site.register(Lesson)
admin.site.register(UserProgressCourse)
admin.site.register(Certificate)