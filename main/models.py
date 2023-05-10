from django.db import models


class Variants(models.Model):
    """Model definition for Variants."""
    number = models.IntegerField()  # номер варианта
    description = models.TextField()  # описание варианта
    L1 = models.FloatField()  # индуктивность
    R1 = models.FloatField()  # сопротивление
    F = models.FloatField()  # частота
    Voltage = models.FloatField()  # напряжение

    def __str__(self):
        return str(self.number)
