from django.contrib import admin

# Register your models here.
from MylinebotApp.models import * #MylinebotApp改成自己綠色的資料夾

# class User_Info_Admin(admin.ModelAdmin):
#     list_display = ('uid','name','pic_url','mtext','mdt')
# admin.site.register(User_Info,User_Info_Admin)

class users_Admin(admin.ModelAdmin):
    list_display = ('u_id','u_name','u_latitude','u_longtitude','u_address','u_role', 'u_give')
admin.site.register(users,users_Admin)

class favor_shop_Admin(admin.ModelAdmin):
    list_display = ('u_id','s_category')
admin.site.register(favor_shop,favor_shop_Admin)

class favor_time_Admin(admin.ModelAdmin):
    list_display = ('u_id','f_time')
admin.site.register(favor_time,favor_time_Admin)

class favor_food_Admin(admin.ModelAdmin):
    list_display = ('u_id','m_group')
admin.site.register(favor_food,favor_food_Admin)

class shops_Admin(admin.ModelAdmin):
    list_display = ('s_id','s_name','u_id','s_category','s_address','s_latitude', 's_longtitude','s_openday','s_start_time','s_end_time', 's_level', 's_city')
admin.site.register(shops,shops_Admin)

class meals_Admin(admin.ModelAdmin):
    list_display = ('m_name','s_id','m_group','m_price', 'm_quantity')
admin.site.register(meals,meals_Admin)

class mapping_Admin(admin.ModelAdmin):
    list_display = ('ru_id','gu_id','stat')
admin.site.register(mapping,mapping_Admin)

class food_id_Admin(admin.ModelAdmin):
    list_display = ('m_id','m_name')
admin.site.register(food_id,food_id_Admin)

class family_shops_Admin(admin.ModelAdmin):
    list_display = ('s_id','s_name')
admin.site.register(family_shops,family_shops_Admin)

