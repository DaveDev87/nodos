import threading


def contar1():
    cont = 0
    while cont<100:
        print("1.- ",cont)
        cont=cont+1



def contar2():
    cont = 0
    while cont<100:
        print("2.- ",cont)
        cont=cont+1

hilo1 = threading.Thread(target=contar1)
hilo2 = threading.Thread(target=contar2)

hilo1.start()
hilo2.start()