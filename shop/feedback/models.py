from django.db import models


class FeedBack(models.Model):
    """"Форма обратной связи с номером"""

    name = models.CharField(max_length=128, verbose_name='Имя')
    phone = models.CharField(max_length=11, verbose_name='Контактный номер телефона')
    comment = models.TextField(verbose_name='Комментарий', null=True, blank=True)

    def __str__(self):
        return str(self.name)

    class Meta:
        verbose_name = 'Форма обратной связи'
        verbose_name_plural = 'Формы обратной связи'


""""1"""