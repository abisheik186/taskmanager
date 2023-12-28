from django.db import models

# Create your models here.
class task_manager_login(models.Model):
    name=models.CharField(max_length=30)
    email=models.EmailField(unique=True)
    password=models.CharField(max_length=30)
class tasks(models.Model):
    title=models.CharField(max_length=30)
    descr=models.TextField()
    duedate=models.DateTimeField()
    priorchoices=[('low' ,'Low'),('medium', 'Medium'),('high','High')]
    prior=models.CharField(max_length=20,choices=priorchoices,default='low')
    user=models.ForeignKey(task_manager_login, on_delete=models.CASCADE)
    statuschoices=[('not completed','not completed'),('completed','completed')]
    status=models.CharField(max_length=30,choices=statuschoices,default='not completed')
    