

from tkinter import *


class TkApp(object):
    def __init__(self):
        return
    
    def run(self):
        
        
        master = Tk()
        
        
        s = Scale(master, from_=-100, to=100,tickinterval=20, orient=HORIZONTAL)
        
        s.pack(fill='x', expand=1)
        
        mainloop()
        
        
        return


def main():
    import argparse
    
    parser = argparse.ArgumentParser()
    
    options = parser.parse_args()
    
    
    app = TkApp()
    
    app.run()
    
    
    return

if __name__ == '__main__':
    main()
    