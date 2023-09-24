import requests
import csv
from random import randint
import socket, select
from time import gmtime, strftime
import base64
import os

#unix socket request vanuit laravel factory?
#daarin vraagt laravel om een geslacht 
# hij zoekt in de csv file naar een item met het geslacht
# en upload de foto
# verwijdert de bijhorende csv line
# verwijdert de bijhorende plaatje
# is er geen foto met die geslacht dan run je de scraper
# en je check je nog een keer lukt het nog steeds niet herhaal je het

def search_gender(gender):
    with open('img/data.csv', 'r') as f, open('img/data_temp.csv', 'w') as f2:
        for row in f.readlines():
            columns = row.split(',')
       
            if len(columns) != 2:
                continue #bad data
            #print(columns[1])
            try:
                if gender in columns[1]:
                    print("here")
                    #remove line from csv
                    writer = csv.writer(f2)
                    writer.writerow(row)
                    os.rename('img/data_temp.csv', 'img/data.csv')
                    return columns[0]
                   
                    
            except:
                continue #bad data


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
    connection, client_address = sock.accept()
    while True:
        try:
            data=connection.recv(600000).decode()
            if not data:
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
        finally:
            connection.send(rM)
        if data.split(' ')[0] == "QUIT":
            quit(connection)
            break


if __name__ == '__main__':
    main()
