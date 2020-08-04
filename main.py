import torch
import torch.nn as nn
import torch.nn.functional as F
import gym
import universe


env = gym.make('gym-core.Pong-v0')
env.configure(remotes="vnc://localhost:5900+15900")
observation_n = env.reset()


while True:
    action_n = [[('KeyEvent', 'ArrowUp', True)] for _ in observation_n]
    observation_n, reward_n, done_n, info = env.step(action_n)
    env.render()



