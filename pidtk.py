

from tkinter import *
from tkinter.font import Font
from simple_pid import PID


class TkApp(object):
    def __init__(self, period=1000, kp=1.0, ki=0.0, kd=0.0, init=0.0):
        
        
        master = self._master = Tk()
        master.geometry("1600x800")
        
        master.option_add("*Font", "Helvetica 36")
        
        
        self._period = period
        
        
        pid = self._pid = PID(kp, ki, kd, setpoint=0.0, sample_time=period/1000)
       
        self._runVar = BooleanVar(master, value=False)
        
        self._kpVar = StringVar(master, f"{pid.Kp}")
        self._kiVar = StringVar(master, f"{pid.Ki}")
        self._kdVar = StringVar(master, f"{pid.Kd}")
        
        self._plantVar = DoubleVar(master, init)
        
        
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
        self._kd_entry = Entry(master, textvariable=self._kdVar)
        self._kd_entry.pack()        
        
        apply = Button(master, text="Apply", command=self._onApply)
        
        apply.pack()
        
        
        return
    
    def _timer(self):
        return
    
    def _onRun(self):
        
        if self._runVar.get():
            self._onApply()
            self._master.after(self._period, self._update)
        
        return
    
    def _update(self):
        
        val = self._plantVar.get()
        
        nval = self._pid(val)
        
        
        self._plantVar.set(val + nval)
        print(f"update val={val:0.3f} nval={nval:0.3f}")
        
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
        
        
        mainloop()
        
        
        return


def main():
    import argparse
    
    parser = argparse.ArgumentParser()
    
    parser.add_argument("--kp", type=float, default=1.0)
    parser.add_argument("--ki", type=float, default=0.0)
    parser.add_argument("--kd", type=float, default=0.0)
    parser.add_argument("--init", type=float, default=0.0)
    parser.add_argument("--period", type=int, default=1000)
    
    options = parser.parse_args()
    
    
    app = TkApp(kp=options.kp, ki=options.ki, kd=options.kd, init=options.init, period=options.period)
    
    app.run()
    
    
    return

if __name__ == '__main__':
    main()
    