class Datos:
    def __init__(self, ruc: str, razon_social, provincia_juridiccion, nombre_comercial, estado_contribuyente, clase_contribuyente, fecha_inicio_actividades
                 ,fecha_actualizacion, fecha_suspencion_definitiva, fecha_reinicio_actividades, obligado, tipo_contribuyente, numero_establecimiento,
                 nombre_fantasia_comercial, estado_establecimiento, descripcion_provincia_est, descripcion_canton_est, descripcion_parroquia_est, codigo_ciiu,
                 actividad_economica):
        self.ruc = ruc
        self.razon_social = razon_social
        self.provincia_juridiccion = provincia_juridiccion
        self.nombre_comercial = nombre_comercial
        self.estado_contribuyente = estado_contribuyente
        self.clase_contribuyente = clase_contribuyente
        self.fecha_inicio_actividades = fecha_inicio_actividades
        self.fecha_actualizacion = fecha_actualizacion
        self.fecha_suspencion_definitiva = fecha_suspencion_definitiva
        self.fecha_reinicio_actividades = fecha_reinicio_actividades
        self.obligado = obligado
        self.tipo_contribuyente = tipo_contribuyente
        self.numero_establecimiento = numero_establecimiento
        self.nombre_fantasia_comercial = nombre_fantasia_comercial
        self.estado_establecimiento = estado_establecimiento
        self.descripcion_provincia_est = descripcion_provincia_est
        self.descripcion_canton_est = descripcion_canton_est
        self.descripcion_parroquia_est =descripcion_parroquia_est
        self.codigo_ciiu = codigo_ciiu
        self. actividad_economica = actividad_economica



# ESTADO_ESTABLECIMIENTO|DESCRIPCION_PROVINCIA_EST|DESCRIPCION_CANTON_EST|DESCRIPCION_PARROQUIA_EST|CODIGO_CIIU|ACTIVIDAD_ECONOMICA
