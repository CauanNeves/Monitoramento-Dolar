import aspose.words as aw
import os

class Pdf():
    def word_para_pdf(self, caminho_docx):
        try:
            # Carrega o documento Word
            doc = aw.Document(caminho_docx)
            # Salva como PDF
            caminho_pdf = os.getcwd() + '/cotacao_dolar.pdf'
            doc.save(caminho_pdf)
            print("Documento convertido com sucesso para PDF!")
        except Exception as e:
            print("Erro durante a conversão:", e)