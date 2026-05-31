import tkinter as tk







class myapps:
    def __init__(self,root:tk.Tk,titles:str,w:int,h:int,backgrounds:str,steps:int,colors:str):
        self.root=root
        self.root.title(titles)
        self.root.geometry(str(w)+"x"+str(h))
        self.root.configure(background=backgrounds)
        self.canvas = tk.Canvas(background=backgrounds,width=w,height=h)
        self.canvas.pack(padx=0,pady=0)
        c=self.canvas
        for a in range(0,w,steps*4):
            
            
            c.create_rectangle(a,0,a+steps,h,fill=colors)
        for a in range(0,h,steps*4):
            
            
            c.create_rectangle(0,a,w,a+steps,fill=colors)




def starts(titles:str,w:int,h:int,backgrounds:str,steps:int,colors:str):
    root=tk.Tk()
    apps=myapps(root,titles,w,h,backgrounds,steps,colors)
    root.mainloop()



starts("rets",640,480,"black",20,"white")