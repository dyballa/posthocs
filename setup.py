from setuptools import setup
from os.path import join, dirname

setup(name='posthocs',
      version='0.2.9',
      description='Statistical post-hoc analysis algorithms',
      long_description=open(join(dirname(__file__), 'README.rst')).read(),
      url='http://github.com/maximtrp/posthocs',
      author='Maksim Terpilowski',
      author_email='maximtrp@gmail.com',
      license='GPLv3+',
      packages=['posthocs'],
      keywords='statistics posthoc anova',
      install_requires=['numpy', 'scipy', 'statsmodels',
                        'pandas', 'seaborn', 'matplotlib'],
	  classifiers=[
		'Development Status :: 4 - Beta',

		'Intended Audience :: Education',
		'Intended Audience :: Information Technology',
		'Intended Audience :: Science/Research',

		'Topic :: Scientific/Engineering :: Information Analysis',
		'Topic :: Scientific/Engineering :: Mathematics',

		'License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)',

        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
		'Programming Language :: Python :: 3',
		'Programming Language :: Python :: 3.1',
		'Programming Language :: Python :: 3.2',
		'Programming Language :: Python :: 3.3',
		'Programming Language :: Python :: 3.4',
		'Programming Language :: Python :: 3.5',
		'Programming Language :: Python :: 3.6',
	  ],
      zip_safe=False)
