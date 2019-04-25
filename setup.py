from setuptools import setup, find_packages

setup(
      name='obpfaker',
      version='0.0.1',
      packages=find_packages(),
      install_requires=[
            'Click',
      ],
      entry_points='''
        [console_scripts]
        obpfaker=run_script:cli
      ''',
      )
