from django.db import models

# Create your models here.
class Topic(models.Model):
    Topic_Name=models.CharField(max_length=2000)
    def __str__(self):
        return self.Topic_Name

class Webpage(models.Model):
    Topic_Name=models.ForeignKey(Topic,on_delete=models.CASCADE)
    Name=models.CharField(max_length=2000)
    Url=models.URLField()
    Email=models.EmailField(default='india@gmail.com')
    Reenter_Email=models.EmailField(default='india@gmail.com')

    def __str__(self):
        return self.Name

class AccessRecord(models.Model):
    Name=models.ForeignKey(Webpage,on_delete=models.CASCADE)
    Date=models.DateField()
    Author=models.CharField(max_length=100)
    def __str__(self):
        return self.Author

