# gym-parametrized

Repository containing collection of environment for reinforcement learning task possessing parametrized action space.

## "Moving-v0" 
<img align="right" src="moving-v0.jpg"> "Moving-v0" is a sandbox environment for parametrized agent. It consist in a 2x2 field, with circle target of 0.1 radius. 
The goal is to stop the player inside the target. There is three discrete action: turn, accelerate, and break; as well as 
2 possible parameters: acceleration and rotation. The state is constitued of a list of 10 elements, including the speed, the 
position, the direction, the position of the target, etc.


Snippet of code to run the environment:
```
import gym
import gym_parametrized

env = gym.make('Moving-v0')
env.reset()

done = False
while not done:
    state, reward, done, info = env.step(env.action_space.sample())
    print(f'State: {state} Reward: {reward} Done: {done}')
```

Disclaimer:  
Even though the mechanics of the environment are done, maybe the hyperparameter will need some further adjustmenents.

This environment is described in several paper such as:  
[[Parametrized Deep Q-Networks Learning]](https://arxiv.org/pdf/1810.06394.pdf)  
[[Hybrid Actor-Critic Reinforcement Learning in Parameterized Action Space]](https://arxiv.org/pdf/1903.01344.pdf)




