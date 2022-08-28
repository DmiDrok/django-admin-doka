from django.db import models

# Модель отзыва
class Review(models.Model):
	name = models.CharField(max_length=255, verbose_name='Имя пользователя')
	desc = models.TextField(verbose_name='Текст отзыва')

	def __str__(self):
		return f'{self.pk}: Отзыв от {self.name}'

	class Meta:
		verbose_name = 'Отзыв'
		verbose_name_plural = 'Отзывы'
		ordering = ['-id', 'name']


# Модель заказа
class Order(models.Model):
	user_id = models.CharField(max_length=255, verbose_name='ID пользователя в TG')
	name = models.CharField(max_length=255, verbose_name='Login пользователя в TG')
	start_raiting = models.IntegerField(verbose_name='Начальный рейтинг')
	end_raiting = models.IntegerField(verbose_name='Желаемый рейтинг')
	decency = models.IntegerField(verbose_name='Порядочность')
	lvl_trophies = models.IntegerField(verbose_name='Уровень трофеев')
	duo = models.BooleanField(default=False, verbose_name='Дуо')
	price = models.FloatField(verbose_name='Цена заказа')
	is_completed = models.BooleanField(verbose_name='Заказ выполнен')
	date_create = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return f'{self.pk}: Заказ от {self.name}'

	class Meta:
		verbose_name = 'Заказ'
		verbose_name_plural = 'Заказы'
		ordering = ['-id', 'name']