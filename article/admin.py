from django.contrib import admin

from .models import Article, Comment

# Register your models here.

admin.site.register(Comment)

@admin.register(Article) #Decorator yarattık.
class ArticleAdmin(admin.ModelAdmin):

    list_display = ["title", "author", "created_date"]

    list_display_links = ["title", "created_date"]

    search_fields = ["title"] #Title bilgisine göre arama özelliği ekledik.

    list_filter = ["created_date"] #Tarihe göre arama yapmak için filtre oluşturduk.

    class Meta: #Python'da class içinde class yazılabiliyor.
        model = Article #Article modeline göre özelleştirme