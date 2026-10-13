from django.core.validators import MinValueValidator
from django.db import models


class Editorial(models.Model):
	nombre = models.CharField(max_length=120, unique=True, verbose_name='Nombre')
	pais = models.CharField(max_length=80, verbose_name='País')
	ciudad = models.CharField(max_length=80, verbose_name='Ciudad')
	presupuesto_clp = models.DecimalField(
		max_digits=14,
		decimal_places=0,
		validators=[MinValueValidator(0)],
		verbose_name='Monto',
	)

	class Meta:
		ordering = ('nombre',)
		verbose_name = 'editorial'
		verbose_name_plural = 'editoriales'

	def __str__(self):
		return self.nombre


class Libro(models.Model):
	editorial = models.ForeignKey(
		Editorial,
		on_delete=models.CASCADE,
		related_name='libros',
		verbose_name='editorial',
	)
	titulo = models.CharField(max_length=200, verbose_name='Título')
	autor = models.CharField(max_length=120, verbose_name='Autor')
	anio_publicacion = models.PositiveIntegerField(verbose_name='Año de publicación')
	precio_clp = models.DecimalField(
		max_digits=12,
		decimal_places=0,
		validators=[MinValueValidator(0)],
		verbose_name='Precio',
	)

	class Meta:
		ordering = ('titulo',)
		verbose_name = 'libro'
		verbose_name_plural = 'libros'

	def __str__(self):
		return self.titulo
