from setuptools import setup, find_namespace_packages

setup(
    name='clean_folder',
      version='0.1.1',
      description='Sorting files into folders',
      url='https://github.com/yufira/first_project',
      author='Yulia Fironova',
      author_email='fironovayu@gmail.com',
      license='MIT',
      packages=find_namespace_packages(),
      install_requires=[],
      long_description="Sorting files in folders",
      long_description_content_type="text/x-rst",
      entry_points={
          'console_scripts': ['clean-folder=clean_folder.clean:main']
          },
      )