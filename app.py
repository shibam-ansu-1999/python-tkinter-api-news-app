from tkinter import *
import requests
class News:

    def __init__(self):
        self.root=Tk()
        self.root.title("News application")
        self.root.minsize(400,400)
        self.root.maxsize(400,400)
        self.root.configure(background="#fff")

        self.label=Label(self.root,text="Our news 24*7",bg="white")
        self.label.configure(font=("Times", 20, "bold"))
        self.label.pack(pady=(10,30))

        self.label1 = Label(self.root, text="Enter the topic",bg="white")
        self.label1.configure(font=("Times", 15, "italic","bold"))
        self.label1.pack(pady=(10, 20))

        self.topic = Entry(self.root)
        self.topic.pack(pady=(0, 10), ipadx=40, ipady=5)

        self.search = Button(self.root, text="Search", bg="cyan",fg="Black",command=lambda :self.fetch())
        self.search.configure(font=("Times", 12))
        self.search.pack(pady=(8,10), ipadx=10, ipady=4)



        self.root.mainloop()

    def fetch(self):
        trem=self.topic.get()

        url="https://newsapi.org/v2/everything?q={}&apiKey=15bcbe3f5e854f0ebf1058c526a52932".format(trem)

        response= requests.get(url)
        self.response=response.json()
        #print(self.response)
        self.data = self.response['articles']
        self.extract()

    def extract(self, index=0):
        news = []
        news.append(self.data[index]['title'])
        news.append(self.data[index]['source']['name'])
        news.append(self.data[index]['description'])

        self.clear()
        self.display(news, index=index)

    def display(self, news, index):
        title = Text(self.root,fg="red")
        title.insert(INSERT,news[0])
        title.configure(font=("Times", 15),height=2)
        title.pack(pady=(10,25), padx=(2, 2))

        source = Label(self.root, text=news[1], fg="blue", bg="white")
        source.configure(font=("Times",15))
        source.pack(pady=(10,25), padx=(2, 2))

        desc = Text(self.root)
        desc.insert(INSERT,news[2])
        desc.configure(font=("Times",15),height=10)
        desc.pack(padx=(20,20))

        frame = Frame(self.root)
        frame.pack()

        if index != 0:
            previous = Button(frame, text="Previous", command=lambda: self.extract(index=index - 1))
            previous.pack(side="left")
        if index !=len(self.data)-1:
            next = Button(frame, text="Next", command=lambda: self.extract(index=index + 1))
            next.pack(side="right")

    def clear(self):
        for i in self.root.pack_slaves():
            i.destroy()




obj=News()