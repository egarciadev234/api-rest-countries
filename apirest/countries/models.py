from django.db import models

# Create your models here.
class Country(models.Model):
    """
    Modelo Country
        Atributos
            name_country: nombre de los paises
            code_country: codigo de cada pais
    """
    name = models.CharField(max_length=250)
    code = models.CharField(max_length=3)

    class Meta:
        verbose_name = "Country"
        verbose_name_plural = "Countries"

    def __str__(self): 
        return '{}{}'.format(self.name, self.code)