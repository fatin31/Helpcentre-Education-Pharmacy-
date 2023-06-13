from django.contrib import admin



# Register your models here.
from .models import Cart
from .models import Diabetics
from .models import CheckOut
from .models import Otc
from .models import BabyCare
from .models import WomenChoice
from .models import PersonalCare
from .models import SWellness

class Diabeticsadmin(admin.ModelAdmin):
    list_display=('name','price','quantity')
    
class Otcadmin(admin.ModelAdmin):
    list_display=('name','price','quantity')
    
class BabyCareadmin(admin.ModelAdmin):
    list_display=('name','price','quantity')


class CartModelAdmin(admin.ModelAdmin):
    list_display=('id','user','products','quantity')

class WomenChoiceModelAdmin(admin.ModelAdmin):
    list_display=('id','user','products','quantity')
    
class PersonalCareModelAdmin(admin.ModelAdmin):
    list_display=('id','user','products','quantity')
    
class SwellnessModelAdmin(admin.ModelAdmin):
    list_display=('id','user','products','quantity')

admin.site.register(Diabetics, Diabeticsadmin)
admin.site.register(Cart)
admin.site.register(CheckOut)
admin.site.register(Otc)
admin.site.register(BabyCare)
admin.site.register(WomenChoice)
admin.site.register(PersonalCare)
admin.site.register(SWellness)