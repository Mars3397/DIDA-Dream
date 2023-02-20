from django.db import models

# Create your models here.
# class User_Info(models.Model):
#     uid = models.CharField(max_length=50,null=False,default='')         #user_id
#     name = models.CharField(max_length=255,blank=True,null=False)       #LINE名字
#     pic_url = models.CharField(max_length=255,null=False)               #大頭貼網址
#     mtext = models.CharField(max_length=255,blank=True,null=False)      #文字訊息紀錄
#     mdt = models.DateTimeField(auto_now=True)                           #物件儲存的日期時間
#                            #物件儲存的日期時間

#     def __str__(self):
#         return self.uid

class users(models.Model):
    u_id = models.CharField(max_length=256, default='')
    u_name = models.CharField(max_length=256, default='')
    u_latitude = models.FloatField(default=0)
    u_longtitude = models.FloatField(default=0)
    u_address = models.CharField(max_length=256, default='')
    u_role = models.CharField(max_length=3, default='u')
    u_give = models.IntegerField(default=0)
    u_result = models.CharField(max_length=10, default='')

class favor_shop(models.Model):
    u_id = models.CharField(max_length=256, null=False, default='')
    s_category = models.CharField(max_length=256, null=False, default='')

class favor_time(models.Model):
    u_id = models.CharField(max_length=256, null=False, default='')
    f_time = models.IntegerField(null=False, default=0)

class favor_food(models.Model):
    u_id = models.CharField(max_length=256, null=False, default='')
    m_group = models.CharField(max_length=256, null=False, default='')

class shops(models.Model):
    s_id = models.IntegerField(null=False, default=0)
    s_name = models.CharField(max_length=256, null=False, default='')
    u_id = models.CharField(max_length=256, null=False, default='')
    s_category = models.CharField(max_length=256, null=False, default='')
    s_address = models.CharField(max_length=256, default='')
    s_latitude = models.FloatField(null=False, default=0)
    s_longtitude = models.FloatField(null=False, default=0)
    s_openday = models.CharField(max_length=256, default='')
    s_start_time = models.IntegerField(default=0)
    s_end_time = models.IntegerField(default=0)
    s_level = models.CharField(max_length=256, default='')
    s_city = models.CharField(max_length=256, default='')

class meals(models.Model):
    m_name = models.CharField(max_length=256, null=False, default='')
    s_id = models.CharField(max_length=256, null=False, default='')
    m_group = models.CharField(max_length=256, null=False, default='')
    m_price = models.IntegerField(null=False, default=0)
    m_quantity = models.IntegerField(null=False, default=0)

class mapping(models.Model):
    ru_id = models.CharField(max_length=256, default='')
    gu_id = models.CharField(max_length=256, default='')
    stat = models.CharField(max_length=256, default='')

class food_id(models.Model):
    m_id = models.CharField(max_length=256, default='')
    m_name = models.CharField(max_length=256, default='')

class family_shops(models.Model):
    s_id = models.CharField(max_length=256, default='')
    s_name = models.CharField(max_length=256, default='')




