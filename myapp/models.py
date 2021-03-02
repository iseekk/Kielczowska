from django.db import models
from django.utils import timezone
from django.urls import reverse
from django.core.validators import MinValueValidator
from picklefield.fields import PickledObjectField


NUM_OF_OCCUPANTS = 3


class Purchase(models.Model):
    author = models.ForeignKey("auth.User", on_delete=models.CASCADE)
    item = models.CharField(max_length=64)
    price = models.FloatField(default=0, validators=[MinValueValidator(0)])
    debts = PickledObjectField(null=True)
    date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"{self.date} - {self.author}: {self.item} {self.price} zł"

    def get_absolute_url(self):
        return reverse("purchase_detail", kwargs={"pk": self.pk})


class Comment(models.Model):
    purchase = models.ForeignKey("Purchase", related_name="comments", on_delete=models.CASCADE)
    author = models.CharField(max_length=25)
    text = models.TextField(max_length=500)
    date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.text

    def get_absolute_url(self):
        return reverse("purchase_detail", kwargs={"pk": self.pk})
