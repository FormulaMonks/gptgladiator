from setuptools import setup, find_packages

setup(
    name='gptgladiator',
    version='0.1.4',
    packages=find_packages(),
    install_requires=[
        'openai==0.27.6',
        'tiktoken==0.3.3',
        'streamlit==1.22.0'
    ],
    py_modules=['gptgladiator'],
    author='Will Jessup',
    author_email='Will@theoremone.co',
    description='Generate multiple draft responses and then use a second model to judge the answers and pick a winner, which is then returned to the user.',
    url='https://github.com/TheoremOne/gladiator/',
)
