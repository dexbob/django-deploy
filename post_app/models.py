from django.db import models
from django.utils.text import slugify
from django.utils.crypto import get_random_string

# Create your models here.
class Posts(models.Model):
    CATEGORY = (('BUSINESS', 'Business'), ('PERSONAL','Personal'),('IMPORTANT','Important')) 
    title = models.CharField(max_length=100)
    body = models.TextField()
    slug = models.SlugField(unique=True, blank=True, null=True)        # 고유문자값 (id로 활용 가능)
    category = models.CharField(max_length=10, choices=CATEGORY, default='PERSONAL')      # 드롭다운 메뉴 형식
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            slug = slugify(self.title)
            if Posts.objects.filter(slug=slug).exists():
                slug = f'{slug}-{get_random_string(5)}'
            self.slug = slug
        super(Posts, self).save(*args, **kwargs)

