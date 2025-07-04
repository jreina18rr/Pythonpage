# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Compra(models.Model):
    idcompra = models.AutoField(db_column='IdCompra', primary_key=True)  # Field name made lowercase.
    fechaemision = models.DateField(db_column='FechaEmision', blank=True, null=True)  # Field name made lowercase.
    idproveedor = models.ForeignKey('Proveedor', models.DO_NOTHING, db_column='IdProveedor', blank=True, null=True)  # Field name made lowercase.
    descripcion = models.CharField(db_column='Descripcion', max_length=100, blank=True, null=True)  # Field name made lowercase.
    valortotal = models.DecimalField(db_column='ValorTotal', max_digits=10, decimal_places=2, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        db_table = 'compra'


class DetalleCompra(models.Model):
    iddetallecompra = models.AutoField(db_column='IdDetalleCompra', primary_key=True)  # Field name made lowercase.
    idcompra = models.ForeignKey(Compra, models.DO_NOTHING, db_column='IdCompra', blank=True, null=True)  # Field name made lowercase.
    idproducto = models.ForeignKey('Producto', models.DO_NOTHING, db_column='IdProducto', blank=True, null=True)  # Field name made lowercase.
    cantidad = models.IntegerField(db_column='Cantidad', blank=True, null=True)  # Field name made lowercase.
    valorproducto = models.DecimalField(db_column='ValorProducto', max_digits=10, decimal_places=2, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        db_table = 'detalle_compra'


class DetallePedido(models.Model):
    iddetallepedido = models.AutoField(db_column='IdDetallePedido', primary_key=True)  # Field name made lowercase.
    idpedido = models.ForeignKey('Pedido', models.DO_NOTHING, db_column='IdPedido', blank=True, null=True)  # Field name made lowercase.
    idproducto = models.ForeignKey('Producto', models.DO_NOTHING, db_column='IdProducto', blank=True, null=True)  # Field name made lowercase.
    cantidad = models.IntegerField(db_column='Cantidad', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        db_table = 'detalle_pedido'


class DetalleVenta(models.Model):
    iddetalleventa = models.AutoField(db_column='IdDetalleVenta', primary_key=True)  # Field name made lowercase.
    idventa = models.ForeignKey('Venta', models.DO_NOTHING, db_column='IdVenta', blank=True, null=True)  # Field name made lowercase.
    idproducto = models.ForeignKey('Producto', models.DO_NOTHING, db_column='IdProducto', blank=True, null=True)  # Field name made lowercase.
    cantidad = models.IntegerField(db_column='Cantidad', blank=True, null=True)  # Field name made lowercase.
    preciounitario = models.DecimalField(db_column='PrecioUnitario', max_digits=10, decimal_places=2, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        db_table = 'detalle_venta'


class Pedido(models.Model):
    idpedido = models.AutoField(db_column='IdPedido', primary_key=True)  # Field name made lowercase.
    idusuario = models.ForeignKey('Usuarios', models.DO_NOTHING, db_column='IdUsuario', blank=True, null=True)  # Field name made lowercase.
    estado = models.CharField(db_column='Estado', max_length=50, blank=True, null=True)  # Field name made lowercase.
    fechacreacion = models.DateTimeField(db_column='FechaCreacion')  # Field name made lowercase.

    class Meta:
        db_table = 'pedido'


class Producto(models.Model):
    idproducto = models.AutoField(db_column='IdProducto', primary_key=True)  # Field name made lowercase.
    fecharegistro = models.DateField(db_column='FechaRegistro', blank=True, null=True)  # Field name made lowercase.
    nomproducto = models.CharField(db_column='NomProducto', max_length=50, blank=True, null=True)  # Field name made lowercase.
    nomcategoria = models.CharField(db_column='NomCategoria', max_length=10, blank=True, null=True)  # Field name made lowercase.
    cantidad = models.CharField(db_column='Cantidad', max_length=50, blank=True, null=True)  # Field name made lowercase.
    fechavencimiento = models.DateField(db_column='FechaVencimiento', blank=True, null=True)  # Field name made lowercase.
    valorlibra = models.IntegerField(db_column='Valorlibra', blank=True, null=True)  # Field name made lowercase.
    imagen = models.CharField(db_column='Imagen', max_length=255, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        db_table = 'producto'


class Proveedor(models.Model):
    idproveedor = models.IntegerField(db_column='IdProveedor', primary_key=True)  # Field name made lowercase.
    nomempresa = models.CharField(db_column='NomEmpresa', max_length=50, blank=True, null=True)  # Field name made lowercase.
    producto = models.CharField(db_column='Producto', max_length=50, blank=True, null=True)  # Field name made lowercase.
    telefono = models.IntegerField(db_column='Telefono', blank=True, null=True)  # Field name made lowercase.
    correo = models.CharField(db_column='Correo', max_length=50, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        db_table = 'proveedor'


class Roles(models.Model):
    idrol = models.AutoField(db_column='IdRol', primary_key=True)  # Field name made lowercase.
    rolnombre = models.CharField(db_column='RolNombre', max_length=50, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        db_table = 'roles'


class Usuarios(models.Model):
    idusuario = models.AutoField(db_column='IdUsuario', primary_key=True)  # Field name made lowercase.
    rol = models.ForeignKey(Roles, models.DO_NOTHING, db_column='Rol', blank=True, null=True)  # Field name made lowercase.
    nombres = models.CharField(db_column='Nombres', max_length=50, blank=True, null=True)  # Field name made lowercase.
    apellidos = models.CharField(db_column='Apellidos', max_length=50, blank=True, null=True)  # Field name made lowercase.
    fechanacimiento = models.DateField(db_column='FechaNacimiento', blank=True, null=True)  # Field name made lowercase.
    direccion = models.CharField(db_column='Direccion', max_length=100, blank=True, null=True)  # Field name made lowercase.
    telefono = models.CharField(db_column='Telefono', max_length=20, blank=True, null=True)  # Field name made lowercase.
    email = models.CharField(db_column='Email', max_length=50, blank=True, null=True)  # Field name made lowercase.
    contrasena = models.CharField(db_column='Contrasena', max_length=50, blank=True, null=True)  # Field name made lowercase.
    estado = models.CharField(db_column='Estado', max_length=13, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        db_table = 'usuarios'


class Venta(models.Model):
    idventa = models.AutoField(db_column='IdVenta', primary_key=True)  # Field name made lowercase.
    fechaemision = models.DateField(db_column='FechaEmision', blank=True, null=True)  # Field name made lowercase.
    idusuario = models.ForeignKey(Usuarios, models.DO_NOTHING, db_column='IdUsuario', blank=True, null=True)  # Field name made lowercase.
    valortotal = models.DecimalField(db_column='ValorTotal', max_digits=10, decimal_places=2, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        db_table = 'venta'
