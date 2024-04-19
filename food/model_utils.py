from django.db import models


class TimeStampedModel(models.Model):
    """Абстрактная модель для автозаполнения даты создания и обновления."""

    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True
