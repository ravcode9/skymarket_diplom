from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class Ad(models.Model):
    image = models.URLField(verbose_name="Изображение",
                            blank=True, null=True)
    title = models.CharField(max_length=255,
                             verbose_name="Название")
    price = models.IntegerField(verbose_name="Цена")
    phone = models.CharField(max_length=20, verbose_name="Телефон",
                             blank=True, null=True)
    description = models.TextField(verbose_name="Описание",
                                   blank=True, null=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE,
                               verbose_name="Автор")
    created_at = models.DateTimeField(auto_now_add=True,
                                      verbose_name="Дата создания")

    class Meta:
        ordering = ['-created_at']
        verbose_name = "Объявление"
        verbose_name_plural = "Объявления"

    def __str__(self):
        return self.title

    @property
    def author_first_name(self):
        return self.author.first_name

    @property
    def author_last_name(self):
        return self.author.last_name

    @property
    def author_id(self):
        return self.author.id


class Comment(models.Model):
    text = models.TextField(verbose_name="Текст отзыва")
    author = models.ForeignKey(User, on_delete=models.CASCADE,
                               verbose_name="Автор")
    ad = models.ForeignKey(Ad, related_name='comments',
                           on_delete=models.CASCADE,
                           verbose_name="Объявление")
    created_at = models.DateTimeField(auto_now_add=True,
                                      verbose_name="Дата создания")

    class Meta:
        ordering = ['-created_at']
        verbose_name = "Отзыв"
        verbose_name_plural = "Отзывы"

    def __str__(self):
        return f"Отзыв от {self.author.email} на {self.ad.title}"

    @property
    def author_first_name(self):
        return self.author.first_name

    @property
    def author_last_name(self):
        return self.author.last_name

    @property
    def author_id(self):
        return self.author.id

    @property
    def ad_id(self):
        return self.ad.id

    @property
    def author_image(self):
        return self.author.profile_image_url if hasattr(
            self.author, 'profile_image_url'
        ) else None
