import machine
import socket
import utime
import network
import time
import dht

myLed = machine.Pin('LED',machine.Pin.OUT)
myLed.value(1)

ssid = '...'
password = '...'

wlan = network.WLAN(network.STA_IF)
wlan.active(True)
wlan.connect(ssid, password)
 

sensor = dht.DHT11(machine.Pin(16))

 
# Wait for connect or fail
wait = 10
while wait > 0:
    if wlan.status() < 0 or wlan.status() >= 3:
        break
    wait -= 1
    print('waiting for connection...')
    time.sleep(1)
 
# Handle connection error
if wlan.status() != 3:
    raise RuntimeError('wifi connection failed')
else:
    print('connected')
    ip=wlan.ifconfig()[0]
    print('IP: ', ip)


def webpage(temp, humid):
    html = f"""
            
            <!doctype html>
            <html lang="en">
              <head>
                <meta charset="utf-8">
                <meta name="viewport" content="width=device-width, initial-scale=1">
                <title>RGB LAMP</title>
                <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0-alpha3/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-KK94CHFLLe+nY2dmCWGMq91rCGa5gtU4mk92HdvYe+M/SXH301p5ILy+dN9+nJOZ" crossorigin="anonymous">
              </head>
              <body>
                <container class="p-2">
                <h1 class="text-center">Termometerrr</h1>
                <img src="https://www.thoughtco.com/thmb/ns8iAXaXV-PxWrdpXGQr6sETzb8=/1500x0/filters:no_upscale():max_bytes(150000):strip_icc()/thermometer-sun-high-degres--hot-summer-day--high-summer-temperatures-1010691618-2a5ca45876424dffbef441d73ae896b8.jpg" width="200px" class="rounded mx-auto d-block mb-2" alt="...">
                
                
               <div class="col mx-auto text-center">
       
                    <h3 class="text-body-secondary"> Temperature</h3>
                    <h1 class="fw-light">{temp} oC</h1>
                    
                    
                    <h3 class="text-body-secondary">  Humidity</h3>
                    <h1 class="fw-light"> {humid} %</h1>
                 
                  <a href="#" class="btn btn-success my-2" onclick="location.reload();">Refresh</a>
              </div>
      
      
                   
               
              
                </container>
                <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0-alpha3/dist/js/bootstrap.bundle.min.js" integrity="sha384-ENjdO4Dr2bkBIFxQpeoTz1HIcje39Wm4jDKdf19U8gI4ddQ3GYNS7NTKfAdVQSZe" crossorigin="anonymous"></script>
              </body>
            </html>
            
            
            """
    return html
 
def serve(connection):
    while True:
        client = connection.accept()[0]
        request = client.recv(1024)
        print(request)

        sensor.measure()
        temp = sensor.temperature()
        humid = sensor.humidity()
    
        html=webpage(temp,humid)
        client.send(html)
        client.close()
 
def open_socket(ip):
    # Open a socket
    address = (ip, 80)
    connection = socket.socket()
    connection.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    connection.bind(address)
    connection.listen(1)
    print(connection)
    return(connection)
 

try:
    if ip is not None:
        connection=open_socket(ip)
        serve(connection)
except KeyboardInterrupt:
    machine.reset()

