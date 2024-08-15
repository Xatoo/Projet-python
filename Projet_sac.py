
from tkinter import *
from random import randint

def b1(B1,B2,B3,fenetre,t1, BN1, BN2, BN3):

    B1.destroy()
    B2.destroy()
    B3.place(x= 910, y= 630)
    t1.config(text= "")
    t1.config(text= "Choisissez un sac :")
    BN1.place(x=700 , y=500)
    BN2.place(x=900 , y=500)
    BN3.place(x=1100 , y=500)

def b2(fenetre, j):
    j[0]=1
    fenetre.destroy()



def s1(BN1, BN2, BN3, n,t1, fenetre):
    BN1.destroy()
    BN2.destroy()
    BN3.destroy()
    t1.destroy()

    txt1 = Label(fenetre, text = "Vous avez choisi le sac 1", \
    font = ("Comic_Sans_MS", 20), bg = "#B7CEEB")
    txt1.pack(expand = YES)
    n[0]+=0



def s2(BN1, BN2, BN3, n,t1, fenetre):
    BN1.destroy()
    BN2.destroy()
    BN3.destroy()
    t1.destroy()

    txt2 = Label(fenetre, text = "Vous avez choisi le sac 2", \
    font = ("Comic_Sans_MS", 20), bg = "#B7CEEB")
    txt2.pack(expand = YES)
    n[0]+= 1

def s3(BN1, BN2, BN3, n,t1, fenetre):
    BN1.destroy()
    BN2.destroy()
    BN3.destroy()
    t1.destroy()
    txt3 = Label(fenetre, text = "Vous avez choisi le sac 3", \
    font = ("Comic_Sans_MS", 20), bg = "#B7CEEB")
    txt3.pack(expand = YES)
    n[0]+= 2



def b3(score,fenetre,n, gain,sac):
    sac += repartition()

    if len(sac[n[0]])>len(sac[(n[0]+1)%3]) and len(sac[n[0]])>len(sac[(n[0]+2)%3]):
        gain[0] += 1
        score[0] +=1
    if 9 in sac[n[0]]:
        gain[0] += 1
        score[0] += 1
    if gain[0] == 0:
        score[0] -= 1
        gain[0] = -1
    fenetre.destroy()



def repartition():
    sac = []
    for i in range(3):
        sac.append([])
    nbre_chiffres = [0, 0, 0]
    i = randint(1, 6)
    nbre_chiffres[0] = i
    j = randint(1, 8-i)
    while j==i or 9-i-j==i or 9-i-j==j:
        j = randint(1, 8-i)
    nbre_chiffres[1] = j
    nbre_chiffres[2] = 9-i-j
    chiffres_pris = []
    for i in range(3):
        for j in range(nbre_chiffres[i]):
            k = randint(1, 9)
            while k in sac[i] or k in chiffres_pris:
                k = randint(1, 9)
            sac[i].append(k)
            chiffres_pris.append(k)
    return sac


def main():

    score=[0]
    gain=[0]
    sac=[]
    j=[0]
    while j[0] ==0 :
        n=[0]

        fenetre= Tk()
        fenetre.title("jeu du meilleur sac")
        fenetre.geometry("1920x1080")
        fenetre.minsize(1920, 1080)
        fenetre.config(background = "#B7CEEB")

        Ti = Label(fenetre, text = "Jeu du Meilleur Sac", \
        font = ("Comic_Sans_MS", 37), bg = "#B7CEEB")
        #Ti.pack(expand = YES)
        Ti.place(x=710, y=100)

        t1 = Label(fenetre, text = "Nouvelle partie ?", \
        font = ("Comic_Sans_MS", 25), bg = "#B7CEEB")
        #t1.pack(expand = YES)
        t1.place(x= 830, y = 200)
        t2 = Label(fenetre, text = "", \
        font = ("Comic_Sans_MS", 20), bg = "#B7CEEB")

        t3 = Label(fenetre, text = "score :"+ str(score[0]), \
        font = ("Comic_Sans_MS", 20), bg = "#B7CEEB")
        t3.place(x=150,y=840)




        B1 = Button (fenetre, text = "jouer" ,width = 20, height = 2, bg='#58FA58')
        B1.bind('<1>', lambda e: b1(B1,B2,B3,fenetre,t1, BN1, BN2, BN3))
        #B1.pack(expand = YES)
        B1.place(x=800,y = 500 )


        B2 = Button (fenetre, text = "quitter", width = 20, height = 2, bg='#FE2E2E')
        B2.bind('<1>', lambda e: b2(fenetre, j))
        #B2.pack(expand = YES)
        B2.place(x=1030,y = 500 )



        B3 = Button (fenetre, text = "ok",width = 20, height = 2, bg='#00FF00')
        B3.bind('<1>', lambda e: b3(score,fenetre,n, gain, sac))


        BN1 = Button (fenetre, text = "Sac 1",width = 20, height = 2)
        BN1.bind('<1>', lambda e: s1(BN1, BN2, BN3, n,t1, fenetre))

        BN2 = Button (fenetre, text = "Sac 2",width = 20, height = 2)
        BN2.bind('<1>', lambda e: s2(BN1, BN2, BN3, n,t1, fenetre))

        BN3 = Button (fenetre, text = "Sac 3",width = 20, height = 2)
        BN3.bind('<1>', lambda e: s3(BN1, BN2, BN3, n,t1, fenetre))

        t4 = Label(fenetre, text = "gain : "+ str(gain[0]), \
        font = ("Comic_Sans_MS", 20), bg = "#B7CEEB")
        t4.place(x=150,y=880)

        t5 = Label(fenetre, text = "Le contenu des Sacs : " + str(sac), \
        font = ("Comic_Sans_MS", 20), bg = "#B7CEEB")
        t5.place(x=150,y=920)

        gain=[0]
        sac=[]


        fenetre.mainloop()


if __name__ == "__main__":
    main()