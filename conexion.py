from mysql.connector import pooling
from mysql.connector import Error


class Conexion:
    DATABASE = 'zona_fit_db'
    USER = 'root'
    PASSWORD = 'admin'
    DB_PORT = '3306'
    HOST = 'localhost'
    POOL_SIZE = 5
    POOL_NAME = 'zona_fit_pool'
    pool = None

    @classmethod
    def obtener_pool(cls):
        if cls.pool is None: # Se crea el objeto pool
            try:
                cls.pool = pooling.MySQLConnectionPool(
                    pool_name = cls.POOL_NAME,
                    pool_size = cls.POOL_SIZE,
                    host = cls.HOST,
                    port = cls.DB_PORT,
                    database = cls.DATABASE,
                    user = cls.USER,
                    password = cls.PASSWORD
                )
                return cls.pool

            except Error as e:
                print('ocurrio un error al obtener pool: {e}')
        else:
            return cls.pool
    
    @classmethod    
    def obtener_conexion(cls):
        return cls.obtener_pool().get_connection()
    
    @classmethod
    def liberar_conexion(cls,conexion):
        conexion.close()


if __name__ == '__main__':
    # Crear objeto pool
    pool = Conexion.obtener_pool()
    print(pool)

    conexion1 = pool.get_connection()
    print(conexion1)

    Conexion.liberar_conexion(conexion1)
    print('Se ha liberado el objeto conexion1')
    
