# ** Django Imports **
from django.db import models


class Commission(models.Model):
    """
    Model for commissions
    """

    # information's
    reservation = models.CharField(
        verbose_name="Reservation", max_length=100, db_index=True, unique=True)
    check_in = models.DateField(verbose_name="Check in")
    checkout = models.DateField(verbose_name="Checkout")
    flat = models.CharField(verbose_name="Flat", max_length=65)
    city = models.CharField(verbose_name="City", max_length=28)
    net_incoming = models.DecimalField(
        verbose_name="Net incoming", max_digits=10, decimal_places=2, default=0)

    # modetation's
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.reservation
    
    class Meta:
        verbose_name = "Commission"
        verbose_name_plural = "Commissions"
        ordering = ('-created_at',)