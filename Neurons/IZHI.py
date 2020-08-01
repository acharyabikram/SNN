import math
import numpy as np
import matplotlib.pyplot as plt



class Izhi():
    def __init__(self):
        self.a = .1            
        self.b = .2
        self.c = -65
        self.d = 8

        self.v = -65
        self.u = -14


    def step(self, dt, I, method=0): 

        if method != 1 and method != 0:
            print("Invalid method\n0 - EULER\n1 - RK4\n")

        if self.v >= -30:
            self.v = self.c
            self.u += self.d
        else: 
            if method == 1: 
                self.solve_rk4(dt, I)
            elif method == 0: 
                self.solve_euler(dt, I)

    def solve_euler(self,dt,I): 
        u = self.u 
        v = self.v 
        dv = self.f_v(I,v,dt) 
        du = self.f_u(u,dt) 
        self.v += dv
        self.u += du

    def solve_rk4(self, dt, I):
        dv1 = self.f_v(I, self.v,dt) 
        dv2 = self.f_v(I, self.v + dv1*0.5,dt)
        dv3 = self.f_v(I, self.v + dv2*0.5,dt) 
        dv4 = self.f_v(I, self.v + dv3,dt) 
        dv  = 1/6*(dv1 + dv2*2 + dv3*2 + dv4) 
        

        du1 = self.f_u(self.u,dt) 
        du2 = self.f_u(self.u + du1*0.5,dt)
        du3 = self.f_u(self.u + du2*0.5,dt) 
        du4 = self.f_u(self.u + du3,dt) 
        du  = 1/6*(du1 + du2*2 + du3*2 + du4) 

        self.v += dv 
        self.u += du 
            
    def f_v(self, i, v, dt): 
        return (0.04 * v * v + 5 * v + 140 - self.u + i) *dt

    def f_u(self, u,dt): 
        return self.a * (self.b * self.v - u) *dt

def plot(neuron, time, dt, I, method):

    # build the v and u vector
    steps = math.ceil(time/dt)
    v = np.zeros(steps)

    v[0] = neuron.v
 

    for i in range(steps): 
        neuron.step(dt, I[i], method)
        v[i] = neuron.v 



    vTime = np.arange(0, time, dt, dtype=None)
    plt.plot(vTime, v, color='b', label="potential")
    plt.plot(vTime, I, color='r', label="current")
    plt.title("Single neuron stimulation")
    plt.xlabel("Time [ms]")
    plt.ylabel("Voltage [mv]")
    plt.savefig("Fast spiking")
    plt.show()



neuron = Izhi() 
time = 500
dt = 0.01
steps = math.ceil(time / dt)
I = [0 if 200/dt <= i <= 300/dt  else 10 for i in range(steps)]

plot(neuron, time, dt, I,1 )