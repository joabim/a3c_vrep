from default.cartpole_simulator import CartpoleSimulator
from default.cartpole import CartPole
import numpy as np
import tensorflow as tf

#from a3c import CHECKPOINT_DIR

# sess = tf.Session()
# init = tf.initialize_all_variables()
# saver = tf.train.Saver(init)
# checkpoint = tf.train.get_checkpoint_state(CHECKPOINT_DIR)
# if checkpoint and checkpoint.model_checkpoint_path:
#     saver.restore(sess, checkpoint.model_checkpoint_path)
#     print("Successfully loaded:", checkpoint.model_checkpoint_path)
# else:
#     print("Unable to load previous checkpoint")

cpl_env = CartPole()
sim = CartpoleSimulator(cpl_env)

# # TODO: construct model interface functions
# while True:
#     taken_action = sess.run() # kinda like this
#     sim.run(taken_action)

for i in range(10):
    rnd = np.random.random_integers(0, 1)
    cpl_env.takeAction(rnd)
    s, _ = cpl_env._state()
    print('vel= %f, rnd= %d'% (s[1], rnd))
    #sim.run()