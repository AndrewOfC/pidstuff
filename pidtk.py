

from tkinter import *
from simple_pid import PID


class TkApp(object):
    def __init__(self):
        
        master = self._master = Tk()
        
        
        self._pid = PID()
        
        self._runVar = BooleanVar(master, value=False)
        
        return
    
    def _timer(self):
        return
    
    def _onRun(self):
        return 
    
    def run(self):
        
        master = self._master 
       
        
        s = Scale(master, from_=-100, to=100,tickinterval=20, orient=HORIZONTAL)
        
        s.pack(fill='x', expand=1)
        
        ##
        ## Run
        ##
        run_cb = Checkbutton(master, text="run", command=self._onRun, onvalue=True, offvalue=False, variable=self._runVar)
        run_cb.pack()
        
        ##
        ## Kp
        ##
        Label(master, text="Kp").pack()
        kp_entry = Entry(master)
        kp_entry.pack()
        
        ##
        ## Ki
        ##
        Label(master, text="Ki").pack()
        ki_entry = Entry(master)
        ki_entry.pack()    
        
        ##
        ## Kd
        ##
        Label(master, text="Kd").pack()
        kd_entry = Entry(master)
        kd_entry.pack()        
        
        apply = Button(master, text="Apply")
        
        apply.pack()
        
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
    