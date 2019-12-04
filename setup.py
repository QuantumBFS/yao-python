from setuptools import setup

def readme():
    with open('README.md') as f:
        return f.read()

setup(name='yao-framework',
      version='0.6.0',
      description='Extensible Efficient Quantum Algorithm Design in Python',
      long_description=readme(),
      long_description_content_type="text/markdown",
      classifiers=[
        'Development Status :: 4 - Beta',
        # https://pypi.org/pypi?%3Aaction=list_classifiers
        'Intended Audience :: Developers',
        'Intended Audience :: Education',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: Apache Software License',
        'Programming Language :: Python :: 3.6',
        'Topic :: Scientific/Engineering',
        'Topic :: Scientific/Engineering :: Artificial Intelligence',
        'Topic :: Scientific/Engineering :: Physics'
      ],
      url='https://github.com/QuantumBFS/Yao.jl',
      keywords='differential equations stochastic ordinary delay differential-algebraic dae ode sde dde',
      author='Xiuzhe (Roger) Luo and Jinguo Liu',
      author_email='roger.luo@uwaterloo.ca',
      license='Apache License 2.0',
      packages=['yao_framework'],
      install_requires=['julia>=0.2'],
      include_package_data=True,
      zip_safe=False)
