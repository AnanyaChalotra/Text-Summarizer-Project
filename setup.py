import setuptools

with open("README.md", "r" , encoding="utf-8") as f:
    long_description = f.read()

__version__ = "0.0.0"

REPO_NAME = "Text-Summarizer-Project"
AUTHOR_USER_NAME = "Ananya-Chalotra"
SRC_REPO = "textSummarizer"
AUTHOR_EMAIL = "chalotraananya@gmail.com"

setuptools.setup(
    name=REPO_NAME,
    version=__version__,
    author=AUTHOR_USER_NAME,
    author_email=AUTHOR_EMAIL,
    description="A Small Python Package for NLP Application",
    long_description=long_description,
    long_description_content="text/markdown",
    url="https://github.com/" + AUTHOR_USER_NAME + "/" + REPO_NAME,
    project_urls={
        "Bug Tracker":f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}/issues",
    },
    package_dir = {"" : "src"}, 
    packages=setuptools.find_packages(where = "src"),
)