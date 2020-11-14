import gym
import time
import gym_hybrid

env = gym.make('Moving-v0')
env.reset()

done = False
while not done:
    _, _, done, _ = env.step(env.action_space.sample())
    env.render()
    time.sleep(0.1)

time.sleep(1)
env.close()