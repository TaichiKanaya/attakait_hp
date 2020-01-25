from django.db import models


class Category(models.Model):
    name = models.CharField(verbose_name='カテゴリ名', max_length=50, null=False)
    created_at = models.DateTimeField(verbose_name='作成日時', auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name='更新日時', auto_now_add=True)
    deleted_at = models.DateTimeField(verbose_name='削除日時', null=True, blank=True)

    def __str__(self):
        return self.name


class SubCategory(models.Model):
    name = models.CharField(verbose_name='サブカテゴリ名', max_length=50, null=False)
    category = models.ForeignKey(Category, verbose_name='カテゴリID', on_delete=models.PROTECT, null=False)
    created_at = models.DateTimeField(verbose_name='作成日時', auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name='更新日時', auto_now_add=True)
    deleted_at = models.DateTimeField(verbose_name='削除日時', null=True, blank=True)

    def __str__(self):
        return self.name


class Article(models.Model):
    category = models.ForeignKey(Category, verbose_name='カテゴリID', on_delete=models.PROTECT, null=False)
    sub_category = models.ForeignKey(SubCategory, verbose_name='サブカテゴリID', on_delete=models.PROTECT, null=True, blank=True)
    title = models.CharField(verbose_name='タイトル', max_length=100, null=False)
    content = models.TextField(verbose_name='本文', null=False)
    created_at = models.DateTimeField(verbose_name='作成日時', auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name='更新日時', auto_now_add=True)
    deleted_at = models.DateTimeField(verbose_name='削除日時', null=True, blank=True)

    def __str__(self):
        return self.title

