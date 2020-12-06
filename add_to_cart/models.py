from django.contrib.auth import forms
from django.db import models
from twilio.rest import Client
import pickle




class Orders(models.Model):

    order_id = models.AutoField(primary_key=True)
    items_json = models.CharField(max_length=5000)
    amount = models.IntegerField(default=0)
    first_name = models.CharField(max_length=90)
    last_name = models.CharField(max_length=111)
    email = models.CharField(max_length=111)
    address = models.CharField(max_length=111, null=True, blank=True)
    city = models.CharField(max_length=111)
    state = models.CharField(max_length=111)
    phone = models.IntegerField(default=0)
    zip_code = models.CharField(max_length=111)

    def str(self):
        return str(self.order_id)

    def save(self, *args, **kwargs):
        name = self.first_name
        field_name = 'order_id'
        obj = OrderUpdate.objects.first()
        field_value = getattr(obj, field_name)

        print(field_value)
        number = '+91' + str(self.phone)
        account_sid = 'AC426a0c6231f62af9155f3ea2dfbf48d4'
        auth_token = '93d00a0d792bdeb19bcf1c4727ff1f35'
        client = Client(account_sid, auth_token)

        message = client.messages.create(

            body=f'Thankyou for Shopping {name}!. Your orderId is {field_value}.You can use this ID to track your order.',
            from_='+12056221509',
            to=number,

        )
        print(message.sid)
        return super().save(args, **kwargs)

    # @staticmethod
    # def address_passing(self, address):
    #     pass


class OrderUpdate(models.Model):
    update_id = models.AutoField(primary_key=True)
    order_id = models.IntegerField(default='')
    update_desc = models.CharField(max_length=5000)
    address = models.CharField(max_length=111, null=True, blank=True)
    timestamp = models.DateField(auto_now_add=True)

    def str(self):
        return self.update_desc[0:7] + "..."