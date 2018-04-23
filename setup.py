from setuptools import setup, find_packages

setup(
    name='jupyterhub-kubespawner',
    version='0.8.1',
    install_requires=[
        'jupyterhub>=0.8',
        'pyYAML',
        'kubernetes==4.*',
        'escapism',
        'ldap3'
    ],
    setup_requires=['pytest-runner'],
    tests_require=['pytest'],
    description='JupyterHub Spawner targeting Kubernetes',
    url='https://github.com/moskiGithub/spawner_test.git',
    author='Yuvi Panda',
    author_email='yuvipanda@gmail.com',
    license='BSD',
    packages=find_packages(),
)
