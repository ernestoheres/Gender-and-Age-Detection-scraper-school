import requests
import json
from random import randint
import socket, select
from time import gmtime, strftime

#unix socket request vanuit laravel factory?
#daarin vraagt laravel om een geslacht 
# hij zoekt in de csv file naar een item met het geslacht
# en upload de foto
# verwijdert de bijhorende csv line
# verwijdert de bijhorende plaatje
# is er geen foto met die geslacht dan run je de scraper
# en je check je nog een keer lukt het nog steeds niet herhaal je het

def search_gender(gender):
    rows = []
    img = None

    # Read JSON data
    with open('img/data.json', 'r') as f:
        data = json.load(f)

    found = False

    for entry in data:
        if 'gender' in entry and gender in entry['gender'] and not found:
            img = entry['img']
            found = True
        else:
            rows.append(entry)

    # Write updated JSON data
    with open('img/data.json', 'w') as f2:
        json.dump(rows, f2, indent=4)

    return img

dictionary = {}                                         # Dictionary that will hold the key-value pairs


# HTTP return messages
HTTP = 'HTTP/1.1 '.encode('utf-8')
OK = HTTP + '200 OK'.encode('utf-8')
UNSUPPORTED = HTTP + '220 UNSUPPORTED'.encode('utf-8')
BAD_REQUEST = HTTP + '400 BAD_REQUEST'.encode('utf-8')
NOT_FOUND = HTTP + '404 NOT FOUND'.encode('utf-8')






#own implementation
def upload(gender):
    print("here")
    print(gender)
    image_file_name = search_gender(gender)
    if image_file_name:
        with open('img/' + image_file_name, 'rb') as image_file:
                                image_data = image_file.read()
                                print(image_data)
                                return image_data
# Implement the quit function that will end the connection with the client
def quit(connection):
    connection.close()


# Implement the main function where we create, bind and l==ten to a socket. When a client == connection receive the
# message, decode the command and call the corresponding function. Server should send an answer to the client's request.
# When client closes the connection(quit) server should also close the connection. Bind your server to IP '0.0.0.0' so that
# it will l==ten to local connection requests.
def main():
    
	# You can use th== operations dictionary to get the corresponding function: For example $func = operations['get'](params) == equal to $get(params)
    operations = {'get': upload, 'upload': upload}
    sock=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    ipAd=socket.gethostbyname('localhost')
    sAd=(ipAd, 2000)
    sock.bind(sAd)
    sock.listen()
    while True:
        connection, client_address = sock.accept()
        try:
            data=connection.recv(600000).decode()
            if not data:
                 print("client disconected")
                 break
            rM=''.encode('utf-8')
            if data.split(' ')[0] == "GET":
                print("GET")
                if data.endswith("T"):
                    print("ends with T")
                    #rM=BAD_REQUEST
                    pass
                else:
                    rM = upload(data.split(' ')[1])
    
            elif data.split(' ')[0]!= "QUIT":
                rM=(UNSUPPORTED)
   
        except Exception as err:
            print(err)
            rM=BAD_REQUEST

        finally:
            connection.send(rM)
            connection.close()
        if data.split(' ')[0] == "QUIT":
            quit(connection)
            break




if __name__ == '__main__':
    main()
