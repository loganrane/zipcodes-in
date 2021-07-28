from setuptools import setup, find_packages

with open("README.md", "r", encoding='utf-8') as f:
    readme = f.read()

with open("VERSION.txt", "r") as f:
    version_num = f.read()

setup (
    name="zipcodes-in",
    version = version_num.strip(),
    author="Arpit",
    author_email="arpitfalcon1@gmail.com",
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
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
    entry_points = {
    'console_scripts': [
        'zipcode = zipcode_in.__main__:main'
    ],
    
    })