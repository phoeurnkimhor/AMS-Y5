from setuptools import setup, find_packages

setup(
    name="preprocessing_package",
    version="0.1.0",
    packages=find_packages(),
    install_requires=["pandas"],
    author="Kimhor Phoeurn",
    author_email="phoeurnkimhor@gmail.com",
    description="A package for data preprocessing",
    python_requires=">=3.8",
)
