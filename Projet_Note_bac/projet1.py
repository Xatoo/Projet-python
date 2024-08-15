from tkinter import *




def lecture_note():
    resulats = [['histoire', 11, 3.33,],['Enseignement scientifique', 14.0, 2.5], #notes de premières
                ['Anglais', 11, 3.33], ['Espagnol', 13, 3.33],
                ['Spécialité Physique', 10.50,5],['Bulletin', 12.30, 5],
                ['Francais écrit', 11, 5], ['Francais Oral',11, 5]] 

     
    fich= open('notes.txt','r') 
   
    for ligne in fich:
        liste = ligne.split(",")
        if liste[1] != '':
            matiere = str(liste[0])
            note = float(liste[1])
            coef = float(liste[2])
            resulats.append([matiere,note,coef])
        
    
    fich.close()
    somme_notes = 0
    somme_coeff = 0
    for x in resulats:      
        somme_notes += float(x[1]) * float(x[2])
        somme_coeff += float(x[2])
    note_finale = round(somme_notes / somme_coeff, 2)
    
    
    note_bac = Label(fen, text = "La moyenne du bac est : " + str(note_finale) + ' /20', font = ("Comic_Sans_MS", 20), bg = "#3867d6")
    note_bac.place(x=1270, y=670)
    
   
def modif1(entry_histoire1, entry_emc, entry_eps1,entry_lva1,entry_lvb1, \
        entry_science1,entry_math, entry_phil,entry_nsi, entry_oral): 

    #Remplace les Entry par des Label + Enregistre les notes dans le fichier


    hist = entry_histoire1.get()
    emc = entry_emc.get() 
    eps = entry_eps1.get()
    esp = entry_lvb1.get()   
    ang = entry_lva1.get()
    sci= entry_science1.get()
    math = entry_math.get()
    nsi = entry_nsi.get()
    phil = entry_phil.get()
    oral = entry_oral.get()

    
    
    fic = open('notes.txt', 'r')
    data = fic.readlines()
    fic.close    
    
    
    data[0] = 'Histoire,' + str(hist) + ',3'
    data[1] = 'Enseignement scientifique,' + str(sci) + ',2.5'
    data[2] = 'Anglais,' + str(ang)+ ',3' 
    data[3] = 'Espagnol,' + str(esp) + ',3'
    data[4] = 'EPS,' + str(eps) + ',5'
    data[5] = 'EMC,' + str(emc) + ',1'
    data[6] = 'Spe Math,' + str(math) + ',16'
    data[7] = 'Spe NSI,' + str(nsi) + ',16'
    data[8] = 'Philosophie,' + str(phil) + ',8'
    data[9] = 'Grand Oral,' + str(oral) + ',10'
 
    
    fichier = open('notes.txt', 'w')
    ecrire(fichier, data)
    fichier.close()
    
    

    
    
    entry_histoire1.destroy()
    n9 = Label(fen, text=str(hist),width=4, height= 1) 
    n9.place(x=952,y=470 )
    
    entry_science1.destroy()
    n10 = Label(fen, text=str(sci),width=4, height= 1) 
    n10.place(x=952,y=500 )
    
    entry_lva1.destroy()
    n11 = Label(fen, text=str(ang),width=4, height= 1) 
    n11.place(x=952,y=530 )
    
    entry_lvb1.destroy()
    n12 = Label(fen, text=str(esp),width=4, height= 1) 
    n12.place(x=952,y=560 )
    
    entry_eps1.destroy()
    n13 = Label(fen, text=str(eps),width=4, height= 1) 
    n13.place(x=952,y=590 )     
    
    entry_emc.destroy()
    n14 = Label(fen, text=str(emc),width=4, height= 1) 
    n14.place(x=952,y=620 )
   
    entry_math.destroy()
    n15 = Label(fen, text=str(math),width=4, height= 1) 
    n15.place(x=952,y=650 )
   
    entry_nsi.destroy()
    n16 = Label(fen, text=str(nsi),width=4, height= 1) 
    n16.place(x=952,y=680)
    
    entry_phil.destroy()
    n17 = Label(fen, text=str(phil),width=4, height= 1) 
    n17.place(x=952,y=710 )
    
    entry_oral.destroy()
    n18 = Label(fen, text=str(oral),width=4, height= 1) 
    n18.place(x=952,y=740 )
    

   
    
    
    B4 = Button (fen, text = "Changer les notes", width = 20, height = 2)
    B4.bind('<1>', lambda e: affiche_page(B1))    
    B4.place(x=1080,y=600)   
    
    B5 = Button (fen, text = "Calculer la moyenne", width = 20, height = 2)
    B5.bind('<1>', lambda e: lecture_note())    
    B5.place(x=1080,y=670)   
    



def ecrire(fichier,contenu):  #Ecris dans le fichier txt
    for i in range(len(contenu)):
        fichier.write(contenu[i])
        fichier.write('\n')
    
    
    




def affiche_page(B1):  #Affiche les champs de saisie et Label (Matières)
    
    B3.destroy()
    B1.place(x=1530,y = 800 )
    
    #Notes connue de première 
    titre_premiere = Label(fen, text = "Notes de Première", font = ("Comic_Sans_MS", 20), bg = "#3867d6")
    titre_premiere.place(x=280,y=250)
    
    label_histoire = Label(fen, text=" Histoire : ",width=21, height= 1)
    label_histoire.place(x=300, y=500)
    n1 = Label(fen, text="11,00",width=4, height= 1) 
    n1.place(x=458,y=500 )
    
    label_spepremiere = Label(fen, text=" Spécialité Physique : ", width=21, height= 1)
    label_spepremiere.place(x=300, y=470)
    n2 = Label(fen, text="10,50",width=4, height= 1) 
    n2.place(x=458,y=470 )
    
    label_science = Label(fen, text=" Enseignement scientifique : " ,width=21, height= 1)
    label_science.place(x=300, y=530)
    n3 = Label(fen, text="14,00",width=4, height= 1) 
    n3.place(x=458,y=530 )
    
    label_lva = Label(fen, text=" Anglais : ",width=21, height= 1)
    label_lva.place(x=300, y=560)
    n4 = Label(fen, text="11,00",width=4, height= 1) 
    n4.place(x=458,y=560 )
    
    label_lvb = Label(fen, text=" Espagnol : ",width=21, height= 1)
    label_lvb.place(x=300, y=590)
    n5 = Label(fen, text="13,00",width=4, height= 1) 
    n5.place(x=458,y=590 )
    
    label_fro = Label(fen, text=' Français Oral : ', width=21, height=1 )
    label_fro.place(x = 300, y=620)
    n6 = Label(fen, text="11,00",width=4, height= 1) 
    n6.place(x=458,y=620 )
    
    label_fre = Label(fen, text=' Français Ecrit : ', width=21, height=1 )
    label_fre.place(x = 300, y=650)
    n7 = Label(fen, text="11,00",width=4, height= 1) 
    n7.place(x=458,y=650 )
     
    label_bu = Label(fen, text=' Bulletin de première :', width=21, height=1 )
    label_bu.place(x = 300, y=680)
    n8 = Label(fen, text="12,30",width=4, height= 1) 
    n8.place(x=458,y=680 )
    

    #Notes de Terminale    
    
    titre_terminale = Label(fen, text = "Notes de Terminale", font = ("Comic_Sans_MS", 20), bg = "#3867d6")
    titre_terminale.place(x=810,y=250)
    
    label_histoire1 = Label(fen, text=" Histoire : ",width=21, height= 1)
    label_histoire1.place(x=794, y=470)
    entry_histoire1 = Entry(fen)
    entry_histoire1.place(x= 954,y= 470)
    
    label_science1 = Label(fen, text=" Enseignement scientifique : ",width=21, height= 1)
    label_science1.place(x=794, y=500)
    entry_science1 = Entry(fen)
    entry_science1.place(x= 954,y= 500)
    
    label_lva1 = Label(fen, text=" Anglais : ",width=21, height= 1)
    label_lva1.place(x=794, y=530)
    entry_lva1 = Entry(fen)
    entry_lva1.place(x= 954,y= 530)
    
    label_lvb1 = Label(fen, text=" Espagnol : ",width=21, height= 1)
    label_lvb1.place(x=794, y=560)
    entry_lvb1 = Entry(fen)
    entry_lvb1.place(x= 954,y= 560)
    
    label_eps1 = Label(fen, text=" EPS : ",width=21, height= 1)
    label_eps1.place(x=794, y=590)
    entry_eps1 = Entry(fen)
    entry_eps1.place(x= 954,y= 590)
    
    label_emc = Label(fen, text=" EMC : ",width=21, height= 1)
    label_emc.place(x=794, y=620)
    entry_emc = Entry(fen)
    entry_emc.place(x= 954,y= 620)
    
    label_math = Label(fen, text=" Spécialité Mathématique : ",width=21, height= 1)
    label_math.place(x=794, y=650)
    entry_math = Entry(fen)
    entry_math.place(x= 954,y= 650)
    
    label_nsi = Label(fen, text=" NSI : ",width=21, height= 1)
    label_nsi.place(x=794, y=680)
    entry_nsi = Entry(fen)
    entry_nsi.place(x= 954,y= 680)
    
    label_phil = Label(fen, text=" Philosophie : ",width=21, height= 1)
    label_phil.place(x=794, y=710)
    entry_phil = Entry(fen)
    entry_phil.place(x= 954,y= 710)
    
    label_oral = Label(fen, text=" Grand Oral : ",width=21, height= 1)
    label_oral.place(x=794, y=740)
    entry_oral = Entry(fen)
    entry_oral.place(x= 954,y= 740)
    
    B2 = Button (fen, text = "Enregistrer les notes", width = 20, height = 2)
    B2.bind('<1>', lambda e: modif1(entry_histoire1, entry_emc, entry_eps1,entry_lva1,entry_lvb1, \
        entry_science1,entry_math, entry_phil,entry_nsi, entry_oral))    
    B2.place(x=796,y=800)   




def quitter(fen):
    fen.destroy()
    

fen= Tk()

fen.title("Moyenne du Bac")
#fen.geometry("1920x1080")
fen.minsize(1920, 1080)
fen.config(background = "#45aaf2")

Ti = Label(fen, text = "Note du Bac", font = ("Comic_Sans_MS", 37) ,bg='#45aaf2')
Ti.place(x=810, y=100)

B1 = Button (fen, text = "quitter", width = 20, height = 2)
B1.bind('<1>', lambda e: quitter(fen))
B1.place(x=880,y = 700 )


B3 = Button(fen, text='Renseigner les notes', width='40', height='8')
B3.bind('<1>', lambda e: affiche_page(B1))
B3.place(x=810,y = 500 )

fen.mainloop()

L = ["fils de pute", " La mere de Naros",2,3,5,7,8,4,8,4,7]

print(L)