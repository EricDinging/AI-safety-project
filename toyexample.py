#Gym environment called Taxi-V2
#https://www.learndatasci.com/tutorials/reinforcement-q-learning-scratch-python-openai-gym/

import gym
from IPython.display import clear_output
from time import sleep

env = gym.make("Taxi-v3")

env.reset()
env.render()

print("Action Space {}".format(env.action_space))
print("State Space {}".format(env.observation_space))

# state encoding

state = env.encode(3, 1, 2, 0)
env.s = state
# State: 328
# +---------+
# |R: | : :G|
# | : : : : |
# | : : : : |
# | | : | : |
# |Y| : |B: |
# +---------+
print(env.s)
print(env.P[328])
#This dictionary has the structure {action: [(probability, nextstate, reward, done)]}

#-------------------------------------------
# A Brute Force Method

epochs = 0
penalties, reward = 0, 0

frames = [] # for animation

done = False

while not done:
    action = env.action_space.sample()
    state, reward, done, info = env.step(action)

    if reward == -10:
        penalties += 1
    
    # Put each rendered frame into dict for animation
    frames.append({
        'frame': env.render(mode='ansi'),
        'state': state,
        'action': action,
        'reward': reward
        }
    )

    epochs += 1
    

goodResIdx = 0

def print_frames(frames):
    for i, frame in enumerate(frames):
        clear_output(wait=True)
        print(frame['frame'])
        print(f"Timestep: {i + 1}")
        print(f"State: {frame['state']}")
        print(f"Action: {frame['action']}")
        print(f"Reward: {frame['reward']}")
        if frame['reward'] == 20:
            goodResIdx = i
        sleep(.1)
        
print_frames(frames)

print("Timesteps taken: {}".format(epochs))
print("Penalties incurred: {}".format(penalties))
print(goodResIdx)
if goodResIdx != 0:
    frame = frames[goodResIdx]
    print(frame['frame'])
    print(f"Timestep: {i + 1}")
    print(f"State: {frame['state']}")
    print(f"Action: {frame['action']}")
    print(f"Reward: {frame['reward']}")


# The agent has no memory of which action was best for each state, which is exactly what Reinforcement Learning will do for us