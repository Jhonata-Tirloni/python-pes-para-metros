from tkinter import *
from tkinter import ttk

#Função usada para converter os valores
#Function for converting the values
def Calcular(*args):
    try:
        valor = float(pes.get())
        metros.set(int(0.3048 * valor * 10000.0 + 0.5)/10000.0)
    except ValueError:
        pass

root = Tk()
root.title("Pés para Metros - Feet to Meters")
root.geometry('342x97')

#Design da aplicação, em uma Grid de 3 colunas e 3 linhas
#Application design with a grid of 3x3 (columns and lines)
mainframe = ttk.Frame(root, padding="3 3 12 12")
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

#Declaração de variáveis para recebimento de valores da função de calculo
#Variables for receiving the values used on the convertion
pes = StringVar()
pes_entry = ttk.Entry(mainframe, width=7, textvariable=pes)
pes_entry.grid(column=2, row=1, sticky=(W, E))

metros = StringVar()
ttk.Label(mainframe, textvariable=metros).grid(column=2, row=2, sticky=(W, E))


#Botão "Calcular"
#"Calculate" button
ttk.Button(mainframe, text="Calcular", command=Calcular).grid(column=3, row=3, sticky=W)

#Labels de valores e texto da aplicação
#Text labels on the application
ttk.Label(mainframe, text="pés").grid(column=3, row=1, sticky=W)
ttk.Label(mainframe, text="equivale a").grid(column=1, row=2, sticky=E)
ttk.Label(mainframe, text="metros").grid(column=3, row=2, sticky=W)

for child in mainframe.winfo_children(): 
    child.grid_configure(padx=5, pady=5)

pes_entry.focus()
root.bind("<Return>", Calcular)

root.mainloop()

