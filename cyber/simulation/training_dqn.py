import os
import time
import sys
import glob
from gym_idsgame.config.runner_mode import RunnerMode
from gym_idsgame.agents.training_agents.q_learning.q_agent_config import QAgentConfig
from gym_idsgame.agents.dao.agent_type import AgentType
from gym_idsgame.config.client_config import ClientConfig
from gym_idsgame.runnner import Runner
from gym_idsgame.experiments.util import plotting_util, util
from gym_idsgame.agents.training_agents.q_learning.dqn.dqn_config import DQNConfig


def get_script_path():
    """
    :return: the script path
    """
    return os.path.dirname(os.path.realpath(sys.argv[0]))


def default_output_dir() -> str:
    """
    :return: the default output dir
    """
    script_dir = get_script_path()
    return script_dir


def default_config() -> ClientConfig:
    """
    :return: Default configuration for the experiment
    """
    '''dqn_config = DQNConfig(input_dim=242, attacker_output_dim=220, defender_output_dim=242, hidden_dim=64,
                           replay_memory_size=10000,
                           num_hidden_layers=1,
                           replay_start_size=1000, batch_size=32, target_network_update_freq=1000,
                           gpu=False, tensorboard=False, tensorboard_dir=default_output_dir() + "/results/tensorboard",
                           loss_fn="Huber", optimizer="Adam", lr_exp_decay=True, lr_decay_rate=0.9999)'''
    dqn_config = DQNConfig(input_dim=40, attacker_output_dim=32, defender_output_dim=40, hidden_dim=16,
                           replay_memory_size=10000,
                           num_hidden_layers=1,
                           replay_start_size=1000, batch_size=32, target_network_update_freq=1000,
                           gpu=False, tensorboard=False, tensorboard_dir=default_output_dir() + "/results/tensorboard",
                           loss_fn="Huber", optimizer="Adam", lr_exp_decay=True, lr_decay_rate=0.9999)
    q_agent_config = QAgentConfig(gamma=0.999, alpha=0.00001, epsilon=1, render=False, eval_sleep=0.9,
                                  min_epsilon=0.01, eval_episodes=100, train_log_frequency=100,
                                  epsilon_decay=0.9999, video=True, eval_log_frequency=1,
                                  video_fps=5, video_dir=default_output_dir() + "/results/videos", num_episodes=20001,
                                  eval_render=False, gifs=True, gif_dir=default_output_dir() + "/results/gifs",
                                  eval_frequency=1000, attacker=True, defender=True, video_frequency=101,
                                  save_dir=default_output_dir() + "/results/data", dqn_config=dqn_config,
                                  checkpoint_freq=5000)
    env_name = "idsgame-cyber-v0"
    #env_name = "idsgame-v5"

    client_config = ClientConfig(env_name=env_name, attacker_type=AgentType.DQN_AGENT.value,
                                 defender_type=AgentType.DQN_AGENT.value,
                                 mode=RunnerMode.TRAIN_DEFENDER_AND_ATTACKER.value,
                                 q_agent_config=q_agent_config, output_dir=default_output_dir(),
                                 title="TrainingDQNAgent vs TrainingDQNAgent")
    return client_config


# Program entrypoint
if __name__ == '__main__':
    config = default_config()
    time_str = str(time.time())
    util.create_artefact_dirs(config.output_dir,3)
    logger = util.setup_logger("cyber_vs_cyber-dqn-v0", config.output_dir + "/results/logs/",time_str=time_str)
    config.logger = logger
    config.q_agent_config.logger = logger
    config.q_agent_config.to_csv(config.output_dir + "/results/hyperparameters/" + time_str + ".csv")
    train_result, eval_result = Runner.run(config)



