from django.db import models

class Post(models.Model):
    CATEGORY_CHOICES = [
        ('tech', 'Technology'),
        ('business', 'Business'),
        ('lifestyle', 'Lifestyle'),
        ('travel', 'Travel'),
        ('other', 'Other'),
    ]
    
    title = models.CharField(max_length=200)
    content = models.TextField()
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES, default='other')
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.title