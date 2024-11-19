from setuptools import setup, Extension

port_scanner_extension = Extension(
    "port_scanner.port_scanner", sources=["src/port_scanner/port_scanner.c"]
)

setup(
    name="port_scanner",
    version="0.1",
    description="A simple port scanner",
    author="<author>",
    author_email="<email>",
    packages=["port_scanner"],
    package_dir={"": "src"},
    ext_modules=[port_scanner_extension],
    install_requires=[],
)
