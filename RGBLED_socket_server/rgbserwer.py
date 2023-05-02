import machine
import socket
import math
import utime
import network
import time
 
ssid = '...'
password = '...'

wlan = network.WLAN(network.STA_IF)
wlan.active(True)
wlan.connect(ssid, password)
 
# rgb led
red=machine.Pin(15,machine.Pin.OUT)
green=machine.Pin(14,machine.Pin.OUT)
blue=machine.Pin(13,machine.Pin.OUT)
 
red.high()
green.high()
blue.high() 
 
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


def webpage():
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
                <h1 class="text-center">Lamp controler</h1>
                <img src="https://www.silentiumpc.com/wp-content/uploads/2021/07/ico-illumination-rgb-200px-2021.png" width="200px" class="rounded mx-auto d-block mb-2" alt="...">
                <form class="row" action="./white">
                <div>
                <input class="form-control" type="submit" value="white " />
                </div>
                </form>
                
                <form class="row" action="./red">
                <div>
                <input class="form-control" type="submit" value="red " />
                </div>
                </form>
                
                <form class="row"  action="./green">
                <div>
                <input class="form-control" type="submit" value="green" />
                </div>
                </form>
                
                <form class="row"  action="./blue">
                <div>
                <input class="form-control" type="submit" value="blue" />
                </div>
                </form>
                
                <form class="row"  action="./off">
                <div>
                <input class="form-control" type="submit" value="off" />
                </div>
                </form>
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
        request = str(request)
        try:
            request = request.split()[1]
        except IndexError:
            pass
        
        print(request)
        
        if request == '/off?':
            red.high()
            green.high()
            blue.high()
        elif request == '/white?':
            red.low()
            green.low()
            blue.low()    
        elif request == '/red?':
            red.low()
            green.high()
            blue.high()
        elif request == '/green?':
            red.high()
            green.low()
            blue.high()
        elif request == '/blue?':
            red.high()
            green.high()
            blue.low()
 
        html=webpage()
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