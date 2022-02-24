import os
import time
import sys
from gym_idsgame.config.runner_mode import RunnerMode
from gym_idsgame.agents.training_agents.q_learning.q_agent_config import QAgentConfig
from gym_idsgame.agents.dao.agent_type import AgentType
from gym_idsgame.config.client_config import ClientConfig
from gym_idsgame.runnner import Runner
from gym_idsgame.experiments.util import util


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
    q_agent_config = QAgentConfig(gamma=0.999, alpha=0.05, epsilon=1, render=False, eval_sleep=0.9,
                                  min_epsilon=0.01, eval_episodes=5, train_log_frequency=10,
                                  epsilon_decay=0.9999, video=False, eval_log_frequency=10,
                                  video_fps=5, video_dir=default_output_dir() + "/videos", num_episodes=20001,
                                  eval_render=False, gifs=False, gif_dir=default_output_dir() + "/gifs",
                                  eval_frequency=5000, attacker=True, defender=True,
                                  video_frequency=1000,checkpoint_freq= 500,
                                  save_dir=default_output_dir() + "/data")
    env_name = "idsgame-cyber-v0"
    client_config = ClientConfig(env_name=env_name, attacker_type=AgentType.TABULAR_Q_AGENT.value,
                                 defender_type=AgentType.TABULAR_Q_AGENT.value,
                                 mode=RunnerMode.TRAIN_DEFENDER_AND_ATTACKER.value,
                                 q_agent_config=q_agent_config, output_dir=default_output_dir(),
                                 title="TrainingQAgent vs TrainingQAgent")
    return client_config



# Program entrypoint
if __name__ == '__main__':
    config = default_config()
    time_str = str(time.time())
    util.create_artefact_dirs(config.output_dir,0)
    train_result, eval_result = Runner.run(config)



