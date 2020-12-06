from django.db import models

class Size(models.Model):
    title = models.CharField(max_length=100,default='Small')
    def __str__(self):
        return self.title

class Toppings(models.Model):
    name1 = models.CharField(max_length=140,default='Onion')
    def __str__(self):
        return self.name1

class UserToppings(models.Model):
    name_user = models.CharField(max_length=140)
    def __str__(self):
        return self.name_user

class UserSize(models.Model):
    name_size = models.CharField(max_length=140)
    def __str__(self):
        return self.name_size

class Types(models.Model):
    type = models.CharField(max_length=140,default='Square')
    def __str__(self):
        return self.type

class Pizza(models.Model):
    toppings = models.ForeignKey(Toppings,on_delete=models.CASCADE)
    types = models.ForeignKey(Types,on_delete=models.CASCADE)
    size = models.ForeignKey(Size,on_delete=models.CASCADE)

class UserForm(models.Model):
    user_toppings = models.ForeignKey(UserToppings,on_delete=models.CASCADE)
    user_size = models.ForeignKey(UserSize,on_delete=models.CASCADE)