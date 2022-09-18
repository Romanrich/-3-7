from setuptools import setup, find_packages

from clean_folder.clean_folder.clean import get_main_path, around_dir 
setup(
    name="clean_folder",
    version=‘1’,
    description=‘Very useful code’,
    author=‘Gagauz Roman’,
    author_email=‘flyingcircus@example.com’,
    license=‘MIT’,
    packages=find_namespace_packages(),
    entry_points={‘console_scripts’: [‘clean-folder = clean_folder.clean:main’]})


