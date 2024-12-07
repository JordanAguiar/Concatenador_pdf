import PyPDF2
import os

concat = PyPDF2.PdfMerger()

lista_arquivos = os.listdir("arquivos")
lista_arquivos.sort()

for arquivo in lista_arquivos:
    if ".pdf" in arquivo:
        concat.append(f"arquivos/{arquivo}")


concat.write("PDF Final.pdf")