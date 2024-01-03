from django.contrib import admin
from .models import Bot,Model,Product,Client1,Client2,Fermer,Late,We,Name,Our,Contact,Lorem,Post,New
# Register your models here.

admin.site.register(Bot)
admin.site.register(Model)
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug":('name',)}
admin.site.register(Client2)
admin.site.register(Client1)
admin.site.register(Fermer)
@admin.register(Late)
class LateAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug":('name',)}
admin.site.register(We)
admin.site.register(Name)
admin.site.register(Our)
admin.site.register(Contact)
admin.site.register(Lorem)
admin.site.register(Post)
admin.site.register(New)



