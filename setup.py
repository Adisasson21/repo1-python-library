import setuptools

setuptools.setup(
  name='sum_prime_numbers',
  packages=['sum_prime_numbers'],
  version='0.1',
  license='MIT',
  description='The function calculate all the prime numbers up to the number you chose',
  author='Adi Sasson',
  author_email='sassonadi38@gmail.com',
  install_requires=[
          'flask',
      ],
  python_requires='>=3.10'
)
