from setuptools import setup, find_packages

setup(name='dnurt_compose_html',
      version='1.0.0',
      description='DNURT app for html composing for ojs',
      install_requires=[],
      author='Andrey Nechaev',
      author_email='andrewnech@gmail.com',
      license='DNURT',
      packages=find_packages(),

      entry_points={
          'console_scripts':
              ['html_compose = src.repimg:compose']
      },

      )
