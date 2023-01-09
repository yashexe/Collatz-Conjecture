import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import numpy as np
from tkinter import *
import customtkinter
from PIL import Image

class CollatzGUI:
    def __init__(self,root):

        customtkinter.set_appearance_mode("System")  # Modes: system (default), light, dark
        customtkinter.set_default_color_theme("blue")  # Themes: blue (default), dark-blue, green

        self.root = root

        self.root.title("Collatz GUI")

        self.root.geometry("500x500")
        self.root.minsize(320,425)
        
        self.num = 1

        label = customtkinter.CTkLabel(self.root, text="Enter a positive integer:")
        label.pack(anchor='center')


        self.text_box = customtkinter.CTkEntry(self.root)
        self.text_box.pack(anchor='center')
   

        self.output_label = customtkinter.CTkLabel(self.root, text="")
        self.output_label.pack(anchor='center')
  

        button = customtkinter.CTkButton(self.root, text="Generate Sequence", command=self.onButtonClick)
        button.pack(anchor='center')

        image = customtkinter.CTkImage(dark_image=Image.open("Graph.png"), size=(300,300))
        image_label = customtkinter.CTkLabel(self.root,image= image, text="")
        image_label.pack(anchor='center')

        self.root.bind("<Return>", self.onButtonClick)

        pass

    def onButtonClick(self,event= None):

        try:
            self.num = int(self.text_box.get())

            self.output_label.configure(text=" ")

            if self.num <= 0: raise ValueError

        except ValueError:
            self.output_label.configure(text="Invalid input")

            return self.num
        
        self.plotAll(self.num)

        return None

    def plotAll(self,num):
        Data = self.collatz(num)

        print("Sequence is as follows: ", Data, "\nIt has a length of: ", len(Data))
        print("Plotting Sequences...")

        self.plotSingularX(Data)
        self.plotSingularY(Data)

        if len(Data) == 1: print("1 is the only number... ")
        else:
            self.plotSingularBar(Data)
            self.plotSequenceLength(num)
            self.plotMultipleY(num)


    def collatz(self,num):

        Data = [num]

        while num != 1:
            num = [3*num + 1, num/2][num % 2 == 0]
            Data.append(num)

        return Data


    def plotSingularX(self,Data):
        fig, ax = plt.subplots()

        ax.plot(Data[0],0, color = 'black', marker = 'o', markersize=4)#first number

        if len(Data)==1:                                            #input of 1
            ax.set_xlim(0,5)
            ax.set_ylim(0,5)

            # plt.savefig('conjectureX.png')

            plt.show()
            return

        for index,a in enumerate(Data):                             # input of integer greater than 1

            if(index + 1 <len(Data) ):b = Data[index+1]
            
            x = np.linspace(a, b, 100)
            y = abs(-(x-a)*(x-b))     

            ax.set_xlim(min(Data)-1,max(Data)+1)
            ax.plot(x,y,"black")
            
        ax.set_ylim

        plt.title('X-Axis Representation of Singular Collatz Sequence')

        # plt.savefig('conjectureX.png')

        plt.show()


    def plotSingularY(self,Data):

        index = []

        for i in range(len(Data)):
            index.append(i)
            plt.plot(i,Data[i],'o', markersize=4)

        plt.plot(index,Data)
        
        plt.title("Y-Axis Representation of Singular Collatz Sequence")

        # plt.savefig('conjectureY.png')

        plt.show()


    def plotSingularBar(self,Data):

        if len(Data) == 1: return

        bar = {}

        for element in (Data):
            if element in bar: bar[element]+= 1
            else: bar[element] = 1

        for element in bar: plt.bar(str(element),element)

        if len(bar) <=25:
            for i, v in enumerate(bar): plt.text(i-0.15, v+0.25, str(v))

        plt.title('Bar Graph Representation of Singular Collatz Sequence')

        # plt.savefig('conjecture_bar.png')

        plt.show()


    def plotSequenceLength(self,num):

        plt.clf()

        for i in range(1,num+1): 
            plt.bar(str(i),len(self.collatz(i)))
            plt.text(i-1.15,len(self.collatz(i))+0.25,str(len(self.collatz(i))))

        plt.title('Length of Collatz Sequences up to ' + str(num))

        # plt.savefig('conjecture_lengths.png')

        plt.show()


    def plotMultipleY(self,num):
        
        plt.plot(0,1, marker = 'o', markersize=4)         
        
        for i in range(1,num+1):
            newCollatz = self.collatz(i)
            index=[]

            for j in range(len(newCollatz)):index.append(j)

            plt.plot(index,newCollatz)

        plt.title("Y-Axis Representation of Multiple Collatz Sequences")

        # plt.savefig('conjecturesY.png')

        plt.show()


if __name__ == "__main__":

    root = customtkinter.CTk()
    gui= CollatzGUI(root)

    gui.root.mainloop()




