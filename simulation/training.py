import argparse
from email.policy import default
import os
import sys
from gym_idsgame.config.runner_mode import RunnerMode
from gym_idsgame.agents.training_agents.q_learning.q_agent_config import QAgentConfig
from gym_idsgame.agents.training_agents.q_learning.dqn.dqn_config import DQNConfig
from gym_idsgame.agents.dao.agent_type import AgentType
from gym_idsgame.config.client_config import ClientConfig
from gym_idsgame.runnner import Runner
from gym_idsgame.experiments.util import util
import time

def define_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('--dqn', action='store_true')
    parser.add_argument('--num_episodes', type=int, default = 20001)
    parser.add_argument('--checkpoint_freq', type=int, default = 500)

    args = parser.parse_args()
    return args


def default_output_dir() -> str:
    """
    :return: the default output dir
    """
    return os.path.dirname(os.path.realpath(sys.argv[0]))


def default_config(args) -> ClientConfig:
    """
    :return: Default configuration for the experiment
    """
    output_dir = default_output_dir()
    env_name = "idsgame-cyber-v0"
    if(args.dqn):
        dqn_config = DQNConfig(input_dim=40, attacker_output_dim=32, defender_output_dim=40, hidden_dim=16,
                           replay_memory_size=10000,
                           num_hidden_layers=1,
                           replay_start_size=1000, batch_size=32, target_network_update_freq=1000,
                           gpu=False, tensorboard=False, tensorboard_dir=output_dir + "/results/tensorboard",
                           loss_fn="Huber", optimizer="Adam", lr_exp_decay=True, lr_decay_rate=0.9999)
        q_agent_config = QAgentConfig(gamma=0.999, alpha=0.00001, epsilon=1, render=False, eval_sleep=0.9,
                                    min_epsilon=0.01, eval_episodes=100, train_log_frequency=100,
                                    epsilon_decay=0.9999, video=False, eval_log_frequency=1,
                                    video_fps=5, video_dir=output_dir + "/results/videos", num_episodes=args.num_episodes,
                                    eval_render=False, gifs=False, gif_dir=output_dir + "/results/gifs",
                                    eval_frequency=1000, attacker=True, defender=True, video_frequency=101,
                                    save_dir=output_dir + "/results/data", dqn_config=dqn_config,
                                    checkpoint_freq=args.checkpoint_freq)
        client_config = ClientConfig(env_name=env_name, attacker_type=AgentType.DQN_AGENT.value,
                                    defender_type=AgentType.DQN_AGENT.value,
                                    mode=RunnerMode.TRAIN_DEFENDER_AND_ATTACKER.value,
                                    q_agent_config=q_agent_config, output_dir=output_dir,
                                    title="TrainingDQNAgent vs TrainingDQNAgent")
    else:
        q_agent_config = QAgentConfig(gamma=0.999, alpha=0.05, epsilon=1, render=False, eval_sleep=0.9,
                                    min_epsilon=0.01, eval_episodes=5, train_log_frequency=10,
                                    epsilon_decay=0.9999, video=False, eval_log_frequency=10,
                                    video_fps=5, video_dir=output_dir + "/videos", num_episodes=args.num_episodes,
                                    eval_render=False, gifs=False, gif_dir=output_dir + "/gifs",
                                    eval_frequency=5000, attacker=True, defender=True,
                                    video_frequency=1000,checkpoint_freq= args.checkpoint_freq,
                                    save_dir=output_dir + "/data")
        client_config = ClientConfig(env_name=env_name, attacker_type=AgentType.TABULAR_Q_AGENT.value,
                                    defender_type=AgentType.TABULAR_Q_AGENT.value,
                                    mode=RunnerMode.TRAIN_DEFENDER_AND_ATTACKER.value,
                                    q_agent_config=q_agent_config, output_dir=output_dir,
                                    title="TrainingQAgent vs TrainingQAgent")

    return client_config

if __name__ == '__main__':
    args = define_args()
    config = default_config(args)
    time_str = str(time.time())
    util.create_artefact_dirs(config.output_dir,0)
    train_result, eval_result = Runner.run(config)