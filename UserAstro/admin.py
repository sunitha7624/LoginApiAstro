from django.contrib import admin
from .models import *
# Register your models here.

class Natal_First_Time_TableAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Natal_First_Time_Table._meta.get_fields()]
    list_editable = list_display[1:]
    
class User_Registration_TableAdmin(admin.ModelAdmin):
    list_display = [field.name for field in User_Registration_Table._meta.get_fields()]
    list_editable = list_display[1:] 
    
class User_Setting_TableAdmin(admin.ModelAdmin):
    list_display = [field.name for field in User_Setting_Table._meta.get_fields()]
    list_editable = list_display[1:]        
    
    
admin.site.register(Natal_First_Time_Table, Natal_First_Time_TableAdmin)
admin.site.register(User_Registration_Table, User_Registration_TableAdmin)   
admin.site.register(User_Setting_Table, User_Setting_TableAdmin)    


