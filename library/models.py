from django.db import models

# Create your models here.
class Books(models.Model):
    # PK
    id_book = models.AutoField(primary_key=True, editable=False)

    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    release_year = models.IntegerField()
    state = models.CharField(max_length=50)
    pages = models.IntegerField()
    publishing_company = models.CharField(max_length=255)
    created_at = models.DateField(auto_now_add=True)

    def __str__(self):
        return f'Instância: {self.title} da Entidade: {self.__class__.__name__}'
    