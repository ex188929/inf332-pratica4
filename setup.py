from setuptools import setup, find_packages

setup(
    name="vagago_api",
    version="0.0.1",
    packages=find_packages(),
    install_requires=[
        "flask",
        "flask-apispec",
        "apispec",
        "marshmallow",
    ],
    entry_points={
        "console_scripts": [
            "vagago-api=vagago_api.main:app",
        ],
    },
    author="INF332-Grupo01",
    description="An API based on Flask and Flask-APISpec for VagaGO application.",
    python_requires=">=3.11",
)
