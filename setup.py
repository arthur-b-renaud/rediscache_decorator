import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="rediscache_decorator",
    packages=['rediscache_decorator'],
    version="1.0",
    author="Arthur RENAUD",
    license='MIT',
    author_email="arthur@coalition.ai",
    description="Using redis as external rediscache_decorator with one line of code",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/arthur-b-renaud",
    install_requires=['redis>=2.10.6'],
    classifiers=(
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ),
)