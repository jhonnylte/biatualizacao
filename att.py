from selenium import webdriver
from time import sleep
import csv
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
#from selenium.webdriver.firefox.options import Options
#options = Options()
#options.headless = True 

#from selenium.webdriver.firefox.options import Options as FirefoxOptions
#from selenium import webdriver

# options = FirefoxOptions()
# options.add_argument("--headless")



driver = webdriver.Chrome()
#IGEST
driver.get('https://app.powerbi.com/view?r=eyJrIjoiYjExZGVmZTgtNjU0NC00MDAwLWJkYzgtNThlYjQwYTJhMDNhIiwidCI6IjYxOGE5ZWVkLWYxM2MtNDU4Ny1iODgzLTAwNWZiY2Q4N2FlZCJ9')
sleep(10)
soup = BeautifulSoup(driver.page_source, 'html.parser')
IGEST = soup.find('tspan').text
#HALO
driver.get('https://app.powerbi.com/view?r=eyJrIjoiMmNlMTIzOWMtODJhNC00ZjYyLTlhMmEtMTJiN2RhMDZhYWVjIiwidCI6IjYxOGE5ZWVkLWYxM2MtNDU4Ny1iODgzLTAwNWZiY2Q4N2FlZCJ9')
sleep(10)
soup = BeautifulSoup(driver.page_source, 'html.parser')
HALO = soup.find_all('g')[-2].text
#HERMES
driver.get('https://app.powerbi.com/view?r=eyJrIjoiMmQ0NmE2ZjUtNjRkMi00ZjI3LWFlM2QtN2RhNGJmYTBjMjFlIiwidCI6IjYxOGE5ZWVkLWYxM2MtNDU4Ny1iODgzLTAwNWZiY2Q4N2FlZCJ9')
sleep(10)
soup = BeautifulSoup(driver.page_source, 'html.parser')
HERMES = soup.find_all('g')[-2].text
#AÇÕES
driver.get('https://app.powerbi.com/view?r=eyJrIjoiMmUzMDJiYTgtYjFjZS00ODVmLWIxMmUtNGFhMTc5MmIyNjAyIiwidCI6IjYxOGE5ZWVkLWYxM2MtNDU4Ny1iODgzLTAwNWZiY2Q4N2FlZCJ9')
sleep(10)
soup = BeautifulSoup(driver.page_source, 'html.parser')
ACOES = soup.find_all('tspan')[-1].text
#AÇÕES PJE
driver.get('https://app.powerbi.com/view?r=eyJrIjoiMmUzMDJiYTgtYjFjZS00ODVmLWIxMmUtNGFhMTc5MmIyNjAyIiwidCI6IjYxOGE5ZWVkLWYxM2MtNDU4Ny1iODgzLTAwNWZiY2Q4N2FlZCJ9')
sleep(10)
soup = BeautifulSoup(driver.page_source, 'html.parser')
ACOESPJE = soup.find_all('tspan')[-1].text
#TRT 7 EM NÚMEROS
driver.get('https://app.powerbi.com/view?r=eyJrIjoiNTZhZTIzY2QtMGY2My00NDZkLWE4MDUtMWI3Y2ViMTRiNzQ5IiwidCI6IjYxOGE5ZWVkLWYxM2MtNDU4Ny1iODgzLTAwNWZiY2Q4N2FlZCJ9')
sleep(10)
soup = BeautifulSoup(driver.page_source, 'html.parser')
TRT7 = soup.find_all('tspan')[-1].text
#Relatório de desempenho IGEST
driver.get('https://igest.shinyapps.io/home/')
sleep(10)
soup = BeautifulSoup(driver.page_source, 'html.parser')
RDIGEST = soup.find_all('strong')[1].text
#Pendentes de solução
driver.get('https://trt7.shinyapps.io/pendentes_de_soluo/')
sleep(10)
soup = BeautifulSoup(driver.page_source, 'html.parser')
PENDESOL = soup.find_all('strong')[1].text
#Aptos a Julgamento
driver.get('https://app.powerbi.com/view?r=eyJrIjoiYjliODY4ZWUtOTZkYy00MjE0LWI1N2MtYzEyYTJkODRkZTJiIiwidCI6IjYxOGE5ZWVkLWYxM2MtNDU4Ny1iODgzLTAwNWZiY2Q4N2FlZCJ9')
sleep(10)
soup = BeautifulSoup(driver.page_source, 'html.parser')
APTOS = soup.find_all('text')[0].text
#BITurmas
driver.get('https://app.powerbi.com/view?r=eyJrIjoiMWVmMTNhMzktYmQ3My00MTViLWIzODUtOTA5NjUzZTg4YWVhIiwidCI6IjYxOGE5ZWVkLWYxM2MtNDU4Ny1iODgzLTAwNWZiY2Q4N2FlZCJ9')
sleep(10)
soup = BeautifulSoup(driver.page_source, 'html.parser')
element = soup.find_all('div', {'aria-valuetext': True})[-1]
BITURMAS = element['aria-valuetext']
#BIREMESSA
driver.get('https://app.powerbi.com/view?r=eyJrIjoiNGVhYWFkYTYtZGYzNC00ZThlLWIwMDUtODFhNzdhYmZjMGFhIiwidCI6IjYxOGE5ZWVkLWYxM2MtNDU4Ny1iODgzLTAwNWZiY2Q4N2FlZCJ9')
sleep(10)
soup = BeautifulSoup(driver.page_source, 'html.parser')
BIREMESSA = soup.find_all('tspan')[-3].text
#PendentesPrazoVencido
driver.get('https://app.powerbi.com/view?r=eyJrIjoiNjNkYzhlYWYtMGI3Yi00NjU5LTk2OWEtODE0MmMxZTQxYjljIiwidCI6IjYxOGE5ZWVkLWYxM2MtNDU4Ny1iODgzLTAwNWZiY2Q4N2FlZCJ9')
sleep(10)
soup = BeautifulSoup(driver.page_source, 'html.parser')
PENDENTESPRAZOVENCIDO = soup.find_all('tspan')[1].text
#BIAssuntos
driver.get('https://app.powerbi.com/view?r=eyJrIjoiYjY3NTdhNmMtN2Q1ZS00YmQyLWJmZTUtYTIyYTQzYTAyNjYwIiwidCI6IjYxOGE5ZWVkLWYxM2MtNDU4Ny1iODgzLTAwNWZiY2Q4N2FlZCJ9')
sleep(10)
soup = BeautifulSoup(driver.page_source, 'html.parser')
BIASSUNTOS = soup.find_all('tspan')[0].text

with open('dados.csv', mode='w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    
    # Cabeçalhos do CSV
    writer.writerow(['PAINEL', 'DATA','LINK','REDE','ATUALIZAR'])
    
    # Escreve as variáveis em uma nova linha
    
    writer.writerow(["PENDENTES DE SOLUÇÃO (Diário-1)",PENDESOL,"https://trt7.shinyapps.io/pendentes_de_soluo/","X:\SGE\GABINETE\Shiny\PENDENTES DE SOLUÇÃO","Acesse o endereço de rede. Caso já tenha configurado o ambiente, é suficiente executar o arquivo 'atualizacao.R'. Veja a documentação completa em: https://confluence.trt7.jus.br/confluence/pages/viewpage.action?pageId=89104928"])
    writer.writerow(["HALO (Diário)",HALO,"https://app.powerbi.com/view?r=eyJrIjoiMmQ0NmE2ZjUtNjRkMi00ZjI3LWFlM2QtN2RhNGJmYTBjMjFlIiwidCI6IjYxOGE5ZWVkLWYxM2MtNDU4Ny1iODgzLTAwNWZiY2Q4N2FlZCJ9","X:\SGE\GABINETE\BI HALO","OBS: Esse BI atualiza automaticamente pelo serviço web. Acesse o endereço de rede. Abra o arquivo 'Análise de Fluxo - PJE.pbix'.  Clique no Botão 'Atualizar'.  Clique no Botão 'Publicar' "])
    writer.writerow(["HERMES (Diário)",HERMES,"https://app.powerbi.com/view?r=eyJrIjoiMmQ0NmE2ZjUtNjRkMi00ZjI3LWFlM2QtN2RhNGJmYTBjMjFlIiwidCI6IjYxOGE5ZWVkLWYxM2MtNDU4Ny1iODgzLTAwNWZiY2Q4N2FlZCJ9","X:\SGE\GABINETE\BI HERMES","OBS: Esse BI atualiza automaticamente pelo serviço web. Acesse o endereço de rede. Abra o arquivo 'Painel Hermes.pbix'.  Clique no Botão 'Atualizar'.  Clique no Botão 'Publicar' "])
    writer.writerow(["AÇÕES PRIORITÁRIAS PJE (Diário)",ACOESPJE,"https://app.powerbi.com/view?r=eyJrIjoiMmUzMDJiYTgtYjFjZS00ODVmLWIxMmUtNGFhMTc5MmIyNjAyIiwidCI6IjYxOGE5ZWVkLWYxM2MtNDU4Ny1iODgzLTAwNWZiY2Q4N2FlZCJ9","X:\SGE\GABINETE\BI PROCESSOS COM TRAMITAÇÃO PRIORITÁRIA PENDENTES DE BAIXA IDOSOS", "OBS: Esse BI atualiza automaticamente pelo serviço web. Acesse o endereço de rede. Abra o arquivo 'Processos com tramitação prioritária pendentes de baixa_17022023_PJE.pbix'.  Clique no Botão 'Atualizar'.  Clique no Botão 'Publicar'"])
    writer.writerow(["AÇÕES PRIORITÁRIAS (Diário)",ACOES,"https://app.powerbi.com/view?r=eyJrIjoiMmUzMDJiYTgtYjFjZS00ODVmLWIxMmUtNGFhMTc5MmIyNjAyIiwidCI6IjYxOGE5ZWVkLWYxM2MtNDU4Ny1iODgzLTAwNWZiY2Q4N2FlZCJ9","X:\SGE\GABINETE\BI PROCESSOS COM TRAMITAÇÃO PRIORITÁRIA PENDENTES DE BAIXA IDOSOS","OBS: Esse BI atualiza automaticamente pelo serviço web. Acesse o endereço de rede. Abra o arquivo 'Processos com tramitação prioritária pendentes de baixa_17022023.pbix'.  Clique no Botão 'Atualizar'.  Clique no Botão 'Publicar'"])
    writer.writerow(["IGEST (Mensal)",IGEST,"https://app.powerbi.com/view?r=eyJrIjoiYjExZGVmZTgtNjU0NC00MDAwLWJkYzgtNThlYjQwYTJhMDNhIiwidCI6IjYxOGE5ZWVkLWYxM2MtNDU4Ny1iODgzLTAwNWZiY2Q4N2FlZCJ9","X:\SGE\GABINETE\BI IGEST\igest1","Acesse o endereço na rede. Execute os scripts 'tab_princ.R' e 'prepara_dataset.R'. A execução desses scripts resultará na criação dos arquivos .csv com os dados necessários para que o painel seja atualizado. Com os dados gerados, Abra o aquivo 'igest.pbix'.  Clique no Botão 'Atualizar'.  Clique no Botão 'Publicar.  "])
    writer.writerow(["TRT7 EM NÚMEROS (Mensal) ",TRT7,"https://app.powerbi.com/view?r=eyJrIjoiNTZhZTIzY2QtMGY2My00NDZkLWE4MDUtMWI3Y2ViMTRiNzQ5IiwidCI6IjYxOGE5ZWVkLWYxM2MtNDU4Ny1iODgzLTAwNWZiY2Q4N2FlZCJ9","X:\SGE\GABINETE\BI TRT7 EM NUMEROS ATUALIZADO","Acesse o endereço de rede. Abra o arquivo 'TRT 7 EM NÚMEROS - IMPLEMENTANDO.pbix'.  Clique no Botão 'Atualizar'.  Clique no Botão 'Publicar'"])
    writer.writerow(["RELATÓRIO DE DESEMPENHO IGEST (Mensal)",RDIGEST,"https://igest.shinyapps.io/home/","X:\SGE\GABINETE\Shiny\IGest RMD","Acesse o endereço na rede. Execute o arquivo 'consultas.R'. Execute o arquivo 'gerador.R'.'Mova os 112 arquivos para a pasta home dentro da pasta shinyapp: 37 html + 37 pdf + 37xlsx com os nomes da varas + o arquivos nomesvara.xlsx. Execute o Script deploy.R "])
    writer.writerow(["APTOS A JULGAMENTO (Mensal)",APTOS,"https://app.powerbi.com/view?r=eyJrIjoiYjliODY4ZWUtOTZkYy00MjE0LWI1N2MtYzEyYTJkODRkZTJiIiwidCI6IjYxOGE5ZWVkLWYxM2MtNDU4Ny1iODgzLTAwNWZiY2Q4N2FlZCJ9","X:\SGE\GABINETE\BI PROCESSOS APTOS A JULGAMENTO","Acesse o endereço de rede. Abra o arquivo 'Provimento_4_2018_CGJT_NEW_QUERY.pbix'.  Clique no Botão 'Atualizar'.  Clique no Botão 'Publicar'"])
    writer.writerow(["MOVIMENTAÇÃO PROCESSUAL DOS ÓRGÃOS JULGADORES (Mensal)",BITURMAS,"https://app.powerbi.com/view?r=eyJrIjoiMWVmMTNhMzktYmQ3My00MTViLWIzODUtOTA5NjUzZTg4YWVhIiwidCI6IjYxOGE5ZWVkLWYxM2MtNDU4Ny1iODgzLTAwNWZiY2Q4N2FlZCJ9","X:\SGE\GABINETE\BI TURMAS"," Acesse o endereço de rede. Abra o arquivo 'Acompanhamento Turmas.pbix'.  Clique no Botão 'Atualizar'.  Clique no Botão 'Publicar'"])
    writer.writerow(["ACOMPANHAMENTO DAS CARGAS (Diário)",BIREMESSA,"https://app.powerbi.com/view?r=eyJrIjoiNGVhYWFkYTYtZGYzNC00ZThlLWIwMDUtODFhNzdhYmZjMGFhIiwidCI6IjYxOGE5ZWVkLWYxM2MtNDU4Ny1iODgzLTAwNWZiY2Q4N2FlZCJ9","X:\SGE\GABINETE\Shiny\BI Remessa","OBS: Esse BI atualiza automaticamente pelo serviço web. Acesse o endereço de rede. Abra o arquivo 'BI Remessa.pbix'.  Clique no Botão 'Atualizar'.  Clique no Botão 'Publicar'"])
    writer.writerow(["PROCESSOS PENDENTES COM O PRAZO VENCIDO(Diário-1)",PENDENTESPRAZOVENCIDO,"https://app.powerbi.com/view?r=eyJrIjoiNjNkYzhlYWYtMGI3Yi00NjU5LTk2OWEtODE0MmMxZTQxYjljIiwidCI6IjYxOGE5ZWVkLWYxM2MtNDU4Ny1iODgzLTAwNWZiY2Q4N2FlZCJ9","X:\SGE\GABINETE\BI Pendentes com o relator","OBS: Esse BI atualiza automaticamente pelo serviço web. Acesse o endereço de rede. Abra o arquivo 'pendentes com o relator.pbix'.  Clique no Botão 'Atualizar'.  Clique no Botão 'Publicar'"])
    writer.writerow(["RECURSOS DISTRIBUÍDOS NO 2º GRAU POR ASSUNTO (Mensal)",BIASSUNTOS,"https://app.powerbi.com/view?r=eyJrIjoiYjY3NTdhNmMtN2Q1ZS00YmQyLWJmZTUtYTIyYTQzYTAyNjYwIiwidCI6IjYxOGE5ZWVkLWYxM2MtNDU4Ny1iODgzLTAwNWZiY2Q4N2FlZCJ9","X:\SGE\GABINETE\BI ASSUNTOS"," Acesse o endereço de rede. Abra o arquivo 'Painel de Assuntos.pbix'.  Clique no Botão 'Atualizar'.  Clique no Botão 'Publicar' "])
driver.quit()

