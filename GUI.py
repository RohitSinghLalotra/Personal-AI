from tkinter import *
from PIL import Image,ImageTk
import speech_to_text 
import action
from text_to_speech import text_to_speech 
root = Tk()
root.title("AI Assisstant")
root.geometry("600x680")
root.resizable(False , False)                            #false so that we cannot resize width and height
root.config(bg="#6F8FAF")


#ask function

def ask():
     user_val = speech_to_text.speech_to_text()
     bot_val = action.Action(user_val)
     text.insert(END , 'User--->'+ user_val+"\n")
     if bot_val != None:
        text.insert(END ,"BOT <----"+str(bot_val)+"\n")
     if bot_val == "ok sir":
        root.destroy()



# delete function
def del_text():
    print("Text delete")

#send function

def send():
    user_val = entry.get()

    if user_val.strip() == "":
        return     # do nothing if empty

    # show user message
    text.insert(END, "User ---> " + user_val + "\n")

    # get bot reply
    bot_val = action.Action(user_val)

    if bot_val is not None:
        text.insert(END, "BOT <--- " + str(bot_val) + "\n")

    entry.delete(0, END)   # clear text box

    # close app if needed
    if bot_val == "ok sir":
        root.destroy()


#frame


frame = LabelFrame(root, padx=100, pady=8, borderwidth=3 ,relief="raised")
frame.config(bg="#6F8FAF")
frame.grid(row=0 ,column=1, padx=55, pady=10)

#text label

text_label = Label(frame, text= "AI ASSISTANT", font=("comic Sans ms" ,14, "bold") ,bg="#356696")
text_label.grid(row=0, column =0,  padx=20 , pady=10)


#image

image= ImageTk.PhotoImage(Image.open("Assiss.jpeg"))
image_label= Label(frame , image= image)
image_label.grid(row=1, column =0, pady=20)

#Addidng a text  widget


text = Text(root, font= ('courier  10  bold') , bg="#356696")
text.grid(row = 2, column= 0)
text.place(x= 120 , y= 330 , width =400 ,height =120)


#entry visit

entry = Entry(root , justify= CENTER)
entry.place(x= 100, y= 500, width= 450,height=30)


#button 1

Button1= Button(root, text="ASk", bg="#356696", padx=40 ,pady=16 , borderwidth=3, relief= SOLID , command= ask)
Button1.place(x=70 ,y= 575)

Button2= Button(root, text="DELETE", bg="#356696", padx=40 ,pady=16 , borderwidth=3, relief= SOLID , command= del_text)
Button2.place(x= 240 ,y= 575)

Button3= Button(root, text="SEND", bg="#356696", padx=40 ,pady=16 , borderwidth=3, relief=SOLID , command= send)
Button3.place(x= 430 ,y= 575)







root.mainloop()