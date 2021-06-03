from tkinter import Tk, Frame, Label, Button 
from time import sleep

class Question:
    def __init__(self, question, answers, correctLetter):
        self.question = question
        self.answers = answers
        self.correctLetter = correctLetter

    def check(self, letter, view):
        global right
        if(letter == self.correctLetter):
            label = Label(view, text="Tunggu!")
            right += 1
        else:
            label = Label(view, text="Tunggu!")
        label.pack()
        view.after(500, lambda *args: self.unpackView(view))


    def getView(self, window):
        view = Frame(window)
        Label(view, text=self.question).pack()
        Button(view, text=self.answers[0], command=lambda *args: self.check("A", view)).pack()
        Button(view, text=self.answers[1], command=lambda *args: self.check("B", view)).pack()
        return view

    def unpackView(self, view):
        view.pack_forget()
        askQuestion()

def askQuestion():
    global questions, window, index, button, right, number_of_questions 
    if(len(questions) == index + 1):
        Label(window, text="Berdasarkan hasil analisa anda dinyatakan mengalami gejala covid tingkat:").pack()
        if (right == 3):
            Label(window, text="Serius!!!", fg='red', font="Times 20").pack()
            Label(window, text="Segeralah mencari bantuan medis!", font="20").pack()
            Label(window, text="Jangan lupa tetap patuhi protokol kesehatan 5M", font="20").pack()
        if (right == 2):
            Label(window, text="Sedang!!!", fg='red', font="Times 20").pack()
            Label(window, text="Anda cukup melakukan perawatan mandiri di rumah ", font="20").pack()
            Label(window, text="Dengan perbanyak mengonsumsi makanan yang sehat, perbanyak minum air putih dan meminum obat penurun demam", font="20").pack()
            Label(window, text="Jangan lupa tetap patuhi protokol kesehatan 5M", font="20").pack()
        if (right == 1):
            Label(window, text="Ringan!!!", fg='red', font="Times 20").pack()
            Label(window, text="Anda cukup melakukan perawatan mandiri di rumah", font="20").pack()
            Label(window, text="Dengan mengonsumsi makanan yang sehat dan meminum obat penurun demam", font="20").pack()
            Label(window, text="Jangan lupa tetap patuhi protokol kesehatan 5M", font="20").pack()            
        if (right == 0):
            Label(window, text="Tidak terdampak", fg='red', font="Times 20").pack()
            Label(window, text="Meskipun tidak ada gejala anda tetap harus menjaga imunitas tubuh dan perbanyak melakukan aktivitas olahraga", font="20").pack()
            Label(window, text="Agar terhindar dari gejala Covid-19", font="20").pack()
            Label(window, text="Jangan lupa tetap patuhi protokol kesehatan 5M", font="20").pack()            
        return window
    
    button.pack_forget()
    index += 1
    questions[index].getView(window).pack()

#pertanyaan
questions = []
file = open("questions.txt", "r")
line = file.readline()
while(line != ""):
    questionString = line
    answers = []
    for i in range (2):
        answers.append(file.readline())
    correctLetter = file.readline()
    correctLetter = correctLetter[:-1]
    questions.append(Question(questionString, answers, correctLetter))
    line = file.readline()
file.close()
index = -1
right = 0
number_of_questions = len(questions)

#Tittle
window = Tk()
window.geometry("800x400")
window.title("Aplikasi Sistem Pakar")
welcome=Label(window,text="Aplikasi Pendiagnosa Gejala Covid-19", bg='yellow', font="20").pack()

#button
button = Button(window, text="Start", command=askQuestion)
button.pack()

window.mainloop()
