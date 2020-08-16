from setuptools import setup

setup(
   name='turkishsd',
   version='0.1',
   description='A Turkish stemmer and deasciifier',
   license="MIT",
   author='Cenk Anıl Bahçevan',
   author_email='cenk.bahcevan@turknet.net.tr',
   packages=['turkishsd'],  
   install_requires=['sklearn','loguru'], 
   test_suite="tests",
   keywords='turkish nlp tokenizer stemmer deasciifier',
   include_package_data=True,
   package_data={
       '': ['data/*'],
    }

)
