from setuptools import setup, find_packages
import codecs
from version import __version__

setup(
    name="explainaboard",
    version=__version__,
    description="Explainable Leaderboards for Natural Language Processing",
    long_description=codecs.open("README.md", encoding="utf-8").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/ExpressAI/ExplainaBoard",
    author="Pengfei Liu",
    license="MIT License",
    classifiers=[
        "Intended Audience :: Developers",
        "Topic :: Text Processing",
        "Topic :: Scientific/Engineering :: Artificial Intelligence",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
    ],
    packages=find_packages(),
    # packages=find_packages("explainaboard"),
    # package_data={
    #     "":["*.txt"],
    #     "tasks":["ner/*.aspects","ner/*.json"],
    # },
    entry_points={
        "console_scripts": [
            "explainaboard=explainaboard.explainaboard_main:main",
        ],
    },
    install_requires=[
        "nltk>=3.2",
        "numpy",
        "scipy",
        "matplotlib",
        "scikit-learn",
        "seqeval",
        "pandas",
        "pyarrow",
        "eaas",
        "wheel",
        "tqdm",
        "sacrebleu",
        "datasets",
        "lexicalrichness",
        "spacy",
        "en_core_web_sm@https://github.com/explosion/spacy-models/releases/download/en_core_web_sm-3.2.0/en_core_web_sm-3.2.0-py3-none-any.whl"
    ],
    include_package_data=True,
)
