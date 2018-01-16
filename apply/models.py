from django.db import models
from contentmanager.utilities import ruslugify



def upload_location(instance, filename):
    instance = Apply.objects.last()
    return "%s_%s/%s" % (ruslugify(instance.second_name), ruslugify(instance.first_name), filename)

class Apply(models.Model):
    first_name = models.CharField("Имя", max_length=50)
    second_name = models.CharField("Фамилия", max_length=50)
    email = models.CharField("Почта", blank=True, max_length=100)

    def __str__(self):
        return '%s %s' % (self.first_name, self.second_name)


class Attachment(models.Model):
    applicant = models.ForeignKey(Apply, on_delete=models.CASCADE)
    document = models.FileField("Проект", blank=True, upload_to=upload_location)

    def __str__(self):
        return self.applicant.second_name
