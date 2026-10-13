from django.contrib import admin
from django.utils.formats import number_format
from django.utils.html import format_html

from .models import Editorial, Libro


@admin.register(Editorial)
class EditorialAdmin(admin.ModelAdmin):
	list_display = ('nombre', 'pais', 'ciudad', 'presupuesto_formateado')
	list_filter = ('pais', 'ciudad')
	search_fields = ('nombre', 'pais', 'ciudad')

	@admin.display(description='Monto', ordering='presupuesto_clp')
	def presupuesto_formateado(self, obj):
		return format_html(
			'${}',
			number_format(
				obj.presupuesto_clp,
				decimal_pos=0,
			use_l10n=False,
				force_grouping=True,
			),
		)


@admin.register(Libro)
class LibroAdmin(admin.ModelAdmin):
	list_display = ('titulo', 'editorial', 'autor', 'anio_publicacion', 'precio_formateado')
	list_filter = ('editorial', 'anio_publicacion')
	search_fields = ('titulo', 'autor', 'editorial__nombre')
	list_select_related = ('editorial',)

	@admin.display(description='Precio', ordering='precio_clp')
	def precio_formateado(self, obj):
		return format_html(
			'${}',
			number_format(
				obj.precio_clp,
				decimal_pos=0,
				use_l10n=False,
				force_grouping=True,
			),
		)
