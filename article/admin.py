from django.contrib import admin
from .models import Article,Reporter

class ArticleAdmin(admin.ModelAdmin):
        list_display=['heading','body','image','created','reporter']
        search_fields=['heading','created','reporter__name']

admin.site.register(Article,ArticleAdmin)

class Reporterid(admin.ModelAdmin):
        list_display=['name','id']
        search_fields=['name']       
admin.site.register(Reporter,Reporterid)
# Register your models here.
