## Funko Kinder Bot
[![en](https://img.shields.io/badge/lang-en-gre.svg)](https://github.com/AlexandraOliv14/FunkoKinderBot/blob/main/README.md)
[![es](https://img.shields.io/badge/lang-es-yellow.svg)](https://github.com/AlexandraOliv14/FunkoKinderBot/blob/main/readme.es.md)

### Table of Contents


1. [General Description](#general-description)
2. [Technologies](#technologies)
3. [Project Structure](#project_structure)
3. [Installation](#installation)
4. [Database Configuration](#database-configuration)
5. [Usage](#usage)
6. [Execution](#execution)
7. [Contributions](#contributions)
8. [License](#license)

### General Description
**Funko Kinder Bot** is a Telegram bot designed to provide information about Funko Pop figures from Kinder Surprise through various commands. This bot uses the `pyTelegramBotAPI` library to interact with users and `mysql.connector` to handle the `MariaDB` database. Below are the available commands and their functionalities.

### Technologies
- *Python 3.x*
- *Python Libraries:*
    - `pyTelegramBotAPI`
    - `mysql-connector-python`
    - `time`
- *A Telegram bot token*

### Project Structure

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

### Installation

#### 1. `Clone the repository or download the files.`

#### 2. `Install the necessary libraries using pip:`

```bash
 pip install pyTelegramBotAPI mysql-connector-python
```

#### 3. `Configure your config.py file with your Telegram bot token and your database details:`

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


#### 4. `Ensure you have the database set up and accessible via the functions in db/queries.py.`

### Database Configuration

To set up the database, make sure you have a MariaDB database installed and running. Then, create the necessary tables:

### `versions`
| Field       | Type         | Null | Key | Default | Extra          |
| ---         | ---          |---   |---  |---      |---             |
| id_version  | int(11)      | NO   | PRI | NULL    | auto_increment |
| version     | int(11)      | NO   |     | NULL    |                |
| description | varchar(255) | NO   |     | NULL    |                |

### `cod_back`
| Field            | Type         | Null | Key | Default | Extra          |
| ---              | ---          |---   |---  |---      |---             |
| id_cod_back      | int(11)      | NO   | PRI | NULL    | auto_increment |
| code_back_number | int(11)      | NO   |     | NULL    |                |
| code_back_code   | varchar(255) | NO   |     | NULL    |                |

### `cod_front`
| Field        | Type         | Null | Key | Default | Extra          |
| ---          | ---          |---   |---  |---      |---             |
| id_cod_front | int(11)      | NO   | PRI | NULL    | auto_increment |
| code_front   | varchar(255) | NO   |     | NULL    |                |

### `funko`
| Field        | Type         | Null | Key | Default | Extra          |
| ---          | ---          |---   |---  |---      |---             |
| id_funko     | int(11)      | NO   | PRI | NULL    | auto_increment |
| name         | varchar(255) | NO   |     | NULL    |                |
| collected    | tinyint(1)   | YES  |     | NULL    |                |
| id_version   | int(11)      | YES  | MUL | NULL    |                |
| id_cod_front | int(11)      | YES  | MUL | NULL    |                |
| id_cod_back  | int(11)      | YES  | MUL | NULL    |                |


These tables store information about Funko versions and the details of each Funko, respectively.


### Usage

- `/start` o `/inicio`: Displays a welcome message and the available commands.
- `/search` o `/busqueda`: Perform a complete search.
- `/funkos`: Shows a list of available Funkos along with their versions as interactive buttons.
- `/versions` o `/versiones`: Shows a list of available versions.
- `/frontcode` o `/codigofrontal`: Shows a list of available front codes as interactive buttons.
- `/backcode` o `/codigotrasero`: Shows a list of available back codes as interactive buttons.

### Execution

To run the bot, simply execute the `main.py` script:

```bash
 python3 main.py
```

### Contributions

Contributions are welcome. If you have any improvements or new functionality, feel free to fork the repository and submit a pull request.

### License

This project is licensed under the MIT License. For more details, see the `LICENSE` file.

---
Thank you for using Funko Kinder Bot! If you have any questions or issues, feel free to open an issue in the repository.
