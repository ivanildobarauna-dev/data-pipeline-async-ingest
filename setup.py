from setuptools import setup, find_packages

setup(
    name="data-consumer-pipeline",
    version="1.0.0",
    description="Consumer Pipeline Dataflow",
    author="Ivanildo Barauna",
    author_email="ivanildo.jnr@outlook.com",
    packages=find_packages(where="pipeline"),
    package_dir={"": "pipeline"},
    install_requires=[
        "apache-beam[gcp]",
    ],
    package_data={
        "": ["*.py", "*.txt", "*.json"],  # Inclui arquivos .py, .txt, e .json no pacote
    },
    include_package_data=True,
    zip_safe=False,
)
