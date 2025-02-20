from django.db import models


# Example table model
class Example(models.Model):
    text = models.CharField(max_length=30)
    number = models.IntegerField()

    class Meta:
        # Create unique constraints
        constraints = [
            models.UniqueConstraint(fields=['text', 'number'], name='unique_text_number')
        ]
