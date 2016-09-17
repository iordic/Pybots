# Pybots

Proyecto para crear una botnet con scripts muy simples.

## ControlServer
Script que se ejecuta y hace de servidor, recibe órdenes del script de control (Master.py) y las envía a los clientes (Bots). 
## Bot
Se usa en la máquina "víctima" y ejecuta los comandos que recibe del servidor, comandos del cmd windows.
## Master
Se conecta al servidor y envía los comandos introducidos por el usuario, que se ejecutan en todos los clientes bot conectados.

PD: Tiene el fallo de que no recibe la respuesta de los bots, no puede ver que muestran las víctimas al ejecutar el comando.
