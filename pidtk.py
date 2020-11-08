

from tkinter import *
from simple_pid import PID


class TkApp(object):
    def __init__(self, period=1000):
        
        master = self._master = Tk()
        
        self._period = period 
        
        pid = self._pid = PID(setpoint=0.0)
        
        self._Kp = self._pid.Kp
        self._Ki = self._pid.Ki
        self._Kd = self._pid.Kd
        
        self._runVar = BooleanVar(master, value=False)
        
        self._kpVar = StringVar(master, f"{pid.Kp}")
        self._kiVar = StringVar(master, f"{pid.Ki}")
        self._kdVar = StringVar(master, f"{pid.Kd}")
        
        self._plantVar = IntVar(master, 0)
        
        return
    
    def _timer(self):
        return
    
    def _onRun(self):
        
        if self._runVar.get():
            self._master.after(self._period, self._update)
        
        return
    
    def _update(self):
        
        val = self._plantVar.get()
        
        nval = self._pid(val)
        
        print(f"update val={val} nval={nval}")
        
        self._plantVar.set(nval)
        
        if self._runVar.get():
            self._master.after(self._period, self._update)
                
        return
    
    def _onApply(self):
        
        pid = self._pid
        
        kp = float(self._kp_entry.get())
        ki = float(self._ki_entry.get())
        kd = float(self._kd_entry.get())
        
        pid.Kp, pid.Ki, pid.Kd = kp, ki, kd 
                
        
        return 
    
    def run(self):
        
        master = self._master 
        pid    = self._pid
        
        self._plant = Scale(master, variable=self._plantVar, from_=-100, to=100,tickinterval=20, orient=HORIZONTAL)
        
        self._plant.pack(fill='x', expand=1)
        
        ##
        ## Run
        ##
        run_cb = Checkbutton(master, text="run", command=self._onRun, onvalue=True, offvalue=False, variable=self._runVar)
        run_cb.pack()
        
        ##
        ## Kp
        ##
        Label(master, text="Kp").pack()
        self._kp_entry = Entry(master, textvariable=self._kpVar)
        self._kp_entry.pack()
        
        ##
        ## Ki
        ##
        Label(master, text="Ki").pack()
        self._ki_entry = Entry(master, textvariable=self._kiVar)
        self._ki_entry.pack()    
        
        ##
        ## Kd
        ##
        Label(master, text="Kd").pack()
        self._kd_entry = Entry(master, textvariable=self._kiVar)
        self._kd_entry.pack()        
        
        apply = Button(master, text="Apply", command=self._onApply)
        
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
    