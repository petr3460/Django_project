from django.db import models
from django.contrib.auth.models import User


class Category(models.Model):
	name = models.CharField(max_length=50, verbose_name='название категории')
	alias = models.SlugField(verbose_name='alias категории')

	class Meta:
		verbose_name = 'категория'
		verbose_name_plural = 'категории'

	def __str__(self):
		return 'категория %s' % self.name


class Item(models.Model):
	name = models.CharField(max_length=100, verbose_name='название товара')
	price = models.IntegerField(default=0, verbose_name='цена')
	image = models.ImageField(null=True, blank=True, upload_to='static/')
	# image2 = models.ImageField(null=True, blank=True, upload_to='images/')
	# image3 = models.ImageField(null=True, blank=True, upload_to='images/')
	# image4 = models.ImageField(null=True, blank=True, upload_to='images/')
	description = models.CharField(max_length=1023, verbose_name='описание товара')
	alias = models.SlugField(verbose_name='alias товара')
	category = models.ForeignKey(Category, on_delete=models.CASCADE, )
	likes = models.IntegerField(default=0, verbose_name='лайки')

	class Meta:
		verbose_name = 'товар'
		verbose_name_plural = 'товары'

	def __str__(self):
		return 'товар %s' % self.name


class Comments(models.Model):
	class Meta:
		db_table = 'comments'

	comments_text = models.TextField()
	comments_item = models.ForeignKey(Item, on_delete=models.CASCADE)
	comments_user = models.ForeignKey(User, on_delete=models.CASCADE)
