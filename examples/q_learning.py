import gym
from gym_idsgame.envs.idsgame_env import IdsGameEnv
from gym_idsgame.agents.random_defense_agent import RandomDefenseAgent
from gym_idsgame.envs.dao.game_config import GameConfig
from gym_idsgame.envs.dao.idsgame_config import IdsGameConfig
from gym_idsgame.envs.dao.render_config import RenderConfig
from gym_idsgame.algorithms.q_learning import QAgent

# Program entrypoint
if __name__ == '__main__':
    pass
    #env = gym.make("gym_yagw:yagw-v1", width=5, height=5)
    game_config = GameConfig(num_layers=2, num_servers_per_layer=3, num_attack_types=10, max_value=9)
    defender_policy = RandomDefenseAgent(game_config)
    render_config = RenderConfig(num_blinks=6, blink_interval=0.1)
    idsgame_config = IdsGameConfig(game_config=game_config, defender_agent=defender_policy,
                                   render_config=render_config)
    env = IdsGameEnv(idsgame_config=idsgame_config)
    q_agent = QAgent(env, gamma=0.99, alpha=0.3, epsilon=1, render=False, eval_sleep=0.5,
                     min_epsilon=0.1, eval_epochs=10, log_frequency=100, epsilon_decay=0.9999, video=False,
                     video_fps=5, video_dir="./videos")
    #episode_rewards, episode_steps, epsilon_values = q_agent.run(15000)
    episode_rewards, episode_steps, epsilon_values = q_agent.run(5000)
    q_agent.eval()
    #plot_results(episode_rewards, episode_steps)