from django.db import models

class Proposal(models.Model):
    PROPOSAL_TYPES = [
        ('Research', 'Research'),
        ('Business', 'Business'),
        ('Grant', 'Grant'),
    ]

    title = models.CharField(max_length=255)
    proposal_type = models.CharField(max_length=50, choices=PROPOSAL_TYPES)
    file = models.FileField(upload_to='proposals/')
    submitted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
