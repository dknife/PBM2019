import time
import gym
env = gym.make('CartPole-v0')
for i_episode in range(10):
    observation = env.reset()
    for t in range(100000):
        time.sleep(0.01)
        env.render()
        print(observation)
        action = env.action_space.sample()
        observation, reward, done, info = env.step(action)
        print(observation, reward, done, info)
        if done:
            print("Episode finished after {} timesteps".format(t+1))
            break
env.close()