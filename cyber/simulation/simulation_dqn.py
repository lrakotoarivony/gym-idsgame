import os
import time
from gym_idsgame.config.runner_mode import RunnerMode
from gym_idsgame.simulation.dao.simulation_config import SimulationConfig
from gym_idsgame.agents.dao.agent_type import AgentType
from gym_idsgame.config.client_config import ClientConfig
from gym_idsgame.runnner import Runner
from gym_idsgame.agents.training_agents.q_learning.q_agent_config import QAgentConfig
from gym_idsgame.experiments.util import plotting_util, util
import gym
from gym_idsgame.agents.training_agents.q_learning.dqn.dqn import DQNAgent
from gym_idsgame.agents.training_agents.q_learning.dqn.dqn_config import DQNConfig
import torch




def default_output_dir() -> str:
    """
    :return: the default output dir
    """
    script_dir = os.path.dirname(__file__)
    return script_dir


def default_config() -> ClientConfig:
    """
    :return: Default configuration for the experiment
    """
    simulation_config = SimulationConfig(render=True, sleep=0.8, video=True, log_frequency=1,
                                         video_fps=5, video_dir=default_output_dir() + "/videos", num_episodes=2,
                                         gifs=True, gif_dir=default_output_dir() + "/gifs", video_frequency = 1)

    dqn_config = DQNConfig(input_dim=40, attacker_output_dim=32, defender_output_dim=40, hidden_dim=16,
                           replay_memory_size=10000,
                           num_hidden_layers=1,
                           replay_start_size=1000, batch_size=32, target_network_update_freq=1000,
                           gpu=False, tensorboard=False, tensorboard_dir=default_output_dir() + "/results/tensorboard",
                           loss_fn="Huber", optimizer="Adam", lr_exp_decay=True, lr_decay_rate=0.9999)

    q_agent_config = QAgentConfig(gamma=0.999, alpha=0.00001, epsilon=1, render=False, eval_sleep=0.9,
                                  min_epsilon=0.01, eval_episodes=2, train_log_frequency=100,
                                  epsilon_decay=0.9999, video=True, eval_log_frequency=1,
                                  video_fps=5, video_dir=default_output_dir() + "/results/videos", num_episodes=20001,
                                  eval_render=False, gifs=True, gif_dir=default_output_dir() + "/results/gifs",
                                  eval_frequency=1000, attacker=True, defender=True, video_frequency=101,
                                  save_dir=default_output_dir() + "/results/data", dqn_config=dqn_config,
                                  checkpoint_freq=5000)
    env_name = "idsgame-cyber-v0"
    #q_agent_config = QAgentConfig(attacker_load_path="/home/kali/Documents/projet_3A/gym-idsgame/cyber/simulation/results/data/1643884050.5795374_attacker_q_network.pt",defender_load_path="/home/kali/Documents/projet_3A/gym-idsgame/cyber/simulation/results/data/1643884050.5795374_defender_q_network.pt")
    client_config = ClientConfig(env_name=env_name, attacker_type=AgentType.DQN_AGENT.value,
                                 defender_type=AgentType.DQN_AGENT.value, mode=RunnerMode.SIMULATE.value,
                                 simulation_config=simulation_config, output_dir=default_output_dir(),
                                 title="TabularQAgentAttacker vs TabularQAgentDefender",
                                 q_agent_config=q_agent_config)
                                 #initial_state_path = default_output_dir() + "/initial_state/initial_state.pkl")
    return client_config


# Program entrypoint
if __name__ == '__main__':
    
    config = default_config()
    time_str = str(time.time())
    util.create_artefact_dirs(config.output_dir,1)
    logger = util.setup_logger("idsgame-v0-dqn_vs_dqn", config.output_dir + "/results/logs/",
                               time_str=time_str)
    config.logger = logger
    config.simulation_config.logger = logger
    config.simulation_config.to_csv(config.output_dir + "/results/hyperparameters/" + time_str + ".csv")

    env = gym.make(config.env_name, idsgame_config = config.idsgame_config,
                       save_dir=config.output_dir + "/results/data/" + str(config.random_seed),
                       initial_state_path = config.initial_state_path)
    agent = DQNAgent(env, config.q_agent_config)

    agent.attacker_q_network.load_state_dict(torch.load("/home/kali/Documents/projet_3A/gym-idsgame/cyber/simulation/results/data/1643884050.5795374_attacker_q_network.pt"))
    agent.attacker_q_network.eval()

    agent.defender_q_network.load_state_dict(torch.load("/home/kali/Documents/projet_3A/gym-idsgame/cyber/simulation/results/data/1643884050.5795374_defender_q_network.pt"))
    agent.defender_q_network.eval()


    agent.eval(0,log=False)



