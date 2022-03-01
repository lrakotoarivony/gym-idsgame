import os
import time
from gym_idsgame.config.runner_mode import RunnerMode
from gym_idsgame.simulation.dao.simulation_config import SimulationConfig
from gym_idsgame.agents.dao.agent_type import AgentType
from gym_idsgame.config.client_config import ClientConfig
from gym_idsgame.runnner import Runner
from gym_idsgame.agents.training_agents.q_learning.q_agent_config import QAgentConfig
from gym_idsgame.experiments.util import plotting_util, util
import argparse



def default_output_dir() -> str:
    """
    :return: the default output dir
    """
    script_dir = os.path.dirname(__file__)
    return script_dir

def define_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('--attacker_path', type=str,default='')
    parser.add_argument('--defender_path', type=str,default='')
    parser.add_argument('--num_episodes', type=int, default = 100)
    parser.add_argument('--attacker_bot', action='store_true')
    parser.add_argument('--defender_bot', action='store_true')

    args = parser.parse_args()
    return args


def default_config(args) -> ClientConfig:
    """
    :return: Default configuration for the experiment
    """
    simulation_config = SimulationConfig(render=True, sleep=0.8, video=False, log_frequency=1,
                                         video_fps=5, video_dir=default_output_dir() + "/videos", num_episodes=args.num_episodes,
                                         gifs=False, gif_dir=default_output_dir() + "/gifs", video_frequency = 1)
    q_agent_config = QAgentConfig(attacker_load_path=args.attacker_path,defender_load_path=args.defender_path)
  
    env_name = "idsgame-cyber-v0"
    attacker_type = AgentType.TABULAR_Q_AGENT.value
    defender_type = AgentType.TABULAR_Q_AGENT.value
    if(args.attacker_bot):
        attacker_type = AgentType.ATTACK_MAXIMAL_VALUE.value
    if(args.defender_bot):
        defender_type = AgentType.DEFEND_MINIMAL_VALUE.value


    client_config = ClientConfig(env_name=env_name, attacker_type=attacker_type,
                                 defender_type=defender_type, mode=RunnerMode.SIMULATE.value,
                                 simulation_config=simulation_config, output_dir=default_output_dir(),
                                 title="Simulation",
                                 q_agent_config=q_agent_config)
    return client_config


# Program entrypoint
if __name__ == '__main__':
    args = define_args()
    config = default_config(args)
    result = Runner.run(config)
    print(f'Number of attack victory in {args.num_episodes} episodes: {result.attacker_wins[-1]}')



