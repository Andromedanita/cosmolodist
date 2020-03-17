import setuptools

setuptools.setup(
    name="cosmolodist",
    version="0.0.1",
    author="Anita Bahmanyar",
    author_email="bahmanyar@astro.utoronto.ca",
    description="A package to calculate cosmology distances for different cosmologies",
    url='https://github.com/Andromedanita/cosmolodist',
    packages=['cosmolodist'],
    install_requires=['numpy>=1.7','scipy','matplotlib','setuptools']
)
