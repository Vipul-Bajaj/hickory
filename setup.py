from setuptools import find_packages, setup

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()

setup(
    name="hickory",
    version="1.0.0",
    description="The command line tool for scheduling Python scripts",
    long_description=long_description,
    long_description_content_type="text/markdown",
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Topic :: Office/Business :: Scheduling",
        "Topic :: Terminals",
        "Operating System :: MacOS",
        "Operating System :: POSIX :: Linux",
    ],
    keywords=["schedule", "scheduling", "launchd", "systemd"],
    url="https://github.com/maxhumber/hickory",
    author="Max Humber",
    author_email="max.humber@gmail.com",
    license="MIT",
    packages=find_packages(),
    package_data={"hickory": ["py.typed"]},
    entry_points={"console_scripts": ["hickory=hickory.cli:main"]},
    python_requires=">=3.6",
    setup_requires=["setuptools>=38.6.0"],
    zip_safe=False,
)
