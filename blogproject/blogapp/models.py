from django.db import models

class BlogPost(models.Model):
    CATEGORY = (('1floor', '一階建')),(('2floor', '二階建')),(('3floor', '三階建'))

    title = models.CharField(
        verbose_name='市町村',
        max_length=200
    )

    content = models.TextField(
        verbose_name='詳細'
    )

    posted_at = models.DateTimeField(
        verbose_name='掲載日時',
        auto_now_add=True
    )

    category = models.CharField(
        verbose_name='階数',
        max_length=50,
        choices=CATEGORY
    )

    def __str__(self):
        return self.title

