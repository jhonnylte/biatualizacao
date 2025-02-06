setwd("C:\\Users\\jhonny.sousa\\Desktop\\bi_atualizacao")
#install.packages("rsconnect")
library(rsconnect)
library(devtools)
# Conta do Vinicius 


system("C:\\Users\\jhonny.sousa\\AppData\\Local\\anaconda3\\python.exe att.py")

data_hora_atual <- Sys.time()
# Formatar a data e hora no formato desejado (exemplo: dd/mm/yyyy HH:MM:SS)
data_hora_formatada <- format(data_hora_atual, "%d/%m/%Y %H:%M:%S")
# Criar um data frame com a data e hora formatada
df <- data.frame(DataHora = data_hora_formatada)
# Escrever o data frame em um arquivo CSV
write.csv(df, file = "datahora.csv", row.names = FALSE)

rsconnect::setAccountInfo(name='igest', token='4AD86E224272B46611C2CB41689B83EB', secret='9ebjFzh5rXdMGJzxldFzrw9tIq2uWC1OULvZMt23')
# Conta do Miguel @TRT7
#rsconnect::setAccountInfo(name='trt7', token='4FA9974AD7C2183D2DCAFD4A9CAF53DE', secret='lI3ZyMxNB568/tWJsS8CW/3b1SUUL7NNHhwjuy+Z')
rsconnect::deployApp("C:\\Users\\jhonny.sousa\\Desktop\\bi_atualizacao")

# renv::settings$snapshot.type("all")
# renv::snapshot()

