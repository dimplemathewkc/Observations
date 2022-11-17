from django.db import models
from django.db.models import ManyToManyField


class ValueTypes(models.Model):
    """
    ValueTypes model
    """

    value_type = models.CharField(max_length=100)

    def __str__(self):
        return self.value_type

    class Meta:
        verbose_name_plural = "ValueTypes"


class ValueUnits(models.Model):
    """
    ValueUnits model
    """

    value_unit = models.CharField(max_length=100)

    def __str__(self):
        return self.value_unit

    class Meta:
        verbose_name_plural = "ValueUnits"


class Components(models.Model):
    """
    Components model
    """

    observation_name = models.CharField(max_length=100)
    value = models.DecimalField(max_digits=10, decimal_places=2)
    value_type = models.ForeignKey(ValueTypes, on_delete=models.CASCADE)
    value_unit = models.ForeignKey(ValueUnits, on_delete=models.CASCADE)

    def __str__(self):
        return self.observation_name

    class Meta:
        verbose_name_plural = "Components"


class Observations(models.Model):
    """
    Observations model
    """

    monitored_id = models.IntegerField()
    observation_name = models.CharField(max_length=500)
    issued_at = models.DateTimeField()
    component = ManyToManyField(Components)

    def __str__(self):
        return self.observation_name

    class Meta:
        verbose_name_plural = "Observations"
