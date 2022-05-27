from django.db import models
from cloudinary.models import CloudinaryField
from django.core.validators import MinValueValidator
from django.contrib.auth.models import User


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone = models.CharField(max_length=14, blank=True)

    def __str__(self):
        return self.user.username


class Properties(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField()
    price = models.IntegerField(validators=[MinValueValidator(0)])
    address = models.CharField(max_length=200)
    main_img = CloudinaryField('image', blank=True)
    list_date = models.DateTimeField(auto_now_add=True)
    available = models.BooleanField(default=True)
    is_published = models.BooleanField(default=False)

    class Meta:
        ordering = ['-list_date']

    def __str__(self):
        return self.name


class ViewingRequest(models.Model):
    message = models.TextField()
    property = models.ForeignKey(Properties, on_delete=models.SET_NULL,
                                 null=True)
    request_date = models.DateTimeField(auto_now_add=True)
    arranged_date = models.DateTimeField(blank=True, null=True)
    for_user = models.OneToOneField(User, on_delete=models.CASCADE)

    class Meta:
        ordering = ['-request_date']

    def __str__(self):
        return f'{self.for_user.first_name} {self.for_user.last_name}'
