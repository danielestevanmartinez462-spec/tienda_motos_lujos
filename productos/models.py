from django.db import models

class categoria(models.Model):
    nombre = models.CharField(max_length=100)

    def __str__(self):
        return  f'{self.nombre}'


class productos(models.Model):
    nombre = models.CharField(max_length=50)
    marca = models.CharField(max_length=60)
    categoria = models.ForeignKey(categoria, on_delete=models.CASCADE, related_name='productos')
    talla = models.CharField (max_length=15)
    color = models.CharField(max_length=30)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.PositiveIntegerField (default=0)
    descripcion =models.TextField (blank=True)
    
    def __str__(self):
        return  f'{self.nombre} - {self.marca} - {self.categoria} - {self.talla} - {self.color} - {self.precio} - {self.stock} - {self.descripcion}'

class clientes (models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField (max_length=50)
    documento = models.CharField(max_length=20,  unique=True)
    correo = models.EmailField(unique=True)
    telefono = models.CharField(max_length=20)
              

    def __str__(self):
        return  f'{self.nombre} - {self.apellido} - {self.documento} - {self.correo} - {self.telefono}'


class venta (models.Model):
    cliente= models.ForeignKey(clientes, on_delete=models.CASCADE, related_name='ventas')
    fecha = models.DateTimeField (auto_now_add=True)
        
    def __str__(self):
        return  f'venta {self.id} - {self.cliente} '

class Detalleventa(models.Model):
    venta = models.ForeignKey(venta, on_delete=models. CASCADE, related_name='detalles')
    producto = models.ForeignKey(productos, on_delete=models. CASCADE)
    cantidad = models.PositiveIntegerField(default=1)
    precio_unitario = models.DecimalField (max_digits=12 , decimal_places=2)

         
    def __str__(self):
        return  f'{self.venta} - {self.producto} - {self.cantidad} - {self.precio_unitario}'