from django.db import models
from ckeditor.fields import RichTextField
# Create your models here.
class Slide(models.Model):
    image = models.ImageField(
        upload_to='slider',
        verbose_name='Картинка'
    )
    title = models.CharField(
        max_length=255,
        verbose_name='название'
    )
    def __str__(self):
        return self.title
    class Meta:
        verbose_name="Cлайд"
        verbose_name_plural = 'Слайды'
        
        
class Parthers(models.Model):
    image = models.ImageField(
        upload_to='pоrtners',
        verbose_name='фотогравия'
    )

    
    class Meta():
        verbose_name= 'партнер',
        verbose_name_plural = 'парнеры'
        
        
class Explanation(models.Model):
    image = models.ImageField(
        upload_to="kwartal_image/",
        verbose_name='фото'
        )
    
    disc = RichTextField(
        verbose_name= 'описание'
    )
    def __str__(self):
        return self.disc
        
    class Meta():
        verbose_name= 'Евро квартал',
        verbose_name_plural = 'Евро кварталы'
        
class Gallery(models.Model):
    image = models.ImageField(
        upload_to="gallery_image/",
        verbose_name='фото'
        )
    

    class Meta():
        verbose_name= 'Галлерия',
        verbose_name_plural = 'Галлерии'
        
class Advantages1(models.Model):
    logo = models.ImageField(
        upload_to="advan_image/",
        verbose_name='фото'
        )
    
    disc = models.TextField(
        verbose_name= 'описание',
        blank=True,null=True
    )
    def __str__(self):
        return self.disc
        
    class Meta():
        verbose_name= 'преймушества 1',
        verbose_name_plural = 'преймушества 1'
        
class Advantages2(models.Model):
    logo = models.ImageField(
        upload_to="advan2_image/",
        verbose_name='фото'
        )
    title = models.CharField(
        max_length=255,
        verbose_name='название'
    )
    disc = models.TextField(
        verbose_name= 'описание',
        blank=True,null=True
    )

    def __str__(self):
        return self.disc
        
    class Meta():
        verbose_name= 'преймушества 2',
        verbose_name_plural = 'преймушества 2'
        