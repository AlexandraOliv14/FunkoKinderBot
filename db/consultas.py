from db.conexion  import getCall, getUniqueCall

def getVersions():
    sql = """SELECT version , description 
                FROM versions ;"""
    return getUniqueCall(sql)

def getKinders():
    sql = """SELECT f.name , v.version, cf.code_front, cb.code_back_number, cb.code_back_code
                FROM funko f 
                INNER JOIN versions v ON f.id_version = v.id_version
                INNER JOIN cod_front cf ON f.id_cod_front = cf.id_cod_front 
                INNER JOIN cod_back cb ON f.id_cod_back = cb.id_cod_back;"""
    return getUniqueCall(sql)

def getCodesByName(name):
    query = """SELECT cf.code_front, cb.code_back_number, cb.code_back_code
                    FROM funko f 
                    INNER JOIN versions v ON f.id_version = v.id_version
                    INNER JOIN cod_front cf ON f.id_cod_front = cf.id_cod_front 
                    INNER JOIN cod_back cb ON f.id_cod_back = cb.id_cod_back
                    WHERE 1=1
                    AND UPPER(TRIM(f.name))= UPPER(TRIM(%s));"""
    val = ([name])
    return getCall(query, val)

def getCodesNamesByFrontCode(code):
    query = """SELECT f.name , cb.code_back_number, cb.code_back_code 
                    FROM funko f
                    INNER JOIN versions v ON f.id_version = v.id_version
                    INNER JOIN cod_front cf ON f.id_cod_front = cf.id_cod_front 
                    INNER JOIN cod_back cb ON f.id_cod_back = cb.id_cod_back
                    WHERE 1=1
                    AND UPPER(TRIM(cf.code_front)) = UPPER(TRIM(%s));"""
    val = ([code])
    return getCall(query, val)

def getCodesNamesByBackCode(code):
    query = """SELECT f.name, cf.code_front
                    FROM funko f
                    INNER JOIN versions v ON f.id_version = v.id_version
                    INNER JOIN cod_front cf ON f.id_cod_front = cf.id_cod_front 
                    INNER JOIN cod_back cb ON f.id_cod_back = cb.id_cod_back
                    WHERE 1=1
                    AND UPPER(TRIM(cb.code_back_number))= UPPER(TRIM(%s))
                    AND UPPER(TRIM(cb.code_back_code))= UPPER(TRIM(%s));"""
    val = ([code])
    return getCall(query, val)

def getFrontCodes():
    query = """SELECT cf.code_front
                    FROM cod_front cf
                    WHERE 1=1;"""
    
    return getUniqueCall(query)

def getBackCodes():
    query = """SELECT cb.code_back_number, cb.code_back_code
                    FROM cod_back cb
                    WHERE 1=1;"""
    
    return getUniqueCall(query)

def nameByCodes(codF, codB):
    query = """SELECT f.name 
                    FROM funko f
                    INNER JOIN versions v ON f.id_version = v.id_version
                    INNER JOIN cod_front cf ON f.id_cod_front = cf.id_cod_front 
                    INNER JOIN cod_back cb ON f.id_cod_back = cb.id_cod_back
                    WHERE 1=1
                    AND UPPER(TRIM(code_front))= UPPER(TRIM(%s))
                    AND UPPER(TRIM(code_back_number))= UPPER(TRIM(%s))
                    AND UPPER(TRIM(code_back_code))= UPPER(TRIM(%s));"""
    val = ([codF, codB])
    return getCall(query, val)

def getcodesByNameVersion(name, version):
    query = """SELECT cf.code_front, cb.code_back_number, cb.code_back_code
                    FROM funko f
                    INNER JOIN versions v ON f.id_version = v.id_version
                    INNER JOIN cod_front cf ON f.id_cod_front = cf.id_cod_front 
                    INNER JOIN cod_back cb ON f.id_cod_back = cb.id_cod_back
                    WHERE 1=1
                    AND UPPER(TRIM(f.name))= UPPER(TRIM(%s))
                    AND UPPER(TRIM(v.version))= UPPER(TRIM(%s));"""
    
    val = ([name, version])
    return getCall(query, val)

def getFunkos():
    query = """SELECT DISTINCT f.version, v.version
                    FROM funko f
                    INNER JOIN versiones v ON f.id_version = v.id_version
                    WHERE 1=1;"""
    
    return getUniqueCall(query)