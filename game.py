current = [7]
human = False
com = False
pos = True

def error():
    print("Error")

def tampilan_awal():
    print("Welcome to NIM Games")

def proses(pick):
    # x = len(current)
    # current[x-1] -= pick
    # current.append(pick)
    maksimal = max(current)
    i = current.index(maksimal)
    if(current[i]-pick == pick):
        error()
    else:
        current[i] -= pick
        current.append(pick)

def human(pick):
    proses(pick)
    human = True
    com = False
    pos = True

def nim_move():
    if pos == True:
        bot(2)
    else:
        bot(1)

def bot(bil):
    proses(bil)
    human = False
    com = True
    pos = False
    print("Com pick a number : ", bil)


def cek_selesai():
    for i in range(len(current)):
        if current[i] > 2:
            return False
            break
    return True


def main():
    selesai = False
    tampilan_awal()
    while(selesai == False):
        if cek_selesai() == False:
            print("\nCurrent State", current)
            pick = int(input("Human pick a number : "))
            proses(pick)
        else:
            selesai = True
        if cek_selesai() == False:
            print("\nCurrent State", current)
            nim_move()
        else:
            selesai = True
    if(human == True):
        print("\nHuman Win")
    else:
        print("\nCom Win")

if __name__ == "__main__":
    main()