# Programa em Python: Cotação do Dólar 💰📈

## Descrição
Este programa em Python utiliza o Selenium para coletar informações de um site de cotação do dólar. Os dados coletados incluem:
- O preço atual do dólar.
- A data da cotação.
- Um print do gráfico do dólar.

O programa salva as informações coletadas em um arquivo `.docx` para facilitar o compartilhamento e registro. 📝

## Funcionalidades ✨
- **Automatização Web**: Utiliza o Selenium para automatizar o processo de coleta de dados.
- **Extração de Dados**: Coleta o preço do dólar e a data correspondente.
- **Captura de Tela**: Realiza a captura do gráfico exibido no site.
- **Geração de Relatório**: Compila as informações em um documento `.docx` bem formatado.

## Requisitos 🛠️
Para executar este programa, você precisa de:
- Python 3.7 ou superior
- Selenium
- Biblioteca `python-docx`
- Um WebDriver compatível com o Selenium (ex.: ChromeDriver para o Google Chrome)

## Instalação 🚀
1. Clone este repositório:
   ```bash
   git clone https://github.com/CauanNeves/Monitoramento-Dolar.git
   cd Monitoramento-Dolar
   ```
2. Instale as bibliotecas necessárias:
   ```bash
   pip install selenium python-docx
   ```
3. Baixe o WebDriver apropriado para o seu navegador e certifique-se de que ele está no PATH do sistema.

## Uso 📋
1. Execute o programa:
   ```bash
   python main.py
   ```
2. O programa irá:
   - Acessar o site especificado.
   - Extrair o preço do dólar e a data.
   - Tirar um print do gráfico do dólar.
   - Salvar todos os dados em um arquivo `.docx` localizado no diretório do projeto.

## Exemplo de Saída 📄
O arquivo `.docx` gerado incluirá:
- Um título.
- O preço do dólar e a data.
- O print do gráfico embutido abaixo do texto.

## Solução de Problemas 🛠️
- Certifique-se de que a versão do WebDriver corresponde à versão do navegador.
- Verifique se o URL do site é acessível e se sua estrutura não mudou.
- Caso ocorram erros, verifique os logs do programa para informações detalhadas.


## Contribuições 🤝
Contribuições são bem-vindas! Sinta-se à vontade para fazer um fork deste repositório e enviar um pull request.

