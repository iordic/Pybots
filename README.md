# Pybots

Proyecto para crear una botnet con scripts muy simples.

## ControlServer
Script que se ejecuta y hace de servidor, recibe órdenes del script de control (Master.py) y las envía a los clientes (Bots). 
## Bot
Se usa en la máquina "víctima" y ejecuta los comandos que recibe del servidor, comandos del cmd windows.
## Master
Se conecta al servidor y envía los comandos introducidos por el usuario, que se ejecutan en todos los clientes bot conectados.

### Fallos:
* No recibe la respuesta de los bots al ejecutar el comando. Con lo que:
    * No se puede ver una lista de ficheros de la víctima.
    * No se puede saber si el comando se ha ejecutado correctamente.
    * Etc.
* Si se reinicia el servidor, el bot no se reconecta.
* Falta por definir la función "recfile" que en un principio estaba ideada para que las víctimas descargaran ficheros directamente desde el servidor. Si se esta trabajando en linux se puede usar el comando "wget".

```
**Este repositorio fue un pequeño apartado de un proyecto final de FP y se ha dejado de lado.**
```
