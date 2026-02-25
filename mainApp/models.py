from django.db import models

class AUser(models.Model):
    id=models.AutoField(primary_key=True)
    IdNumber=models.TextField()
    phonenumber=models.TextField()
    password=models.TextField()

class Tennant(models.Model):
    Name=models.TextField(null=True)
    Tennantid=models.AutoField(primary_key=True)
    userid=models.OneToOneField(AUser, on_delete=models.CASCADE)

class Owner(models.Model):
    OwnerId=models.AutoField(primary_key=True)
    Name=models.TextField()
    userid=models.OneToOneField(AUser, on_delete=models.CASCADE)

class House(models.Model):
    file=models.FileField(upload_to='media/properties')
    PropertyId=models.AutoField(primary_key=True)
    Location = models.CharField(max_length=30)
    Density = models.CharField(max_length=30)
    Rooms=models.IntegerField(default=1)
    Features=models.TextField(default="")
    ownerId=models.ForeignKey(Owner, null=True, on_delete=models.CASCADE)
    Avilability=models.BooleanField(default=False)
    Price=models.IntegerField(null=True)

