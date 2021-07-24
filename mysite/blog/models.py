from django.conf import settings
from django.db import models
from django.utils import timezone

class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete= models.CASCADE) #Um link para outro modelo
    title = models.CharField(max_length= 200) #Definindo um limite de caracteres para o texto.
    text = models.TextField() #Define que este campo é para textos sem limite.
    created_date = models.DateTimeField(default= timezone.now) #Data e hora do instante da criação.
    published_date = models.DateTimeField(blank= True, null= True) #Data e hora das publicaçõesoo-

    def publish(self): #função do blog, POSTAR
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title
