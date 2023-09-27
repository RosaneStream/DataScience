# Descrição do desafio módulo 3 – Processamento de Dados Simplificado com Power BI
##1.	Criação de uma instância na Azure para MySQL

  Cadastrado conta gmail no site https://portal.azure.com/
  Criado o servidor desafio-projeto-dio-rosane.mysql.database.azure.com

##2.	Criar o Banco de dados com base disponível no github
  
  Criada a base de dados azure_company através da execução dos scripts disponibilizados em https://github.com/julianazanelatto/power_bi_analyst/tree/main/M%C3%B3dulo%203/Desafio%20de%20Projeto
  
  Os scripts foram revisados:
- corrigido o nome do schema para que conste somente azure_company
- executado na seguinte sequencia: criação de tabelas,geração de constrainsts e, finalmente, dos inserts.

##3.	Integração do Power BI com MySQL no Azure

  Do Azure, foi baixado o arquivo **desafio-projeto-dio-rosane_azure_company.pbids** para conexão com o Power BI, porém o aplicativo emitiu a mensaguem de que seria necessário atualizar o conector para acessar banco de dados MySQL.
  Foi baixado o conector em https://dev.mysql.com/downloads/connector/net/, porém continuou a não ser reconhecido. Então, foi baixada uma versão anterior, porém sem sucesso.
  A conexão do banco de dados com o Workbench, utilizando as credenciais do Azure ocorreu sem qualquer problema. e, devido a várias tentativas de conexão com o Power BI, as tabelas foram exportadas na máquina local, no formato csv. Dessa forma, foi possível seguir para o carregamento no Power BI.


#4.	Verificar problemas na base a fim de realizar a transformação dos dados

  As tabelas csv baixadas do Workbench foram reunidas num único arquivo Excel, que foi carregado Power BI. No Power BI, ao selecionar as tabelas, foi clicado em 'transformar dados'.


##Diretrizes para transformação dos dados


###1.	Verifique os cabeçalhos e tipos de dados

- Modificado SSN e Super_SSN nas tabelas para texto
- Modificado o nome de algumas colunas para tornar mais significativas

###2.	Modifique os valores monetários para o tipo double preciso

- Modificado campo salario para decimal fixo

###3.	Verifique a existência dos nulos e analise a remoção

- Incluída a informação de gerente no empregado, utilizando ssn de gerente constante na tabela departamento

###4.	Os employees com nulos em Super_ssn podem ser os gerentes. Verifique se há algum colaborador sem gerente

- Checado que não há departamento sem gerente

###5.	Verifique se há algum departamento sem gerente

- Checado que não há departamento sem gerente

###6.	Se houver departamento sem gerente, suponha que você possui os dados e preencha as lacunas

- Não há departamento sem gerente

###7.	Verifique o número de horas dos projetos

- O relacionamento das tabelas trará essa informação no relatório

###8.	Separar colunas complexas

- Modificando campo Address substituindo - por espaço
- Extraída nova coluna do campo Address contendo somente os 2 ultimos dígitos, como State

###9.	Mesclar consultas employee e departament para criar uma tabela employee com o nome dos departamentos associados aos colaboradores. A mescla terá como base a tabela employee. Fique atento, essa informação influencia no tipo de junção

- Mesclado em nova tabela, employee_depart, onde DName foi renomeado como Department

###10.	Neste processo elimine as colunas desnecessárias.

- Excluído campos que pareciam IDs mas não tinham correspondente em outras tabelas

###11.	Realize a junção dos colaboradores e respectivos nomes dos gerentes . Isso pode ser feito com consulta SQL ou pela mescla de tabelas com Power BI. Caso utilize SQL, especifique no README a query utilizada no processo.

- Foi utilizado a tabela employee_depart para realizar a mesclagem de SSN com Super_SSN da tabela employee, onde o campo FName foi atualizado como Manager

###12.	Mescle as colunas de Nome e Sobrenome para ter apenas uma coluna definindo os nomes dos colaboradores

- Criado campo Full_name com junção das colunas nome e sobrenome

###13.	Mescle os nomes de departamentos e localização. Isso fará que cada combinação departamento-local seja único. Isso irá auxiliar na criação do modelo estrela em um módulo futuro.

- Foi Mesclado Location e Department, acrescentada as colunas DName como Departamento, mesclado Dnome com Dlocation, e atualizado o campo como Dept_local em locations

###14.	Explique por que, neste caso supracitado, podemos apenas utilizar o mesclar e não o atribuir.
  
- As tabelas foram mescladas porque são complementares entre si, onde podemos acrescenter as colunas de uma em outra. No entanto, se houvesse dados iguais, poderia ser utilizado o recurso acrescentar.

###15.	Agrupe os dados a fim de saber quantos colaboradores existem por gerente

- Considerando que cada departamento possui um gerente, o relacionamento das tabelas Departament com Employee trará essa informação visível no relatório. No entanto, foi realizada a mesclagem das tabelas para adicionar o nome do gerente em Departament.

###16.	Elimine as colunas desnecessárias, que não serão usadas no relatório, de cada tabela
- Realizado no passo 10 e revisado neste item. 
- Excluí as tabelas: Employee, pois já havia nova consulta com todos os campos da mesma; Dependent, porque não fazia sentido de manter neste contexto analítico financeiro.

