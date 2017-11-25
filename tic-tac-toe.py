from tkinter import *

def win() :
      if player == "X":
           print("O의 승리")
      if player == "O":
           print("X의 승리")
      sys.exit(1)

def checked(i) :
      global player
      button = list[i]

      if button["text"] != "     " :
            return
      button["text"] = player 
      button["bg"] = "yellow"
      
      if player == "X" :
            player = "O"
            button["bg"] = "yellow"
      else :
            player = "X"
            button["bg"] = "lightgreen"

      if list[0]["text"] == list[1]["text"] == list[2]["text"] != "     " : win()
      if list[3]["text"] == list[4]["text"] == list[5]["text"] != "     " : win()
      if list[6]["text"] == list[7]["text"] == list[8]["text"] != "     " : win()
      if list[0]["text"] == list[3]["text"] == list[6]["text"] != "     " : win()
      if list[1]["text"] == list[4]["text"] == list[7]["text"] != "     " : win()
      if list[2]["text"] == list[5]["text"] == list[8]["text"] != "     " : win()
      if list[0]["text"] == list[4]["text"] == list[8]["text"] != "     " : win()
      if list[2]["text"] == list[4]["text"] == list[6]["text"] != "     " : win()   

window = Tk()
player = "X"
list= []

for i in range(9) :
      b = Button(window, text="     ", command=lambda k=i: checked(k))
      b.grid(row=i//3, column=i%3)
      list.append(b)    

window.mainloop()


