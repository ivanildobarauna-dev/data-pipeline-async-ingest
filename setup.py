import setuptools

setuptools.setup(
    name="data-consumer-pipeline",
    version="1.0.0",
    install_requires=[
        "apache-beam[gcp]",
    ],
    packages=setuptools.find_packages(),
)
