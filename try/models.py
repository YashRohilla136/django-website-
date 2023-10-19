from django.db import models

class Contact(models.Model):
    name=models.CharField(max_length=50)
    email=models.EmailField()
    phonenumber=models.CharField(max_length=12)
    description=models.TextField()

    def __str__(self):
        return f'Message from {self.name}'


class Blogs(models.Model):
    title=models.CharField( max_length=100)
    describtion=models.TextField()
    authname=models.CharField(max_length=50)
    img=models.ImageField(upload_to='pics',blank=True,null=True)
    timestamp=models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return f'Upploded by  {self.authname}'