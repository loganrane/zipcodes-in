from setuptools import setup, find_packages

with open("README.md") as f:
    readme = f.read()

with open("VERSION.txt") as f:
    version_num = f.read()

setup (
    name="zipcodes-in",
    version = version_num.strip(),
    description = "Indian Zip Codes",
    long_description = readme,
    long_description_content_type = "text/markdown",

    # Homepage
    url="https://github.com/arpitfalcon/zipcodes-in",

    # Include all package except make_data and tests
    packages=find_packages(exclude=("make_data", "tests", "make_graph")),
    install_requires=[],
    keywords="zipcode zip code india in state validate filter find query",
    include_package_data=True,
    entry_points = {
    'console_scripts': [
        'zipcode = zipcode_script.__main__:main'
    ],
    
    })