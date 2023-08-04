# OLTP-CARD
Course python advances

# Nombre de tu proyecto
OLTP_CARD - bank

## Descripción
Este proyecto es una aplicación de simulación bancaria que permite gestionar usuarios, cuentas bancarias y tarjetas de débito. 
Proporciona una interfaz para realizar operaciones típicas de un banco, como crear cuentas, realizar transferencias y administrar tarjetas de débito.

## Características principales
- Registro de usuarios.
- Creación, edición y eliminación de cuentas bancarias.
- Asignación y administración de tarjetas de débito para cuentas bancarias.
- Realización de transferencias entre cuentas.
- Consulta de saldos y movimientos de cuentas.

## Tecnologías utilizadas
- Lenguaje de programación: Python.
- Framework o bibliotecas utilizadas: Django.
- Base de datos: sqlite.

## Instalación
1. Clona este repositorio en tu máquina local.
2. Crea tu ambiente virtual y activalo, con los siguientes comandos: 
- Windows: 
python -m venv venv
venv\Scripts\activate
- MAC:
python3 -m venv venv
source venv/bin/activate
3. Instala las dependencias necesarias utilizando el comando: pip install -r requirements.txt
4. Aplica las migraciones de los modelos de Django: 
- python manage.py makemigrations
- python manage.py migrate
5. Ejecuta la aplicación utilizando el comando: python manage.py runserver
6. Para hacer uso del proyecto requieres tener Postman y usar las peticiones de la collección "OLTP.json" dentro de este mismo proyecto.

## Uso
A continuación, se muestran algunas operaciones que puedes realizar con la aplicación:

1. Registro de usuarios: Para acceder a las funciones del banco, primero debes registrarte como usuario proporcionando la información requerida.

2. Creación de cuentas bancarias: Una vez registrado, puedes crear cuentas bancarias asociadas a tu perfil. Cada cuenta tendrá un número de cuenta único 
y un saldo inicial.

3. Asignación de tarjetas de débito: Puedes asignar una tarjeta de débito a una cuenta bancaria específica para facilitar el acceso a los fondos.

4. Transferencias de fondos: Utiliza la función de transferencia para mover fondos entre cuentas bancarias. Asegúrate de tener suficiente saldo en la cuenta 
de origen para completar la transferencia.

5. Consulta de saldos y movimientos: Puedes verificar el saldo actual de tus cuentas.

## Contribución
Si deseas contribuir a este proyecto, sigue los siguientes pasos:
1. Realiza un fork de este repositorio.
2. Crea una nueva rama para tu contribución.
3. Realiza los cambios y mejoras deseadas.
4. Envía un pull request describiendo tus cambios y su propósito.

## Créditos
Este proyecto ha sido desarrollado por 
- Ana Isabel Rodríguez González
- Carlos Arnulfo Gonzalez Rodriguez
- Jenifer Villa Díaz
- Lizeth Graciela Villa Díaz
- Oscar Martínez Armas
Agradecemos a Dios y a mis padres por su apoyo y contribuciones.

## Licencia
Este proyecto está bajo la Licencia ISC.

## Contacto
Si tienes preguntas, sugerencias o comentarios, puedes contactarnos en:
- anaisabelrg02@gmail.com
- c.arnulfogr@gmail.com
- jvilla414@accitesz.com
- lvilla415@accitesz.com
- oma_1506@hotmail.com
