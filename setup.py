from setuptools import setup, find_packages

setup(
    name="PolStringConvertor", 
    version="1.0.0", 
    author="Imon Mallik", 
    author_email="imoncoding@gmail.com",
    description="A package to convert infix expressions to postfix/prefix and evaluate them", 
    long_description=open('README.md').read(), 
    long_description_content_type="text/markdown", 
    url="https://github.com/CyberPokemon/PolStringConvertor", 
    packages=find_packages(),  
    classifiers=[
        "Programming Language :: Python :: 3", 
        "License :: OSI Approved :: MIT License", 
        "Operating System :: OS Independent", 
    ],
    python_requires='>=3.6', 
    install_requires=[
        "StrTokenizer==1.1.0", 
    ],
    include_package_data=True, 
)
