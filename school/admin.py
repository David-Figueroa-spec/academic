from django.contrib import admin

# Register your models here.
from .models import Country, Department, City, IdentificationType, User, Person, Student
 
 
@admin.register(Country)
class CountryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'abrev', 'descrip', 'created_at')
    search_fields = ('name', 'abrev')
    list_per_page = 20
 
 
@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'abrev', 'descrip', 'id_country', 'created_at')
    search_fields = ('name', 'abrev')
    list_filter = ('id_country',)
    list_per_page = 20
 
 
@admin.register(City)
class CityAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'abrev', 'descrip', 'id_dept', 'created_at')
    search_fields = ('name', 'abrev')
    list_filter = ('id_dept',)
    list_per_page = 20
 
 
@admin.register(IdentificationType)
class IdentificationTypeAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'abrev', 'descrip', 'created_at')
    search_fields = ('name', 'abrev')
    list_per_page = 20
 
 
@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'email', 'status', 'created_at')
    search_fields = ('email',)
    list_filter = ('status',)
    list_per_page = 20
 
 
@admin.register(Person)
class PersonAdmin(admin.ModelAdmin):
    list_display = ('id', 'first_name', 'last_name', 'id_ident_type', 'ident_number', 'mobile', 'created_at')
    search_fields = ('first_name', 'last_name', 'ident_number')
    list_filter = ('id_ident_type',)
    list_per_page = 20
 
 
@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('id', 'code', 'id_person', 'status', 'created_at')
    search_fields = ('code',)
    list_filter = ('status',)
    list_per_page = 20