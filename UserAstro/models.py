from django.db import models

# Create your models here.

class  Natal_First_Time_Table(models.Model):
    S_No = models.IntegerField(default=0, verbose_name='Serial No.')
    name  = models.CharField(default='', max_length=100, db_column='Name ', verbose_name='Name')
    gender = models.CharField(default='', max_length=100, db_column='gender', verbose_name='gender')
    father_name = models.CharField(default='', max_length=100, db_column='father name', verbose_name='father name')
    mother_name = models.CharField(default='', max_length=100, db_column='mother name', verbose_name='mother name')
    dob = models.CharField(default='', max_length=50, db_column='dob', verbose_name='dob')
    time  = models.CharField(default='', max_length=100, db_column='time ', verbose_name='time')
    location_search_input_lord = models.CharField(default='', max_length=200, db_column='location-search-input', verbose_name='location-search-input')
    timezone = models.CharField(default='', max_length=100, db_column='Time Zone', verbose_name='Time Zone')
    dst = models.CharField(default='', max_length=100, db_column='DST', verbose_name='DST')
    date1 = models.CharField(default='', max_length=100, db_column='BTR Date and Time', verbose_name='BTR Date and Time')
    currentaddress = models.CharField(default='', max_length=200, db_column='BTR Place', verbose_name='BTR Place')
    

    class Meta:
        verbose_name = '100. Table Name: Natal First Time Table (Table Code:100)'
        verbose_name_plural = '100. Table Name:  Natal First Time Table (Table Code:100)'
        
class  User_Registration_Table(models.Model):
   
    name  = models.CharField(default='', max_length=100, db_column='name ', verbose_name='name')
    city = models.CharField(default='', max_length=100, db_column='city', verbose_name='city')
    mobile_number = models.CharField(default='', max_length=100, db_column='mobile number', verbose_name='mobile_number')
    Email = models.CharField(default='', max_length=100, db_column='Email', verbose_name='Email')
    Password = models.CharField(default='', max_length=50, db_column='password', verbose_name='password')
    Forgot_password  = models.CharField(default='', max_length=100, db_column='forgot password ', verbose_name='forgot password')
    Reset_password = models.CharField(default='', max_length=200, db_column='reset password', verbose_name='reset password')
   
    class Meta:
        verbose_name = '100. Table Name: User_Registration_Table (Table Code:101)'
        verbose_name_plural = '100. Table Name:  User_Registration_Table (Table Code:101)'
        
        
class  User_Setting_Table(models.Model):
   
    graphtype = models.CharField(default='', max_length=100, db_column='graphtype', verbose_name='graphtype')
    language = models.CharField(default='', max_length=100, db_column='language', verbose_name='language')
    color  = models.CharField(default='', max_length=100, db_column='color', verbose_name='color')
    font_size= models.CharField(default='', max_length=200, db_column='font-size', verbose_name='font-size')
    bgColor  = models.CharField(default='', max_length=100, db_column='bgColor', verbose_name='bgColor')
    chartColor  = models.CharField(default='', max_length=100, db_column='chartColor', verbose_name='chartColor')
    glyphColor  = models.CharField(default='', max_length=100, db_column='glyphColor', verbose_name='glyphColor')
   
    class Meta:
        verbose_name = '100. Table Name: User_Setting_Table (Table Code:101)'
        verbose_name_plural = '100. Table Name:  User_Setting_Table (Table Code:101)'                   
        
        
        
        