from setuptools import setup, find_packages

setup(
    name="data-consumer-pipeline",
    version="0.1.0",
    description="Data consumer pipeline using Dataflow",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    author="Ivanildo Barauna",
    author_email="ivanildo.jnr@outlook.com",
    url="https://github.com/ivanildobarauna/data-consumer-pipeline",
    packages=find_packages(include=["pipeline", "pipeline.*"]),
    install_requires=["apache-beam[gcp]"],
    include_package_data=True,
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
    ],
    python_requires=">=3.9",
)
