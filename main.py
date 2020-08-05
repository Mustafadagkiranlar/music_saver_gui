import csv
import time

no_of_song = 0
no_of_song_add = 0 
name_of_song = ""
singer = ""

togle = True

def item_no_check():

    global no_of_song

    with open('data.csv', newline='') as data:
        data_reader = csv.DictReader(data) #use DictReader for list the used headers.
        for line in data_reader:
            no_of_song = no_of_song + 1
    #print(no_of_song)

def increment():
    global no_of_song
    no_of_song = no_of_song + 1

def get_song():

    global no_of_song, name_of_song, singer ,no_of_song_add

    no_of_song_add = no_of_song + 1

    name_of_song = input("Please enter name of %s. Song: " % no_of_song_add)
    singer = input("Please enter name of %s. Singer: " % no_of_song_add)


def data_writer():

    with open('data.csv', 'a', newline='') as data:
        fieldnames = ['No','Name','Song']
        writer = csv.DictWriter(data, fieldnames=fieldnames)
        writer.writerow({'No': str(no_of_song_add), 'Name': singer, 'Song': name_of_song})

def show_all():
    #after program work finis print all the music list
    with open('data.csv', newline='') as data:
        data_reader = csv.DictReader(data) #use DictReader for list the used headers.
        for line in data_reader:
            print(line)

### Main ###

item_no_check()

while togle:

    get_song()
    data_writer()

    q = input("Do you want to continue? [y/n]: ")

    if q == "y":
        increment()
        pass
    else:
        togle = False
        show_all()
        #print("Program Closing")
        #time.sleep(0.3)
        #print("Program Closing.")
        #time.sleep(0.3)
        #print("Program Closing..")
        #time.sleep(0.4)
        
