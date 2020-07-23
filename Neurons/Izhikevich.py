from Neuron import Neuron as Neuron_

import math
import numpy as np
import matplotlib.pyplot as plt


class Izhi(Neuron_):
    def __init__(self):
        # setting parameters with the default value
        super().__init__()
        self.a = .1  # fast spiking
        self.b = .2
        self.c = -65
        self.d = 8

        self.V = -65
        self.U = -14

    def create_copy(self):
        n = Izhi()
        n.set_constants(self.a, self.b, self.c, self.d)
        return n

    def stimulation(self, tmax, I, dt):
        steps = math.ceil(tmax / dt)

        # input
        v = np.zeros(steps, dtype=float)
        u = np.zeros(steps, dtype=float)
        v[0] = self.V  # resting potential
        u[0] = self.U

        for t in range(steps - 1):
            self.nextIteration(dt, I[t])
            v[t + 1] = self.V
            u[t + 1] = self.U
        return v

    def nextIteration(self, dt, I):
        for i in range(math.ceil(1 / dt)):
            if self.V >= 30:
                self.V = self.c
                self.U = self.U + self.d
            else:
                dv = (0.04 * self.V * self.V + 5 * self.V + 140 - self.U + I) * dt
                du = (self.a * (self.b * self.V - self.U)) * dt
                self.V += dv
                self.U += du

    def set_constants(self, a=None, b=None, c=None, d=None):
        if a: self.a = a
        if b: self.b = b
        if c: self.c = c
        if d: self.d = d



def plot(time, dt, v, I):
    vTime = np.arange(0, time, dt, dtype=None)
    plt.plot(vTime, v, color='b', label="potential")
    plt.plot(vTime, I, color='r', label="current")
    plt.title("Single neuron stimulation")
    plt.xlabel("Time [ms]")
    plt.ylabel("Voltage [mv]")
    plt.savefig("Fast spiking")
    plt.show()


if __name__ == '__main__':
    n = Izhi()
    n1 = n.create_copy()

    """
    time = 500
    dt = 0.5
    steps = math.ceil(time / dt)
    # I = [0 if 200 / dt <= i <= 300 / dt else 10 for i in range(steps)]
    I = 10*np.ones(math.ceil(time / dt))
    v = n.stimulation(time, I, dt)
    plot(time, dt, v, I)
    """
