from django.db import models

# Create your models here.

class Kategori(models.Model): 
    nama = models.CharField(max_length = 50)

    def __str__(self):
        return self.nama

    class Meta: 
        verbose_name_plural = "Kategori"

class Artikel(models.Model):  
    nama_tempat = models.CharField(max_length = 150) 
    body = models.TextField()
    lokasi = models.TextField() 
    kategory = models.ForeignKey(Kategori , on_delete = models.CASCADE) 
    img = models.FileField(upload_to='img', blank=True, null=True)
    published = models.BooleanField(default=True)

    def __str__(self): 
        return "{} - {}".format(self.nama_tempat, self.kategory) 

    class Meta: 
        verbose_name_plural = "Artikel"

