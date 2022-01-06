from setuptools import find_packages, setup

DESCRIPTION = "Text Classification with Sklearn"

requirements = [
    "pandas==1.3.5",
    "transformers==4.14.1",
    "scikit-learn==0.23.2",
    "numpy==1.21.5",
    "fsspec==2021.11.1",
    "gcsfs==2021.11.1",
    "google-cloud-storage==1.43.0"
]

setup(
    name="sklearn-text-classification",
    version="0.1",
    description=DESCRIPTION,
    long_description=DESCRIPTION,
    author_email="dev@aliz.ai",
    package_dir={"": "src"},
    packages=find_packages("src"),
    package_data={"": ["*.py"]},
    install_requires=requirements,
)
