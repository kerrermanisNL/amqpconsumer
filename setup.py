from setuptools import setup


setup(
    name='amqpconsumer',
    version='1.0',
    description='AMQP event listener',
    long_description='Python module to facilitate listening for and acting on AMQP events.',
    url='https://github.com/ByteInternet/amqpconsumer',
    author='Byte B.V.',
    author_email='tech@byte.nl',
    license='3-clause BSD',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'License :: OSI Approved :: BSD License',
        'Intended Audience :: Developers',
        'Topic :: Utilities',
        'Topic :: Communications',
        'Topic :: Internet',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
    ],
    keywords='amqp events consumer listener rabbitmq',
    packages=['amqpconsumer'],
    install_requires=['pika>=0.9.8']
)
