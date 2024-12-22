from setuptools import setup, find_packages

setup(
    name="adjisan-proxy-scraper",
    version="0.1.1",
    author="adjisan",
    author_email="hello.adjisan@gmail.com",
    description="Scrape fast HTTP, HTTPS, SOCKS4, and SOCKS5 proxies.",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/adjidev/proxyscraper",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
