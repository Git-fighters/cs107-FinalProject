import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="gitfighters",
    version="1.0.6",
    author="cs107-project-group10",
    author_email="hugo_montenegro@g.harvard.edu, talelokvenec@g.harvard.edu, mananahakobyan@g.harvard.edu, Feige@g.harvard.edu",
    description="Automatic Differentiation Library",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Git-fighters/cs107-FinalProject",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    scripts=['cli.py'],    
    install_requires=['matplotlib', 'nltk', 'numpy'], #external packages as dependencies
)
