from tkinter import *
from time import sleep

class Warteschlange:

    def __init__(self, master):
        self.queue = []
        self.master = master
        master.title("Warteschlange")
        master.geometry("1080x720")

        self.listpos = 0
        self.bestellwindowopen = False

        for i in range(5):
            master.columnconfigure(i, weight=1)
        for i in range(5):
            master.rowconfigure(i, weight=1)

        self.delete_bestellung = Button(master = self.master, text = "Bestellung Abgeschlossen", font=("Arial", 15, "bold"), bg = "gray", command = self.bestellung_fertig)
        self.delete_bestellung.grid(row=4, column=3, sticky="NSEW", pady = 10)

        self.add_Bestellung = Button(master = self.master, text = "Bestellung Hinzufügen", font=("Arial", 15, "bold"),bg = "gray", command = self.addbestellung)
        self.add_Bestellung.grid(row=4, column=1, sticky="NSEW", pady = 10)
        
        self.anzeige = Label(master = self.master, text = "Es liegen keine Bestellungen vor.", bg = "gray", font=("Arial", 15, "bold"))
        self.anzeige.grid(row=1, column=1, columnspan=3, rowspan = 2, sticky="NSEW")

        self.left = Button(master = self.master, text = "←", font=("Arial", 15, "bold"),bg = "gray",height = 1, width = 1, command = self.left)
        self.left.grid(row=1, column=0, sticky="NSEW", padx=(100, 10), pady = 130)

        self.right = Button(master = self.master, text = "→", font=("Arial", 15, "bold"),bg = "gray", command = self.right)
        self.right.grid(row=1, column=4, sticky="NSEW", padx=(10, 100), pady = 130)


    def addbestellung(self):
        if self.bestellwindowopen:
            self.add_Bestellung.config(bg="red")
            self.master.update_idletasks()
            sleep(0.2)
            self.add_Bestellung.config(bg="grey")
        else:
            self.bestellwindowopen = True
            global bestell_window
            bestell_window = Tk()
            bestell_window.geometry("800x600")
            bestell_window.title("Bestellung")
            bestell_window.protocol("WM_DELETE_WINDOW", lambda: None)

            global Bestellung
            Bestellung = []
            self.queue.append(Bestellung)
            quitbestmenu = Button(
                master=bestell_window,
                text="Bestellung Komplett",
                bg="gray",
                command=self.closebestwindow,
                font=("Arial", 14, "bold")
                )
            quitbestmenu.grid(row=3, column=0, columnspan=4, rowspan=1, sticky="NSEW", padx=100, pady=50)
            for i in range(4):
                bestell_window.columnconfigure(i, weight=1)
            for i in range(4):
                bestell_window.rowconfigure(i, weight=1)
            item_index = 0
            for i in range(3):
                for j in range(4):
                    item = Button(
                        master=bestell_window,
                        text=itemlist[item_index],
                        bg="gray",
                        font=("Arial", 15, "bold"),
                        command=lambda l=item_index: self.additem(l)
                    )
                    item.grid(row=i, column=j, padx=5, pady=5, sticky="NSEW")
                    item_index += 1
                
            
    def additem(self, item):
        Bestellung.append(itemlist[item])
        print(Bestellung)

    def closebestwindow(self):
        if len(Bestellung) == 0:
            self.queue.pop(-1)
            
        bestell_window.destroy()
        self.update_display()
        self.bestellwindowopen = False

        
        
        

    def list_bestitems(self):
        """
        if self.checkwarteschlange() == False:
            return "Es liegen keine Bestellungen vor"
        else:
            return "\n".join(f"-> {item}" for item in self.queue[self.listpos])
        """
        return "\n".join(f"-> {item}" for item in self.queue[self.listpos])

    def bestellung_fertig(self):
        if self.checkwarteschlange():
            self.listpos = 0
            self.queue.pop(0)
            self.update_display()
            self.update_display()
            #self.anzeige.config(text=self.list_bestitems())

    def update_display(self):
        if self.checkwarteschlange() == False:
            self.anzeige.config(text="Es liegen keine Bestellungen vor")
        else:
            self.anzeige.config(text=self.list_bestitems()+ f"\n{self.listpos + 1}/{len(self.queue)}")


    def checkwarteschlange(self):
        if len(self.queue) == 0:
            print("yes")
            return False
        else:
            print("No")
            return True

    def left(self):
        if self.listpos == 0:
            self.left.config(bg = "red")
            self.master.update_idletasks()
            sleep(0.2)
            self.left.config(bg="grey")
        elif self.checkwarteschlange():
            self.listpos -= 1
            self.update_display()

    def right(self):
        if self.listpos == len(self.queue)-1:
            self.right.config(bg = "red")
            self.master.update_idletasks()
            sleep(0.2)
            self.right.config(bg="grey")
        elif self.checkwarteschlange():
            self.listpos += 1
            self.update_display()



"""
    def bestellung_anzeigen(self):
        self.anzeige = Label(master = self.master, text = self.list_bestitems(), bg = "gray", font=("Arial", 15, "bold"))
        self.anzeige.grid(row=2, column=2, columnspan=2, sticky="NSEW")
"""


itemlist = ["Hamburger", "Cheeseburger", "Bacon-Burger", "Chickenburger", "French Fries", "Chicken Wings", "Chicken Nuggets", "Hot Dog", "Root Beer", "Fanta", "Coca Cola", "Sprite"]
liste1 = ["Fries", "Burger", "Coca Cola"]
liste2 = ["Burger", "Coca Cola"]
liste3 = ["Chickenburger", "Coca Cola"]



#addbestellung(liste1 = [1, 2])




window = Tk()
warteschlange1 = Warteschlange(window)
#warteschlange1.bestellung_anzeigen()
window.mainloop()
