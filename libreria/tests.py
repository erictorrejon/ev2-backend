from decimal import Decimal

from django.contrib.admin.sites import AdminSite
from django.test import TestCase

from .admin import EditorialAdmin, LibroAdmin
from .models import Editorial, Libro


class EditorialLibroTests(TestCase):
	@classmethod
	def setUpTestData(cls):
		cls.editorial = Editorial.objects.create(
			nombre='Ediciones del Sur',
			pais='Chile',
			ciudad='Santiago',
			presupuesto_clp=Decimal('2500000'),
		)
		cls.libro = Libro.objects.create(
			editorial=cls.editorial,
			titulo='Relatos del bosque',
			autor='Camila Rojas',
			anio_publicacion=2024,
			precio_clp=Decimal('12990'),
		)

	def test_models_have_readable_names(self):
		self.assertEqual(str(self.editorial), 'Ediciones del Sur')
		self.assertEqual(str(self.libro), 'Relatos del bosque')

	def test_editorial_deletion_cascades_to_books(self):
		self.editorial.delete()
		self.assertFalse(Libro.objects.filter(pk=self.libro.pk).exists())

	def test_amounts_are_stored_as_chilean_pesos(self):
		self.assertEqual(self.editorial.presupuesto_clp, Decimal('2500000'))
		self.assertEqual(self.libro.precio_clp, Decimal('12990'))

	def test_admin_formats_amounts_as_chilean_pesos(self):
		editorial_admin = EditorialAdmin(Editorial, AdminSite())
		libro_admin = LibroAdmin(Libro, AdminSite())
		self.assertEqual(editorial_admin.presupuesto_formateado(self.editorial), '$2.500.000')
		self.assertEqual(libro_admin.precio_formateado(self.libro), '$12.990')
