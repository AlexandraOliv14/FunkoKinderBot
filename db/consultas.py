from db.conexion  import getCall, getUniqueCall

def getVersions():
    sql = """SELECT version , descripcion 
                    FROM versiones ;"""
    return getUniqueCall(sql)

def getKinders():
    sql = """SELECT k.nombre_funko , k.codigo_frontal, k.codigo_trasero, k.obtenido, v.version
                FROM kinder k 
                INNER JOIN versiones v ON k.version_id = v.version_id ;"""
    return getUniqueCall(sql)

def getCodesByName(name):
    query = """SELECT codigo_frontal , codigo_trasero 
                    FROM kinder 
                    WHERE 1=1
                    AND UPPER(TRIM(nombre_funko))= UPPER(TRIM(%s));"""
    val = ([name])
    return getCall(query, val)

def getCodesNamesByFrontCode(code):
    query = """SELECT nombre_funko , codigo_trasero 
                    FROM kinder 
                    WHERE 1=1
                    AND UPPER(TRIM(codigo_frontal))= UPPER(TRIM(%s));"""
    val = ([code])
    return getCall(query, val)

def getCodesNamesByBackCode(code):
    query = """SELECT nombre_funko , codigo_frontal 
                    FROM kinder 
                    WHERE 1=1
                    AND UPPER(TRIM(codigo_trasero))= UPPER(TRIM(%s));"""
    val = ([code])
    return getCall(query, val)

def getFrontCodes():
    query = """SELECT DISTINCT codigo_frontal
                    FROM kinder
                    WHERE 1=1;"""
    
    return getUniqueCall(query)

def getBackCodes():
    query = """SELECT DISTINCT codigo_trasero
                    FROM kinder
                    WHERE 1=1;"""
    
    return getUniqueCall(query)

def nameByCodes(codF, codB):
    query = """SELECT nombre_funko 
                    FROM kinder 
                    WHERE 1=1
                    AND UPPER(TRIM(codigo_frontal))= UPPER(TRIM(%s))
                    AND UPPER(TRIM(codigo_trasero))= UPPER(TRIM(%s));"""
    val = ([codF, codB])
    return getCall(query, val)

def getcodesByNameVersion(name, version):
    query = """SELECT k.codigo_frontal, k.codigo_trasero
                    FROM kinder k
                    INNER JOIN versiones v ON k.version_id = v.version_id
                    WHERE 1=1
                    AND UPPER(TRIM(k.nombre_funko))= UPPER(TRIM(%s))
                    AND UPPER(TRIM(v.version))= UPPER(TRIM(%s));"""
    
    val = ([name, version])
    return getCall(query, val)

def getFunkos():
    query = """SELECT DISTINCT k.nombre_funko, v.version
                    FROM kinder k 
                    INNER JOIN versiones v ON k.version_id = v.version_id
                    WHERE 1=1;"""
    
    return getUniqueCall(query)