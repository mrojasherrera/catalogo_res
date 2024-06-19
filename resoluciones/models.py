from django.db import models

# Create your models here.

# Modelo Resoluciones
class Resoluciones(models.Model):
    class Origen(models.TextChoices):
        PROCURADOR = 'ptn', 'PTN'
        SUBPROCURADOR = 'sptn', 'SPTN'

    numero = models.IntegerField()
    fecha = models.DateField()
    sumario = models.CharField(max_length=500)
    fecha_publicacion = models.DateField()
    observaciones = models.CharField(max_length=500)
    origen = models.CharField(
        max_length=4,
        choices=Origen.choices,
        default=Origen.PROCURADOR
    )
    # texto_de_resolucion = models.FileField(upload_to='resoluciones/', null=True, blank=True)
    texto_de_resolucion = models.CharField(max_length=100, null=True, blank=True)

    activo = models.BooleanField(default= True)
    dummy = models.TextField()

    class Meta:
        db_table = 'resoluciones'
        verbose_name = 'Resoluciones'
        verbose_name_plural = 'Resoluciones'

    def __str__(self):
        return f"{self.numero} - {self.sumario}"
    

# Modelo ResolucionRelacion

class ResolucionRelacion(models.Model):

    RESOLUCIONES_CHOICES = [
        ('modifica_a', 'MODIFICA_A'),
        ('amplia_a', 'AMPLIA_A'),
        ('suspende_a', 'SUSPENDE_A'),
        ('deroga_a', 'DEROGA_A'),
    ]
    res_orig = models.ForeignKey(Resoluciones, related_name= 'res_orig', on_delete = models.DO_NOTHING)
    res_dest = models.ForeignKey(Resoluciones, related_name= 'res_dest', on_delete = models.DO_NOTHING)
    tipo_relacion = models.CharField(max_length=10, choices=RESOLUCIONES_CHOICES)

    class Meta:
        db_table = 'resolucion_relacion'
        verbose_name = 'Resolucion_Relacion'
        verbose_name_plural = 'Resolucion_Relaciones'

    def __str__(self):
        return f"{self.res_orig.numero} {self.get_tipo_relacion_display()} {self.res_dest.numero}"