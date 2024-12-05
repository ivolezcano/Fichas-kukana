from django.db import models
from django.core.exceptions import ValidationError

def validate_unique_job_number(value):
    if Trabajo.objects.filter(numero_trabajo=value).exists():
        raise ValidationError(f"El número de trabajo {value} ya está asignado a otro trabajo.")

class Trabajo(models.Model):
    # Datos básicos del trabajo
    numero_trabajo = models.PositiveIntegerField(
        unique=True,
        validators=[validate_unique_job_number],
        verbose_name="Número de Trabajo"
    )
    fecha_dia = models.DateField(auto_now_add=True, verbose_name="Fecha del Día")
    fecha_retiro = models.DateField(verbose_name="Fecha en que el cliente puede retirar")

    # Información del cliente
    es_cliente = models.BooleanField(verbose_name="¿Es cliente?", choices=[(True, "Sí"), (False, "No")])
    nombre_cliente = models.CharField(max_length=255, verbose_name="Nombre del Cliente")
    domicilio = models.CharField(max_length=255, verbose_name="Domicilio", blank=True, null=True)
    telefono = models.CharField(max_length=20, verbose_name="Teléfono", blank=True, null=True)
    whatsapp = models.CharField(max_length=20, verbose_name="WhatsApp", blank=True, null=True)
    email = models.EmailField(verbose_name="Email", blank=True, null=True)

    # Detalles de la receta - Lejos
    ojo_derecho_lejos_esf = models.CharField(max_length=10, verbose_name="Ojo Derecho - Esf (Lejos)", blank=True, null=True)
    ojo_derecho_lejos_cil = models.CharField(max_length=10, verbose_name="Ojo Derecho - Cil (Lejos)", blank=True, null=True)
    ojo_derecho_lejos_en = models.CharField(max_length=10, verbose_name="Ojo Derecho - en (Lejos)", blank=True, null=True)
    ojo_derecho_lejos_dip = models.CharField(max_length=10, verbose_name="Ojo Derecho - Dip (Lejos)", blank=True, null=True)
    
    ojo_izquierdo_lejos_esf = models.CharField(max_length=10, verbose_name="Ojo Izquierdo - Esf (Lejos)", blank=True, null=True)
    ojo_izquierdo_lejos_cil = models.CharField(max_length=10, verbose_name="Ojo Izquierdo - Cil (Lejos)", blank=True, null=True)
    ojo_izquierdo_lejos_en = models.CharField(max_length=10, verbose_name="Ojo Izquierdo - en (Lejos)", blank=True, null=True)
    ojo_izquierdo_lejos_alt = models.CharField(max_length=10, verbose_name="Ojo Izquierdo - ALT (Lejos)", blank=True, null=True)

    cristal_lejos = models.CharField(max_length=100, verbose_name="Cristal (Lejos)", blank=True, null=True)
    armazon_lejos = models.CharField(max_length=100, verbose_name="Armazón (Lejos)", blank=True, null=True)

    # Detalles de la receta - Cerca
    ojo_derecho_cerca_esf = models.CharField(max_length=10, verbose_name="Ojo Derecho - Esf (Cerca)", blank=True, null=True)
    ojo_derecho_cerca_cil = models.CharField(max_length=10, verbose_name="Ojo Derecho - Cil (Cerca)", blank=True, null=True)
    ojo_derecho_cerca_en = models.CharField(max_length=10, verbose_name="Ojo Derecho - en (Cerca)", blank=True, null=True)
    ojo_derecho_cerca_dip = models.CharField(max_length=10, verbose_name="Ojo Derecho - Dip (Cerca)", blank=True, null=True)
    
    ojo_izquierdo_cerca_esf = models.CharField(max_length=10, verbose_name="Ojo Izquierdo - Esf (Cerca)", blank=True, null=True)
    ojo_izquierdo_cerca_cil = models.CharField(max_length=10, verbose_name="Ojo Izquierdo - Cil (Cerca)", blank=True, null=True)
    ojo_izquierdo_cerca_en = models.CharField(max_length=10, verbose_name="Ojo Izquierdo - en (Cerca)", blank=True, null=True)
    ojo_izquierdo_cerca_alt = models.CharField(max_length=10, verbose_name="Ojo Izquierdo - ALT (Cerca)", blank=True, null=True)

    cristal_cerca = models.CharField(max_length=100, verbose_name="Cristal (Cerca)", blank=True, null=True)
    armazon_cerca = models.CharField(max_length=100, verbose_name="Armazón (Cerca)", blank=True, null=True)

    # Información adicional
    receta_doctor = models.CharField(max_length=255, verbose_name="Receta Dr", blank=True, null=True)
    obra_social = models.CharField(max_length=255, verbose_name="O.O.S.S", blank=True, null=True)
    observaciones = models.TextField(verbose_name="Observaciones", blank=True, null=True)
    como_nos_conocio = models.CharField(max_length=255, verbose_name="¿Cómo nos conoció?", blank=True, null=True)

    # Información de pagos
    total = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Total", blank=True, null=True)
    seña = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Seña", blank=True, null=True)
    saldo = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Saldo", blank=True, null=True)

    def __str__(self):
        return f"Trabajo #{self.numero_trabajo} - {self.nombre_cliente or 'Sin Nombre'}"