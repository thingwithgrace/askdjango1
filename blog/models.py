# blog/models.py
import re
from django.db import models
from django.forms import ValidationError
from django.utils import timezone
from django.conf import settings
from django.core.urlresolvers import reverse
from imagekit.models import ProcessedImageField
from imagekit.processors import Thumbnail

# Create your models here.


def lnglat_validator(value):
    if not re.match(r'^([+-]?\d+\.?\d*),([+-]?\d+\.?\d*)$', value):
        raise ValidationError('Invalid LngLat Type')

class Post(models.Model):
    STATUS_CHOICES = (
        ('d', 'Draft'),
        ('p', 'Published'),
        ('w', 'Withdrawn'),
    )
    user = models.ForeignKey(settings.AUTH_USER_MODEL)
    title = models.CharField(max_length=100, verbose_name='제목', help_text='포스팅 제목을 입력해 주세요. 최대 100자 내외.')
    content = models.TextField(verbose_name='내용')
    photo = ProcessedImageField(blank=True, upload_to='blog/post/%Y/%m/%d',
                                processors=[Thumbnail(300, 300)],
                                format='JPEG',
                                options={'quality': 60})

    tags = models.CharField(max_length=100, blank=True)
    lnglat = models.CharField(max_length=50, help_text='경도/위도 포맷으로 입력', blank=True,
                              validators=[lnglat_validator])
    status = models.CharField(max_length=1, choices=STATUS_CHOICES)
    tag_set = models.ManyToManyField('Tag', blank=True) # 문자열로도 지정 가능 = 현재 파일 안에 있는 것과 관계를 맺는다 의미(뒤에 있어도 무관)
    created_at = models.DateTimeField(auto_now_add=True) # 최초 저장시 자동저장되는 옵션
    updated_at = models.DateTimeField(auto_now=True) # 저장될 때마다 자동저장됨

    class Meta:
        ordering = ['-id']

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('blog:post_detail', args=[self.id])


class Comment(models.Model):
    post = models.ForeignKey(Post)
    author = models.CharField(max_length=20)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Tag(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name
