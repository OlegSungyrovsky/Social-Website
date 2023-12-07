from django.db import models


class Action(models.Model):
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE, related_name='actions')
    verb = models.CharField(max_length=255)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        indexes = [
            models.Index(fields=['-created']),
        ]
        ordering = ('-created', )
