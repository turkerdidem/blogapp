from django.db import models
from ckeditor.fields import RichTextField

import article
# Create your models here.

class Article(models.Model):
    author = models.ForeignKey("auth.User", on_delete=models.CASCADE, verbose_name="Yazar") #User silindiği zaman o user'a ait article'lar da silinecek.
    title = models.CharField(max_length = 50, verbose_name="Başlık")
    content = RichTextField(verbose_name="İçerik")
    created_date = models.DateTimeField(auto_now_add=True, verbose_name="Oluşturulma Tarihi")
    article_image = models.FileField(blank=True, null=True, verbose_name="Makaleye Fotoğraf Ekleyin")
    def __str__(self): #Bu method'u admin panelindeki article'ların görünüşlerini düzenlemek için kullanıyoruz, burada yalnızca title(Deneme 1) yaptık.
        return self.title

    class Meta:
        ordering = ['-created_date']

class Comment(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE, verbose_name="Makale", related_name="comments")
    comment_author = models.CharField(max_length=50, verbose_name="İsim")
    comment_content = models.CharField(max_length=200, verbose_name="Yorum")
    comment_date = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.comment_content

    class Meta:
        ordering = ['-comment_date']