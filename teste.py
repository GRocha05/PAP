import tkinter as tk
import timer


def after():
    n = input()
    if n == '1':
        root.destroy()


root = tk.Tk()  

root.overrideredirect(True) 

# Make the window transparent
root.attributes("-alpha", 0.3)  

# Make the window stay on top of other windows
root.attributes("-topmost", True)   

root.after(0, after())

root.mainloop()



quit()

root = tk.Tk()

# Disable decoration of the window
root.overrideredirect(True)

# Make the window transparent
root.attributes("-alpha", 0.5)

# Set the window geometry to match the screen
root.geometry("{}x{}+0+0".format(root.winfo_screenwidth(), root.winfo_screenheight()))
#os 2 primeiros são as dimensoes e os 2 ultimos são a posição(ex: a posição vai ser 0,0)
#as dimensoes vao ser as dimensoes do ecrã no .format




root.mainloop()

n = input('teste')

if n == '1':    
    print("fechado")
    root.quit()