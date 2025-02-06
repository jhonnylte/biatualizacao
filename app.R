#setwd("C:\\Users\\vinicius.marques\\Desktop\\biatualizacao")

library(shiny)
library(bslib)
library(openxlsx)
library(dplyr)
library(stringr)
library(shinythemes)
library(lubridate)
library(DT)
library(shinyjs)
library(tidyverse)
library(RSelenium)
library(shinyBS)

#Ler csv com a data de atualização
datahora <- read.csv("datahora.csv", header = TRUE, sep = ",", stringsAsFactors = FALSE, encoding="UTF-8")

ui <- fluidPage(
 
  tags$head(
    
    tags$link(rel = "stylesheet", href = "https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.15.4/css/all.min.css"),
    tags$script(src = "https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.15.4/js/fontawesome.min.js"),
    tags$title("Atualização"),
    tags$link(rel = "icon", type = "image/png", href = "https://www.trt7.jus.br/media/templates/site/jt_padrao/images/favicon.ico"),
    #Script para o Botão de interrogação | abre um alert popup
    tags$script('
      $(document).on("shiny:connected", function() {
        // Quando o Shiny estiver conectado, vincule eventos à div
        $("#questionMark").on("mouseenter", function() {
          alert("As planilhas serão baixadas com os filtros aplicados");
        });

        
      });
    '),
    #CSS
    tags$style(HTML(
        ".navbar{
                  height: 80px;
                  background-color: #303c54;
                  padding: 5px 0px 5px 10px;
                  position: fixed;
                  width:100%;
                  }
               .textNavTitulo{
                 color:#ffffff;
                 font-size: 16px;
                 
                 }
               .textNav{
               font-family: 'open sans', sans-serif;
                font-weight: bold;
                 color:#FFFFFF;font-size: 16px;
                 padding-top: 10px;
  	             padding-bottom: 20px;
	             }
               .textNav:hover{color:#21ae91;
                
               }
             .navbar-default .navbar-nav>.active>a, .navbar-default .navbar-nav>.active>a:focus, .navbar-default .navbar-nav>.active>a:hover  {
               color: #ffffff;
               height: 70px;
               border-radius: 10px;
               background-color: #1a242f;
               padding: auto;
               marging: auto;
               }
               body {
                font-family: 'Aller', sans-serif;
                font-size: 14px;
               }
              .sidebarPanel{
              
              }
              .well{
                background-color:  #f0f4f4;
                color: #2c3e50;
                font-size: 15px;
                width: max-content;
                display: grid;
              }
              .well .shiny-input-container {
                width:auto;
              }
              .tab-content{
                padding: 95px 0px 0px 0px;
                width:1800px;
                overflow-x: auto;
                
              }
              #downloadHTML{
                width:120px;
                font-size: 15px;
                background-color:#95a5a6;
                padding: 13px 0 13px 0;
                color:white;
            }
             #downloadHTML:hover{
                background-color:#808c8c;
             
             }   #RAdownloadHTML{
                width:120px;
                font-size: 15px;
                background-color:#95a5a6;
                padding: 13px 0 13px 0;
                color:white;
            }
             #RAdownloadHTML:hover{
                background-color:#808c8c;
             
             }
                
            #downloadPDF{
              width:120px;
              font-size: 15px;
              background-color:#95a5a6;
              padding: 13px 0 13px 0;
              color:white;
            }
             #RAdownloadPDF{
              width:120px;
              font-size: 15px;
              background-color:#95a5a6;
              padding: 13px 0 13px 0;
              color:white;
            }
             #downloadCSV{
              width:120px;
              font-size: 15px;
              background-color:#95a5a6;
              padding: 13px 0 13px 0;
              color:white;
             }
            
            .questionMark{
              width:30px;
              height:30px;
              font-size: 15px;
              border-radius:500px;
              background-color:#95a5a6;
              padding: 13px 0 13px 0;
              color:white;
              display:flex;
              justify-content:center;
              align-items:center;
              border: solid 2px #01426a;
            }
            
            .container {
  display: flex;
  justify-content: center;
  align-items: center;
  height:70vh;
  width:94vw;
}
             #downloadPDF:hover{
              background-color:#808c8c;
             
             }
              #RAdownloadPDF:hover{
              background-color:#808c8c;
             
             }
             #downloadCSV:hover{
              background-color:#808c8c;
             
            }
            #footer {
              background-color: #303c54;
              color: white;
              display: flex;
              flex-direction: column;
              padding: 20px;
              height: 100%;
              height: 15vh;
              margin: 0rem 0rem ;
              text-align: center;
            }
            
            .atualizado{
              color: #303c54
            }
            .no-footer{
              width: max-content;
              display: grid;
            }
            
            #meuGrafico {
                position: relative;
               
            }

            .main-panel {
           
                width:100%;
            }
            
            .destacar {
          color: red;
}
        
}
          
            
               "

    ))
    
  ),
 
  
  navbarPage(
    div(#44
      img(src = "https://i.ibb.co/7XFP8N9/Coordenadoria-de-Estat-tica-BRANCA-1-1.png", width = "220px", height = "50px", class="Navbar")
    ),
   
    tabPanel(div("Atualização dos Painéis", class= "textNav"),
             #actionButton("show", "Confluence"),
             #bsModal("modalExample", "Documentações SGGE", "show",
            #         "https://confluence.trt7.jus.br/confluence/pages/viewpage.action?pageId=22938627"),
            actionButton("link_externo", "Confluence",onclick= 'var win = window.open("https://confluence.trt7.jus.br/confluence/pages/viewpage.action?pageId=22938627", "Google"); win.addEventListener("load", function() { win.document.documentElement.requestFullscreen(); });'),
        
          
             titlePanel(  div(class="well ", style = " width 100vw ;display: flex;justify-content: center; align-items: center;",paste0("Atualizado em: \n",datahora))),
             div(class="well container ",style="padding-left:10vw ;",
              DT::dataTableOutput("tabela")),
            bsModal("modalExample", "Como Atualizar o Painel?", "show",
                    textOutput("modalText"))
           
             
           
    )
   

  ),
  
  
  footer <-  div(
    id = "footer",
    fluidRow(
      column(
        3,
        div(
          style = "text-align: center; margin: 0 auto;",
          img(src = "https://www.trt7.jus.br/organogramainstitucional/resources/logo-transparente.png", height = "80px", width="100px")  # Substitua com a URL da sua imagem
        )
      ),
      column(4, 
             p(HTML(paste(icon("map-marker"),"Tribunal Regional do Trabalho da 7ª Região"))),
             p("Av. Santos Dumont, 3384, Aldeota - Fortaleza/CE"),
             p("CEP: 60.150-162")),
      column(4, 
             p(HTML(paste(icon("phone"),"Telefones: (85) 3388-9295"))),
             p(HTML(paste(icon("clock"),"Horário de funcionamento:"))),
             p("De segunda a sexta-feira, das 08h30 às 16h30"))
    )
  )
  
  
)


server <- function(input, output) {
 
  # Lê o arquivo CSV
  dados <- read.csv("dados.csv", header = TRUE, sep = ",", stringsAsFactors = FALSE, encoding="UTF-8")
  
  # Renderiza a tabela com o conteúdo do CSV
  output$tabela <- DT::renderDataTable({
    DT::datatable(dados, escape = FALSE,selection = 'single',
                  options = list(pageLength = 10, paging = TRUE,info=FALSE,lengthChange = FALSE,columnDefs = list(list(
                    targets = 0,
                    visible = FALSE
                  ),
                    list(
                      targets = 3, 
                      render = JS(
                        "function(data, type, row, meta) {",
                        "  return '<a href='+data+' target=\"_blank\"><i class=\"fa fa-link\"></i></a>';",
                        "}"
                      )
                    ),
                  list(
                    targets = 5, 
                    render = JS(
                      "function(data, type, row, meta) {",
                      "  return '<button type=\"button\" class=\"btn btn-primary\" data-toggle=\"modal\" data-target=\"#modalExample\" data-row=' + row + '>Ver</button>';",
                      "}"
                    )
                  )))
    )
  })
 
  output$modalText <- renderText({
    req(input$tabela_rows_selected)
    dados[input$tabela_rows_selected, 5] 
    # print(input$tabela_rows_selected)# Ajustar o índice da coluna
  })
  
}

shinyApp(ui = ui, server = server)
