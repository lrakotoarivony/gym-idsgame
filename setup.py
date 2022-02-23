from setuptools import setup, find_packages

setup(name='gym_idsgame',
      version='1.0.12',
      install_requires=['gym', 'pyglet', 'numpy', 'torch', 'matplotlib', 'seaborn', 'tqdm', 'opencv-python',
                        'imageio', 'jsonpickle', 'tensorboard', 'sklearn', 'stable_baselines3', 'torchvision','stepic','pyexiftool','piexif'],
      author='Lucas Rakotoarivony',
      description='An Abstract Cyber Security Simulation and Markov Game for OpenAI Gym',
      keywords='Cyber Security, Intrusion Detection, Markov Games, Reinforcement Learning, Q-learning',
      url='https://github.com/lrakotoarivony/gym-idsgame',
      packages=find_packages(),
      include_package_data=True,
      classifiers=[
          'Development Status :: 3 - Alpha',
          'Intended Audience :: Developers',
          'Topic :: Software Development :: Build Tools',
          'Programming Language :: Python :: 3.5',
          'Programming Language :: Python :: 3.6'
  ]
)
