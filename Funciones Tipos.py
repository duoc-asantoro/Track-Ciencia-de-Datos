# define columnas a seleccionar
columnas_seleccionadas = [
        'ID'                             ,
        'Codigo'                         ,
        #Link                           object
        #Nombre                         object
        #Descripcion/Obervaciones       object
        'Tipo'                           ,
        #ProcedenciaOC                  object
        #EsTratoDirecto                 object
        #EsCompraAgil                   object
        #CodigoTipo                      int64
        #CodigoAbreviadoTipoOC          object
        #DescripcionTipoOC              object
        #codigoEstado                    int64
        'Estado'                         ,
        #codigoEstadoProveedor           int64
        #EstadoProveedor                object
        #FechaCreacion                  ,
        'FechaEnvio'                    ,
        #FechaSolicitudCancelacion      object
        #fechaUltimaModificacion        object
        #FechaAceptacion                object
        #FechaCancelacion               object
        #tieneItems                     ,
        #PromedioCalificacion           object
        #CantidadEvaluacion              int64
        #MontoTotalOC                   object
        #TipoMonedaOC                   object
        'MontoTotalOC_PesosChilenos'     ,
        'Impuestos'                      ,
        'TipoImpuesto'                   ,
        'Descuentos'                     ,
        'Cargos'                         ,
        'TotalNetoOC'                    ,
        #CodigoUnidadCompra              int64
        #RutUnidadCompra                object
        #UnidadCompra                   object
        'CodigoOrganismoPublico'         ,
        'OrganismoPublico'               ,             
        # sector                        
        #ActividadComprador             object
        #CiudadUnidadCompra             object
        #RegionUnidadCompra             object
        #PaisUnidadCompra               object
        #CodigoSucursal                  int64
        'RutSucursal'                    ,
        #Sucursal                       object
        'CodigoProveedor'                ,
        'NombreProveedor'                ,
        'ActividadProveedor'             ,
        'ComunaProveedor'                ,
        'RegionProveedor'                ,
        'PaisProveedor'                  ,
        #Financiamiento                 object
        #PorcentajeIva                  object
        #Pais                           object
        #TipoDespacho                    int64
        #FormaPago                       int64
        'CodigoLicitacion'               ,
        #Codigo_ConvenioMarco           object
        'IDItem'                         ,
        #codigoCategoria               float64
        #Categoria                      object
        'codigoProductoONU'              ,
        'NombreroductoGenerico'          ,
        'RubroN1'                        ,
        'RubroN2'                        ,
        'RubroN3'                        ,
        #EspecificacionComprador        object
        #EspecificacionProveedor        object
        'cantidad'                       ,
        'UnidadMedida'                   ,
        'monedaItem'                     ,
        'precioNeto'                     ,
        'totalCargos'                    ,
        'totalDescuentos'                ,
        'totalImpuestos'                 ,
        'totalLineaNeto'                 
        #Forma de Pago                  object
            ]

columnas_nuevos_nombres  = [
        'OC_ID'                             ,
        'OC_Codigo'                         ,
        #Link                           object
        #Nombre                         object
        #Descripcion/Obervaciones       object
        'OC_Tipo'                           ,
        #ProcedenciaOC                  object
        #EsTratoDirecto                 object
        #EsCompraAgil                   object
        #CodigoTipo                      int64
        #CodigoAbreviadoTipoOC          object
        #DescripcionTipoOC              object
        #codigoEstado                    int64
        'OC_Estado'                         ,
        #codigoEstadoProveedor           int64
        #EstadoProveedor                object
        #FechaCreacion                  ,
        'OC_Fecha'                    ,
        #FechaSolicitudCancelacion      object
        #fechaUltimaModificacion        object
        #FechaAceptacion                object
        #FechaCancelacion               object
        #tieneItems                     ,
        #PromedioCalificacion           object
        #CantidadEvaluacion              int64
        #MontoTotalOC                   object
        #TipoMonedaOC                   object
        'OC_Total_Pesos'                    ,
        'OC_Total_Impuestos'                ,
        'OC_Tipo_Impuesto'                   ,
        'OC_Descuentos'                     ,
        'OC_Cargos'                         ,
        'OC_Total_Neto'                     ,
        #CodigoUnidadCompra              int64
        #RutUnidadCompra                object
        #UnidadCompra                   object
        'OC_Organismo'                     ,
        'OC_Organismo_Nombre'              , 
        # sector                        
        #ActividadComprador             object
        #CiudadUnidadCompra             object
        #RegionUnidadCompra             object
        #PaisUnidadCompra               object
        #CodigoSucursal                  int64
        'Proveedor_Rut'                    ,
        #Sucursal                       object
        'Proveedor_Codigo'                ,
        'Proveedor_Nombre'                ,
        'Proveedor_Actividad'             ,
        'Proveedor_Comuna'                ,
        'Proveedor_Region'                ,
        'Proveedor_Pais'                  ,
        #Financiamiento                 object
        #PorcentajeIva                  object
        #Pais                           object
        #TipoDespacho                    int64
        #FormaPago                       int64
        'Licitacion_Codigo'               ,
        #Codigo_ConvenioMarco           object
        'Item_ID'                         ,
        #codigoCategoria               float64
        #Categoria                      object
        'Item_Producto_Codigo'            ,
        'Item_Producto_Generico'          ,
        'Item_Producto_RubroN1'           ,
        'Item_Producto_RubroN2'           ,
        'Item_Producto_RubroN3'           ,
        #EspecificacionComprador        object
        #EspecificacionProveedor        object
        'Item_Cantidad'                       ,
        'Item_Unidad_Medida'                   ,
        'Item_Moneda'                     ,
        'Item_Precio_Neto'                     ,
        'Item_Total_Cargos'                    ,
        'Item_Total_Descuentos'                ,
        'Item_Total_Impuestos'                 ,
        'Item_Total_Neto'                 
        #Forma de Pago                  object
            ]

# define funcion de limpieza preliminar de archivo feather

# --- PASO 4: Limpieza y Compresión Final en un solo pase ---
def optimizar_tipos(df):

    # Lista de columnas que deben ser enteras y no pueden tener NaN
    cols_enteros = [
        "Organismo_Codigo",
        "Item_Producto_Codigo",
        "Proveedor_Codigo",
        "OC_tieneItems",
    ]
    # Rellenar nulos con 0 solo en las columnas de tipo entero que existan en el DataFrame
    cols_a_rellenar = [col for col in cols_enteros if col in df.columns]
    df[cols_a_rellenar] = df[cols_a_rellenar].fillna(0)
    
    # Mapeo de tipos optimizado para ChileCompra
    dtypes_optimizados = {
        # Fechas
        "OC_Fecha"                   : "datetime64[ns]",
        # Banderas binarias
        "OC_tieneItems"              : "uint8",
        # Campos de codigo
        'OC_Organismo'               : "uint32",
        'Item_Producto_Codigo'       : "uint32",
        'Proveedor_Codigo'           : "uint32",
        # Columnas con pocos valores repetidos (Bajo Cardinalidad)
        "OC_Tipo"                    : "category",
        "OC_Estado"                  : "category",
        "OC_Organismo_Nombre"        : "category",
        "OC_Tipo_Impuesto"           : "category",
        'Item_Producto_Generico'     : "category",
        'Item_Producto_RubroN1'      : "category",
        'Item_Producto_RubroN2'      : "category",
        'Item_Producto_RubroN3'      : "category",
        "Proveedor_Comuna"           : "category",
        "Proveedor_Region"           : "category",
        "Proveedor_Pais"             : "category",
        "Item_Unidad_Medida"         : "category",
        "Item_Moneda"                : "category",
        # Reducción de decimales de 64-bit a 32-bit (suficiente precisión)
        "OC_Total_Pesos"             : "float64",
        "OC_Total_Impuestos"         : "float64",
        "OC_Descuentos"              : "float64",
        "OC_Cargos"                  : "float64",
        "OC_Total_Neto"              : "float64",
        "Item_Cantidad"              : "float64",
        'Item_Precio_Neto'           : "float64", 
        'Item_Total_Cargos'          : "float64",
        'Item_Total_Descuentos'      : "float64",
        'Item_Total_Impuestos'       : "float64",
        'Item_Total_Neto'            : "float64"     
        }

    # Aplicar conversión
    df = df.astype({col: tipo for col, tipo in dtypes_optimizados.items() if col in df.columns})
    
    return df

def dataframe_caracteristicas(dataframe):
  memoria = dataframe.memory_usage(deep=True).sum()/MegaBytes
  print( "\n","="* 40 )
  print(f"{'TAMAÑO DATAFRAME':>29}")
  print( "-" * 40)
  print(f"{'dataframe':>20} {'Original':>15}")
  print( "=" * 40)
  print(f"{'Memoria':<10} {memoria:>10,.2f} Mb {Memoria_original:>10,.2f} Mb")
  print(f"{'Filas':<10} {dataframe.shape[0]:>10,}    {Filas_original:>10,}")
  print(f"{'Columnas':<10} {dataframe.shape[1]:>10,}    {Columnas_original:>10}")
  print( "=" * 40)
  return

# =======================================================================================================
# Despliega caracteriscas del dataframe para confirmar que la consoldiacion de filas esta bien hecha

def dataframe_resumen(df1, nombre1, df2, nombre2):
    # Función auxiliar para calcular métricas de forma vectorial en milisegundos
    def calcular_metricas(df):
        # Total de filas en el dataset
        filas = len(df)

        # --- 1. MÉTRICAS DE CABECERA (OC_) ---
        oc = df["OC_Codigo"].nunique()

        # Deduplicar por OC para obtener el monto total en pesos de la cabecera sin repetir por línea
        df_oc_unicas = df[["OC_Codigo", "OC_Total_Pesos"]].drop_duplicates(subset=["OC_Codigo"])
        oc_Neto = df_oc_unicas["OC_Total_Pesos"].sum()

        # --- 2. MÉTRICAS DE LÍNEA DE DETALLE (ITEM_) ---
        cant = df["Item_Cantidad"].sum()
        neto = df["Item_Total_Neto_Pesos"].sum() if "Item_Total_Neto_Pesos" in df.columns else 0.00
        imp  = df["Item_Total_Impuestos"].sum()

        return filas, oc, oc_Neto, cant, neto, imp

    # 1. Extracción de métricas
    f1, oc1, oc_Neto1, cant1, neto1, imp1 = calcular_metricas(df1)
    f2, oc2, oc_Neto2, cant2, neto2, imp2 = calcular_metricas(df2)

    # 2. Impresión con formato de 3 columnas
    ANCHO = 82
    print("\n" + "=" * ANCHO)
    print(f"{'CARACTERÍSTICAS DEL DATAFRAME':>65}")
    print("-" * ANCHO)
    print(f"{'Métrica':<18} {nombre1:>20} {nombre2:>20} {'Original':>20}")
    print("=" * ANCHO)

    print(f"{'Filas':<18} {f1:>20,} {f2:>20,} {original_filas:>20,}")
    print(f"{'OC Únicas':<18} {oc1:>20,} {oc2:>20,} {original_OC:>20,}")
    print(f"{'OC Total Pesos':<18} {oc_Neto1:>20,.2f} {oc_Neto2:>20,.2f} {original_OC_Total_Pesos:>20,.2f}")
    print(f"{'Item Cantidad':<18} {cant1:>20,.2f} {cant2:>20,.2f} {original_Item_Cantidad:>20,.2f}")
    print(f"{'Item Total Neto Pesos':<18} {neto1:>20,.2f} {neto2:>20,.2f} {original_Item_Total_Neto:>20,.2f}")
    print(f"{'Item Total Impuestos':<18} {imp1:>20,.2f} {imp2:>20,.2f} {original_Item_Total_Impuestos:>20,.2f}")
  
    print("=" * ANCHO + "\n")