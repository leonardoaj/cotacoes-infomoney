# cotacoes-infomoney

Crawler que faz download de cotações históricas.

Requisitos:
- Python3.6
- pip3
- Google Chrome v83

Instruções:
1. Instalar libs necessárias: `pip install -r requirements.txt`
2. Confirmar a versão do Chrome instalada no sistema. Projeto contém drivers para Chrome 83. Caso a versão seja diferente, basta baixar a versão correspondente em https://chromedriver.chromium.org. Obs: Seguir o padrão de nomenclatura utilizado neste repositório: `chromedriver` para linux, `chromedriver.exe` para windows, `chromedriver-macos` para mac.
3. Inserir datas desejadas na primeira linha do arquivo input.dat, separadas por espaço.
4. Inserir tickets desejados, um por linha após a data. Os tickets deverão corresponder exatamente a uma das opções disponibilizadas no site do infomoney.
5. No diretório raíz, executar `python3 -m crawler.main`
