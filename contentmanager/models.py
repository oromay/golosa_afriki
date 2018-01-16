from django.db import models
from django.core.urlresolvers import reverse
from ckeditor_uploader.fields import RichTextUploadingField


from .utilities import ruslugify


def upload_location(instance, filename):
    return "%s/%s" % (instance.slug, filename)

# Create your models here.



class Elder(models.Model):
    first_name = models.CharField("Имя", max_length=50)
    second_name = models.CharField("Фамилия", max_length=50)
    bio = models.TextField("Короткая справка",)
    avatar = models.ImageField("Аватар", upload_to='elders/')
    email = models.CharField("Почта", blank=True, max_length=100)

    def __str__(self):
        return '%s %s' % (self.first_name, self.second_name)

class Author(models.Model):
    first_name = models.CharField("Имя", max_length=50)
    second_name = models.CharField("Фамилия", max_length=50)
    slug = models.SlugField(unique=True)
    bio = models.TextField("Короткая справка",)
    avatar = models.ImageField("Аватар", upload_to='authors/')
    email = models.CharField("Почта", blank=True, max_length=100)
    is_winner = models.BooleanField(default=False)

    def get_absolute_url(self):
        return reverse("author", kwargs={"slug": self.slug})

    def __str__(self):
        return '%s %s' % (self.first_name, self.second_name)

class Post(models.Model):
    title = models.CharField("Название", max_length=50)
    slug = models.SlugField(unique=True)
    top_image = models.ImageField(upload_to=upload_location)
    content= models.TextField()
    author = models.ForeignKey(Author, on_delete=models.CASCADE, verbose_name="Автор")
    publish = models.DateTimeField(auto_now=False, auto_now_add=False)
    update = models.DateTimeField("время создания", auto_now=True, auto_now_add=False)
    timestamp = models.DateTimeField("обновлён", auto_now=False, auto_now_add=True)

    def get_absolute_url(self):
        return reverse("detail", kwargs={"slug": self.slug})

    def __str__(self):
        return self.slug

    class Meta:
        ordering =['-timestamp']

class New(models.Model):
    title = models.CharField("Название", max_length=50)
    slug = models.SlugField(unique=True)
    top_image = models.ImageField(upload_to=upload_location)
    content= RichTextUploadingField()
    updated = models.DateTimeField(auto_now=True, auto_now_add=False)
    timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)

    def __str__(self):
        return self.slug

    class Meta:
        ordering =['-timestamp']
