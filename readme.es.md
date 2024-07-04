## Funko Kinder Bot
[![en](https://img.shields.io/badge/lang-en-yellow.svg)](https://github.com/AlexandraOliv14/FunkoKinderBot/blob/main/README.md)
[![es](https://img.shields.io/badge/lang-es-gre.svg)](https://github.com/AlexandraOliv14/FunkoKinderBot/blob/main/readme.es.md)

### Table of Contents

1. [Descripción General](#descripción-general)
2. [Tecnologias](#tecnologias)
3. [Estructura del Proyecto](#estructura-del-proyecto)
3. [Instalación](#instalación)
4. [Configuración de la Base de Datos](#configuración-de-la-base-de-datos)
5. [Uso](#uso)
6. [Ejecución](#ejecución)
7. [Contribuciones](#contribuciones)
8. [Licencia](#licencia)

### Descripción General
 
**Funko Kinder Bot**  es un bot de Telegram diseñado para proporcionar información sobre figuras Funko Pop de Kinder sorpresa a través de varios comandos. Este bot utiliza la biblioteca `pyTelegramBotAPI` para interactuar con los usuarios y `mysql.connector` para manejar la base de datos `MariaDB`. A continuación se detallan los comandos disponibles y su funcionamiento.

### Tecnologias

- *Python 3.x*
- *Bibliotecas de Python:*
    - `pyTelegramBotAPI`
    - `mysql-connector-python`
    - `time`
- *Un token de bot de Telegram*

### Estructura del Proyecto

```
HarryKinderBot/
│
├── db/
│   ├── coneccion.py
│   ├── consultas.py
|
├── config.py
├── main.py
├── .gitignore
```

### Instalación

#### 1. `Clona el repositorio o descarga los archivos.`

#### 2. `Instala las bibliotecas necesarias usando pip:`

```bash
 pip install pyTelegramBotAPI mysql-connector-python
```

#### 3. `Configura tu archivo config.py con tu token de bot de Telegram y los detalles de tu base de datos:`

```python
#config.py

HOST = "localhost"
PUERTO = "3306"
USER = "user_test"
PASSWORD = "password_test"
DATABASE = "HarryKinder"
TOKEN = "TU_TOKEN_DE_TELEGRAM"
ID = ""
```


#### 4. `Asegúrate de tener la base de datos configurada y accesible mediante las funciones en db/consultas.py.`

### Configuración de la Base de Datos

Para configurar la base de datos, asegúrate de tener una base de datos MariaDB instalada y ejecutándose. Luego, crea las tablas necesarias:

## `versions`
| Field       | Type         | Null | Key | Default | Extra          |
| ---         | ---          |---   |---  |---      |---             |
| id_version  | int(11)      | NO   | PRI | NULL    | auto_increment |
| version     | int(11)      | NO   |     | NULL    |                |
| description | varchar(255) | NO   |     | NULL    |                |

## `cod_back`
| Field            | Type         | Null | Key | Default | Extra          |
| ---              | ---          |---   |---  |---      |---             |
| id_cod_back      | int(11)      | NO   | PRI | NULL    | auto_increment |
| code_back_number | int(11)      | NO   |     | NULL    |                |
| code_back_code   | varchar(255) | NO   |     | NULL    |                |

## `cod_front`
| Field        | Type         | Null | Key | Default | Extra          |
| ---          | ---          |---   |---  |---      |---             |
| id_cod_front | int(11)      | NO   | PRI | NULL    | auto_increment |
| code_front   | varchar(255) | NO   |     | NULL    |                |

## `funko`
| Field        | Type         | Null | Key | Default | Extra          |
| ---          | ---          |---   |---  |---      |---             |
| id_funko     | int(11)      | NO   | PRI | NULL    | auto_increment |
| name         | varchar(255) | NO   |     | NULL    |                |
| collected    | tinyint(1)   | YES  |     | NULL    |                |
| id_version   | int(11)      | YES  | MUL | NULL    |                |
| id_cod_front | int(11)      | YES  | MUL | NULL    |                |
| id_cod_back  | int(11)      | YES  | MUL | NULL    |                |


Estas tablas almacenan la información sobre las versiones de los Funkos y los detalles de cada Funko, respectivamente.


### Uso

- `/start` o `/inicio`: Muestra un mensaje de bienvenida y los Comandos disponibles.
- `/funkos`: Muestra una lista de Funkos disponibles junto con sus versiones como botones interactivos.
- `/versions` o `/versiones`: Muestra una lista de versiones disponibles.
- `/frontcode` o `/codigofrontal`: Muestra una lista de códigos frontales disponibles como botones interactivos.
- `/backcode` o `/codigotrasero`: Muestra una lista de códigos traseros disponibles como botones interactivos.

### Ejecución

Para ejecutar el bot, simplemente corre el script `main.py`:

```bash
 python3 main.py
```

### Contribuciones

Las contribuciones son bienvenidas. Si tienes alguna mejora o nueva funcionalidad, no dudes en hacer un fork del repositorio y enviar un pull request.

### Licencia

Este proyecto está licenciado bajo la Licencia MIT. Para más detalles, consulta el archivo `LICENSE`.

---
¡Gracias por usar Funko Kinder Bot! Si tienes alguna pregunta o problema, no dudes en abrir un issue en el repositorio.
