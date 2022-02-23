import os
import time
from gym_idsgame.config.runner_mode import RunnerMode
from gym_idsgame.simulation.dao.simulation_config import SimulationConfig
from gym_idsgame.agents.dao.agent_type import AgentType
from gym_idsgame.config.client_config import ClientConfig
from gym_idsgame.runnner import Runner
from gym_idsgame.agents.training_agents.q_learning.q_agent_config import QAgentConfig
from gym_idsgame.experiments.util import plotting_util, util



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
    simulation_config = SimulationConfig(render=True, sleep=0.8, video=False, log_frequency=1,
                                         video_fps=5, video_dir=default_output_dir() + "/videos", num_episodes=10,
                                         gifs=False, gif_dir=default_output_dir() + "/gifs", video_frequency = 1)
    q_agent_config = QAgentConfig(attacker_load_path="/home/kali/Documents/projet_3A/gym-idsgame/cyber/simulation/data/1645446154.1411295_attacker_q_table.npy",defender_load_path="/home/kali/Documents/projet_3A/gym-idsgame/cyber/simulation/data/1645446154.1411295_defender_q_table.npy")
    env_name = "idsgame-cyber-v0"
    #AgentType.RANDOM.value
    #AgentType.DEFEND_MINIMAL_VALUE.value
    '''client_config = ClientConfig(env_name=env_name, attacker_type=AgentType.TABULAR_Q_AGENT.value,
                                 defender_type=AgentType.TABULAR_Q_AGENT.value, mode=RunnerMode.SIMULATE.value,
                                 simulation_config=simulation_config, output_dir=default_output_dir(),
                                 title="TabularQAgentAttacker vs TabularQAgentDefender",
                                 q_agent_config=q_agent_config)'''
    client_config = ClientConfig(env_name=env_name, attacker_type=AgentType.ATTACK_MAXIMAL_VALUE.value,
                                 defender_type=AgentType.DEFEND_MINIMAL_VALUE.value, mode=RunnerMode.SIMULATE.value,
                                 simulation_config=simulation_config, output_dir=default_output_dir(),
                                 title="TabularQAgentAttacker vs TabularQAgentDefender",
                                 q_agent_config=q_agent_config)
    return client_config


# Program entrypoint
if __name__ == '__main__':
    config = default_config()
    time_str = str(time.time())
    util.create_artefact_dirs(config.output_dir,1)
    logger = util.setup_logger("idsgame-v0-tabular_q_agent_vs_tabular_q_agent", config.output_dir + "/results/logs/",
                               time_str=time_str)
    config.logger = logger
    config.simulation_config.logger = logger
    config.simulation_config.to_csv(config.output_dir + "/results/hyperparameters/" + time_str + ".csv")
    result = Runner.run(config)
    print(result.attacker_wins)
    print(f'Number of attack victory in 10 episodes: {result.attacker_wins[-1]}')



