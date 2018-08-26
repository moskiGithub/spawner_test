from setuptools import setup, find_packages

setup(
    name='jupyterhub-kubespawner',
    version='0.8.1',
    install_requires=[
        'jupyterhub>=0.8',
        'pyYAML',
        'kubernetes==4.*',
        'escapism',
    ],
    setup_requires=['pytest-runner'],
    tests_require=['pytest'],
    description='JupyterHub Spawner targeting Kubernetes(extend https://github.com/jupyterhub/kubespawner.git)',
    url='https://github.com/moskiGithub/spawner_test.git',
    author='moski',
    author_email='moski_email@163.com',
    license='BSD',
    packages=find_packages(),
)
