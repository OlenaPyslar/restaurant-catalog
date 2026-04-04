from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from catalog.models import DishType, Dish, Cooker


@admin.register(Dish)
class DishAdmin(admin.ModelAdmin):
    list_display = ["name", "price", "dish_type", ]
    list_filter = ["dish_type", ]
    search_fields = ["name", ]


@admin.register(Cooker)
class CookerAdmin(UserAdmin):
    list_display = UserAdmin.list_display + ("years_of_experience", )
    fieldsets = UserAdmin.fieldsets + (("Addition info", {"fields": ("years_of_experience",)}),)
    add_fieldsets = (UserAdmin.add_fieldsets +
                     (("Addition info",
                       {"fields":
                            ("first_name", "last_name", "years_of_experience",)
                        }),))


admin.site.register(DishType)
