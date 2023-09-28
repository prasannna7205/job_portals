from django.contrib import admin
from MyJobApp.models import Student,JobTable

class StudentAdmin(admin.ModelAdmin):
    list_display = ['email', 'password']


class JobtableAdmin(admin.ModelAdmin):
    list_display=['jobname','image',"postdescription",'people_required','job_type','salary']

admin.site.register(Student,StudentAdmin)
admin.site.register(JobTable,JobtableAdmin)


