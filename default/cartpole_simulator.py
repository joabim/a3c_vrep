import tensorflow as tf
from default.cartpole import CartPole
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.animation as animation

# note: using radians
# state [self.cart_location, self.cart_velocity, self.pole_angle, self.pole_velocity]

# class DataGen(object):
#     def __init__(self):
#         state = []
#     def __iter__(self):
#         return self
#     def __next__(self):
#         return self.next()
#     def next(self):
#         state,_ =

class CartpoleSimulator():
    def __init__(self, cartpole_env):
        self.cartpole_env = cartpole_env
        self.pole_length = cartpole_env.pole_length
        #self.pole_mass = cartpole_env.pole_mass
        self.fig = plt.figure()
        #self.fig.set_dpi(100)
        #self.fig.set_size_inches(8, 8)

        # Environment graphics initialization
        self.ax = plt.axes(xlim=(-4,4), ylim=(-4,4))
        self.cart_position = 0.0
        self.cart_patch = plt.Circle((self.cart_position, 0),0.1, fc='y')
        self.pole_line = plt.Line2D((0,0),(0,0), lw=3)

    def _init(self):
        self.cartpole_env._reset()
        self.pole_line.set_data(self.get_system())
        self.ax.add_patch(self.cart_patch)
        self.ax.add_line(self.pole_line)
        return self.cart_patch, self.pole_line

    def get_system(self):
        state, _ = self.cartpole_env._state()
        xdata, ydata = (state[0], state[0] + self.pole_length * np.sin(state[2])), \
                       (0, self.pole_length * np.cos(state[2]))
        print('x=%f' % (state[2]*(180/np.pi)))
        return xdata, ydata

    def _animate(self, action):
        # Random placeholder actions
        self.cartpole_env.takeAction(action)
        xd, yd = self.get_system()
        self.cart_patch.center = (xd[0], 0)
        #print('angle:', state[2]*(180/np.pi))
        self.pole_line.set_data(xd, yd)
        return self.cart_patch, self.pole_line

    # Data gen is supposed to fetch current state vars after cartpole env's state vars has been updated by takeAction
    def _data_gen(self):
        while True:
            yield 2

    def run(self):
        anim = animation.FuncAnimation(self.fig, self._animate, self._data_gen, init_func=self._init,
                                       interval=20, blit=True, repeat=False)
        plt.show()

cpr = CartPole()
dod = CartpoleSimulator(cpr)

dod.run()