from django.db import models

# Create your models here.
class User(models.Model):
    email = models.CharField(max_length=100)
    password = models.TextField(max_length=500)
    status = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(null=True, blank=True)
    #------------------------------------------------------------------------------------------
# modelo tipos de identificacion
class IdentificationType(models.Model):
    name = models.CharField(max_length=50)
    abrev = models.CharField(max_length=10)
    descrip = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(null=True, blank=True)

#------------------------------------------------------------------------------------------
# modelo condados
class Country(models.Model):
    name = models.CharField(max_length=100)
    abrev = models.CharField(max_length=10)
    descrip = models.CharField(max_length=10)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(null=True, blank=True)

#------------------------------------------------------------------------------------------
# modelo departamentos
class Department(models.Model):
    name = models.CharField(max_length=100)
    abrev = models.CharField(max_length=10)
    descrip = models.CharField(max_length=10)
    id_country = models.ForeignKey(
        Country,
        on_delete=models.PROTECT,
        db_column='id_country'
    ) 
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(null=True, blank=True)

#------------------------------------------------------------------------------------------
# modelo ciudades
class City(models.Model):
    name = models.CharField(max_length=100)
    abrev = models.CharField(max_length=10)
    descrip = models.CharField(max_length=10)
    id_dept = models.ForeignKey(
        Department,
        on_delete=models.PROTECT,
        db_column='id_dept'
    ) 
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(null=True, blank=True)

#------------------------------------------------------------------------------------------ 
# modelo personas
class Person(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    id_ident_type = models.ForeignKey( 
        IdentificationType,  
        on_delete=models.PROTECT,
        db_column='id_ident_type'
    )
    ident_number = models.CharField(max_length=15)
    id_exp_city = models.ForeignKey( 
        City, 
        on_delete=models.PROTECT,
        db_column='id_exp_city'
    )
    address = models.CharField(max_length=150)
    mobile = models.CharField(max_length=50)
    id_user = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(null=True, blank=True)

#------------------------------------------------------------------------------------------
# modelo estudiantes 
class Student(models.Model):
    code = models.CharField(max_length=50)
    id_person = models.ForeignKey(
        Person,
        on_delete=models.PROTECT,
        db_column='id_person'
    )
    status = models.BooleanField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(null=True, blank=True)

