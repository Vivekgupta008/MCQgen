from setuptools import find_packages,setup

setup(
    name='mcqgenerator',
    version='0.0.1',
    author='Vivek gupta',
    author_email='guptavivek216arav@gmail.com',
    description='A simple MCQ generator',
    url='https://github.com/vivekgupta/mcqgenerator',
    packages=find_packages(),
    install_requires=["openai","langchain","python-dotenv","streamlit","PyPDF2"]
)