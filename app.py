from tkinter import *
from tkinter import ttk
import re #Expresiones regulares
    #[0-9]+ Números de 0-9 en una o más repeticiones
    #[ \t\n\r\f] Espacio en blanco
    #[a-zA-Z_] Cualquier letra
    #\\ Para validar los caracteres literales de [ y ]
    #El resto son caracteres plenos -> :.,/


def clean():
    print("Cleaning")
    textCleaned = ""
    #Get text from text widget
    asd = T.get("1.0",'end-1c') #El get extrae un caracter adicional que es borrado con end-1c. Se le debe restar 1 al len
    #Configuration Regular Expressions
    p = re.compile('[^a-zA-Z\\s]') #Solo letras
    #Divide per lines
    asd2 = asd.split('\n')
    #Proccess each line
    for line in asd2:
        cleaned = p.sub('',line) #Sustitute everything that is not a letter or space with ''
        cleaned = cleaned.lstrip() #Remove initial spaces
        cleaned = cleaned.rstrip() #Remove final spaces
        textCleaned=textCleaned+cleaned+'\n' #Add cleaned line to final text
    textCleaned = textCleaned.rstrip() #Remove final \n

    #Update the Text
    T.delete("1.0",END) #Delete all text
    T.insert(END, textCleaned) #Insert cleaned text

def delete():
    T.delete("1.0",END) #Delete all text

def copy():
    asd = T.get("1.0",'end-1c') #El get extrae un caracter adicional que es borrado con end-1c. Se le debe restar 1 al len
    root.clipboard_clear()
    root.clipboard_append(asd)
    root.update()

#Main :v
root = Tk()
frm = ttk.Frame(root, padding=100)
frm.grid()
ttk.Button(frm, text="Copy", command=copy).grid(column=1, row=0)
ttk.Button(frm, text="Clean", command=clean).grid(column=2, row=0)
ttk.Button(frm, text="Delete", command=delete).grid(column=2, row=1)

# Create text widget and specify size.
T = Text(frm, height = 5, width = 52)
T.grid(column=3, row=0)
T.insert(END, "Just a text Widget\nin two lines\n")


root.mainloop()


#Notas: Mejorar el nombre de las variables. Tal vez dividir en clases. Manejo de errores. 
