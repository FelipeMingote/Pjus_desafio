# Pjus_desafio
O desafio era:
 
 1- Ler o arquivo csv de input, contendo os CNPJs a serem consultados;\
 2- Acessar o site https://solucoes.receita.fazenda.gov.br/Servicos/cnpjreva/cnpjreva_solicitacao.asp \
 3- Preencher o campo CPNJ com o CNPJ desejado;\
 4- Resolver captcha; Obs: Esta pode ser uma ação manual caso não haja API de resolução de captcha.\
 5- Validar se o CNPJ foi encontrado, caso não tenha sido, registrar esta informação;\
 6- Obter todos os dados resultantes da consulta, associando o cabeçalho e seu respectivo valor;\
 7- Escrever o resultado de todas as consultas em uma planilha com os cabeçalhos e valores coletados;

O desafio não foi completado, a parte principal da automação não funcionou bem, havendo um problema onde a busca feita dentro do Chrome pelo Selenium não retornava resultado, o site considerava como erro a busca e não retornava os dados necessários para scrapping, o que foi estranho pois a mesma busca de maneira manual retornava resultado, utilizando o mesmo input da mesma maneira. Uma alternativa que foi implantada é de fazer a busca na mão, salvar o HTML localmente e abrir aquele HTML salvo para buscar as informações, de maneira a simular a automação e a coleta dos dados, foram feitas 3 buscas manuais para validar padrão. Então, em suma, o que foi realizado foi:

 - Listagem dos CNPJs e filtro removendo possíveis duplicatas
 - Esqueleto e esboço da automação via Selenium
 - Mapeamento das informações e saída via xlsx dos CNPJ padronizada.

Com mais tempo e investigação, falta ser ajustado e/ou implementado:
 - Automação funcional com resolução do captcha
 - Tratar exceção de quando o CNPJ não for encontrado/não possuir dados para scrapping.
