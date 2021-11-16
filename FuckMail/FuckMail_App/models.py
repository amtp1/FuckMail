import asyncio
from asyncio import sleep
from datetime import datetime

from django.db import models

class Emails(models.Model):
    user_id = models.IntegerField()
    address = models.CharField(max_length=255, null=True, verbose_name="Email Address")
    password = models.CharField(max_length=255, null=True, verbose_name="Email Password")
    proxy_url = models.CharField(max_length=255, verbose_name="Proxy URL")
    count_messages = models.IntegerField(null=True, verbose_name="Count messages")
    create_at = models.DateTimeField(editable=True, default=datetime.now())

    def __str__(self):
        return "<Email: %s>" % self.address

    class Meta:
        verbose_name = "Email"
        verbose_name_plural = "Emails"

class CacheMessages(models.Model):
    message_id = models.CharField(max_length=255, null=True, verbose_name="Message ID")
    address = models.CharField(max_length=255, null=True, verbose_name="Email Address")
    from_user = models.CharField(max_length=255, null=True, verbose_name="From")
    subject = models.CharField(max_length=255, null=True, verbose_name="Subject")
    date = models.DateTimeField(editable=True, default=datetime.now())
    payload = models.TextField(null=True, verbose_name="Payload")
    visual = models.BooleanField()

    def __str__(self):
        return "<CacheMessage: %s>" % self.message_id

    class Meta:
        verbose_name = "CacheMessage"
        verbose_name_plural = "CacheMessages"