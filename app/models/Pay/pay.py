# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from django.core.validators import MaxValueValidator


@python_2_unicode_compatible
class Pay(models.Model):
    """
    Class defining the Pay model

    t.integer  "user_id",            limit: 4
    t.string   "bank_account_num",   limit: 255
    t.string   "bank_routing_num",   limit: 255
    t.integer  "percent_of_deposit", limit: 4
    t.datetime "created_at"
    t.datetime "updated_at"
    """
    MAX_INT_VALUE = 2**32-1

    def __str__(self):
        return self.user_id.__str__() + " Pay Summary: \n" \
               + "\nBank Account Number: " + self.bank_account_num \
               + "\nBank Routing Number: " + self.bank_routing_num \
               + "\nPercent of deposit: " + str(self.percent_of_deposit)

    user_id = models.ForeignKey('User', on_delete=models.CASCADE)
    bank_account_num = models.CharField(max_length=255)
    bank_routing_num = models.CharField(max_length=255)
    percent_of_deposit = models.PositiveIntegerField(validators=[MaxValueValidator(MAX_INT_VALUE)])
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        db_table = "app_pays"
