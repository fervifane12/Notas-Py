from setuptools import setup


setup(
    name="paquetes",
    version="2.0",
    description="Saluda, despide y modifica una lista de números",
    author="Fernando Villafañe",
    author_email="fedo@gmail.com",
    url="www.defo.com",
    packages=["Parte_1", "Parte_1.paquetes.adios", "Parte_1.paquetes.hola", "Parte_1.paquetes.modificar_nums"],
    scripts=["test_2.py"]
)