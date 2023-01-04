import matplotlib.pyplot as plt
import numpy



def collatz(hailstone_number):
    with open('sequence.txt','a') as f: 
        f.write(str(hailstone_number)+"\n")

    while(hailstone_number != 1):
        with open('sequence.txt','a') as f:
            if(int(hailstone_number) % 2 == 0):
                hailstone_number = int(hailstone_number)/2
                f.write(str(hailstone_number)+"\n")
            else:
                hailstone_number= 3*int(hailstone_number) + 1
                f.write(str(hailstone_number)+"\n")

    with open("sequence.txt","r") as f:                                             #open text file in read only mode
        dataStr = f.read().split("\n")                                              #seperated by spaces
    dataStr = [str(i) for i in dataStr]                                             #to string
    dataStr.pop(len(dataStr)-1)                                                     #last "\n" removed
    Data = [float(i) for i in dataStr]  
    print("Sequence is as follows: ", Data, "\nIt has a length of: ", len(Data))
    return Data

def plotHailstone(Data):
    fig, ax = plt.subplots()
    for index,a in enumerate(Data):
        
        if(index + 1 <len(Data) ):b = Data[index+1]
        
        x = numpy.linspace(a, b, 100)
        y = abs(-(x-a)*(x-b))        
        ax.set_xlim(min(Data)-1,max(Data)+1)
        ax.plot(x,y,"black")
        
    ax.set_ylim
    plt.savefig('conjecture.png')
    plt.show()

if __name__ == "__main__":
    with open('sequence.txt','w') as f:
        f.truncate(0)
    Data = collatz(input("Enter any Positive number: "))
    plotHailstone(Data)
