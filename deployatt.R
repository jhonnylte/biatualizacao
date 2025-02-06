#setwd("C:\\Users\\jhonny.sousa\\Desktop\\bi_atualizacao")
#install.packages("rsconnect")
library(rsconnect)

# Conta do Vinicius 


#system("C:\\Users\\jhonny.sousa\\AppData\\Local\\anaconda3\\python.exe att.py")

data_hora_atual <- Sys.time()
# Formatar a data e hora no formato desejado (exemplo: dd/mm/yyyy HH:MM:SS)
data_hora_formatada <- format(data_hora_atual, "%d/%m/%Y %H:%M:%S")
# Criar um data frame com a data e hora formatada
df <- data.frame(DataHora = data_hora_formatada)
# Escrever o data frame em um arquivo CSV
write.csv(df, file = "datahora.csv", row.names = FALSE)

rsconnect::setAccountInfo(name='igest', token='9F778740FB114094DCF24FC14BE280CD', secret='myno+hWuTPBB/aW8gr9jPV1Tj+apj2NskDR2EM0L')
dir()
rsconnect::deployApp(getwd(),appName="teste")



