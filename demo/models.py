from django.db import models

class Category(models.Model):
	category_id = models.AutoField(primary_key=True)
	category_name = models.CharField(max_length=40)

	def __str__(self):
		return str(self.category_id)


class Category_details(models.Model):
    cat= models.ForeignKey(Category, null=True,blank=True)
    category_address = models.CharField(max_length=40)
    category_phonenumber=models.IntegerField()

    def __str__(self):
		return self.category_address

class Service(models.Model):
    cat= models.ForeignKey(Category_details, null=True,blank=True)
    service_id = models.AutoField(primary_key=True)
    service_name=models.CharField(max_length=40)  

    def __str__(self):
		return self.service_name