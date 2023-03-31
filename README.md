# ECG-InnovaTec
Proyecto final de Telemedicina. Constituye un sistema de adquisición de datos por medio del microcontrolador ESP32 y el módulo AD8232, el cual enviará los datos de la señal ECG a un servidor para redireccionarlos a una página web y visualizar la gráfica en "tiempo real".

* Para ejecutar el servidor: Instalar Node JS para poder importar los módulos mediante el comando "npm install".
* La carpeta ecg contiene el archivo "ecg.ino" para programar el ESP32 mediante el IDE Arduino.

* Subir las carpetas "public" y "server" a la instancia de Google que tengan (pueden poner ambas carpetas en una carpeta de la instancia e instalen ahí node_modules con "npm install").
* El archivo package.json tiene las configuraciones para usar nodemon en caso de que lo usen. 
* La carpeta "TransmitirECGdeArchivoTxt" tiene el programa de python y el archivo txt de la señal, para transmitir un ecg de un archivo descargado.
