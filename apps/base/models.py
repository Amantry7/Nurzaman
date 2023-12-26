from django.db import models
from ckeditor.fields import RichTextField
# Create your models here.



class Settings(models.Model):
    title = models.CharField(
        max_length=255,
        verbose_name="Название сайта"
    )
    descriptions = models.TextField(
        verbose_name="Информационный текст",
        blank=True,null=True
    )
    logo = models.ImageField(
        upload_to="logo/",
        verbose_name="Логотип для темного фона"
    )
    logo_complex = models.ImageField(
        upload_to="logo_complex/",
        verbose_name="Логотип для комплексов"
    )
    email = models.EmailField(
        max_length=255,
        verbose_name='Почта'
        )
    location = models.CharField(
        max_length=255,
        verbose_name='Адрес'
    )
    whatsapp = models.URLField(
        verbose_name='Whatspp URL',
        blank=True, null=True
    )
    instagram = models.URLField(
        verbose_name='Instagram URL',
        blank=True, null=True
    )
    youtube = models.URLField(
        verbose_name='Youtube URL',
        blank=True, null=True
    )
    facebook = models.URLField(
        verbose_name='Facebook URL',
        blank=True, null=True
    )
    def __str__(self):
        return self.title
    
    class Meta:
            verbose_name = "Основная настройка"
            verbose_name_plural = "Основные настройки"
            
            
class SettingsPhone(models.Model):
    settings = models.ForeignKey(Settings, related_name='phone_title', on_delete=models.CASCADE)
    phone = models.CharField(
        max_length= 255,
        verbose_name='номер телефона'
    )
    class Mata:
        unique_together = ('settings', 'phone') 
        
class About(models.Model):
    image = models.ImageField(
        upload_to="logo_complex/",
        verbose_name="Логотип для комплексов"
    )
    discriptions = RichTextField(
        verbose_name = 'Информационный текст',
        blank=True, null=True
    )
    def __str__(self):
        return self.discriptions
    
    class Meta():
        verbose_name="О нас"
        verbose_name_plural = "О нас"
        
class Adres(models.Model):
    title = models.CharField(
        max_length=255,
        verbose_name='alhtc' 
    )
    
    discriptions = RichTextField(
        verbose_name = 'Информационный текст',
        blank=True, null=True
    )
    def __str__(self):
        return self.discriptions
    
    class Meta():
        verbose_name="адрес"
        verbose_name_plural = "адресы"
