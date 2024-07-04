url_cnpj_solicitacoes = 'https://solucoes.receita.fazenda.gov.br/Servicos/cnpjreva/cnpjreva_solicitacao.asp'
name_file = 'input.csv'

#XPATHS
num_inscricao = {
    'cabecalho': 'NUMERO DE INSCRICAO',
    'valor': '//*[@id="principal"]/table[1]/tbody/tr/td/table[2]/tbody/tr/td[1]/font[2]'
}
data_abert = {
    'cabecalho': 'DATA DE ABERTURA',
    'valor': '//*[@id="principal"]/table[1]/tbody/tr/td/table[2]/tbody/tr/td[3]/font[2]'
}
nome_emprs = {
    'cabecalho': 'NOME EMPRESARIAL',
    'valor': '//*[@id="principal"]/table[1]/tbody/tr/td/table[3]/tbody/tr/td/font[2]'
}
nom_fant = {
    'cabecalho': 'TITULO DO ESTABELECIMENTO (NOME DE FANTASIA)',
    'valor': '//*[@id="principal"]/table[1]/tbody/tr/td/table[4]/tbody/tr/td[1]/font[2]'
}
porte = {
    'cabecalho': 'PORTE',
    'valor': '//*[@id="principal"]/table[1]/tbody/tr/td/table[4]/tbody/tr/td[3]/font[2]'
}
cod_descr_princ = {
    'cabecalho': 'CODIGO E DESCRICAO DA ATIVIDADE ECONOMICA PRINCIPAL',
    'valor': '//*[@id="principal"]/table[1]/tbody/tr/td/table[5]/tbody/tr/td/font[2]'
}
cod_descr_secund = {
    'cabecalho': 'CODIGO E DESCRICAO DAS ATIVIDADES ECONOMICAS SECUNDARIAS',
    'valor': '//*[@id="principal"]/table[1]/tbody/tr/td/table[6]/tbody/tr/td/font[2]'
}
cod_descr_jurid = {
    'cabecalho': 'CODIGO E DESCRICAO DA NATUREZA JURIDICA',
    'valor': '//*[@id="principal"]/table[1]/tbody/tr/td/table[7]/tbody/tr/td/font[2]'
}
logradouro = {
    'cabecalho': 'LOGRADOURO',
    'valor': '//*[@id="principal"]/table[1]/tbody/tr/td/table[8]/tbody/tr/td[1]/font[2]'
}
num_logr = {
    'cabecalho': 'NUMERO',
    'valor': '//*[@id="principal"]/table[1]/tbody/tr/td/table[8]/tbody/tr/td[3]/font[2]'
}
complem_logr = {
    'cabecalho': 'COMPLEMENTO',
    'valor': '//*[@id="principal"]/table[1]/tbody/tr/td/table[8]/tbody/tr/td[5]/font[2]'
}
cep = {
    'cabecalho': 'CEP',
    'valor': '//*[@id="principal"]/table[1]/tbody/tr/td/table[9]/tbody/tr/td[1]/font[2]'
}
bairro = {
    'cabecalho': 'BAIRRO-DISTRITO',
    'valor': '//*[@id="principal"]/table[1]/tbody/tr/td/table[9]/tbody/tr/td[3]/font[2]'
}
municipio = {
    'cabecalho': 'MUNICIPIO',
    'valor': '//*[@id="principal"]/table[1]/tbody/tr/td/table[9]/tbody/tr/td[5]/font[2]'
}
uf = {
    'cabecalho': 'UF',
    'valor': '//*[@id="principal"]/table[1]/tbody/tr/td/table[9]/tbody/tr/td[7]/font[2]'
}
ender_eletr = {
    'cabecalho': 'ENDEREÇO ELETRONICO',
    'valor': '//*[@id="principal"]/table[1]/tbody/tr/td/table[10]/tbody/tr/td[1]/font[2]'
}
fone = {
    'cabecalho': 'TELEFONE',
    'valor': '//*[@id="principal"]/table[1]/tbody/tr/td/table[10]/tbody/tr/td[3]/font[2]'
}
efr = {
    'cabecalho': 'ENTE FEDERATIVO RESPONSAVEL (EFR)',
    'valor': '//*[@id="principal"]/table[1]/tbody/tr/td/table[11]/tbody/tr/td/font[2]'
}
situa_cadast = {
    'cabecalho': 'SITUACAO CADASTRAL',
    'valor': '//*[@id="principal"]/table[1]/tbody/tr/td/table[12]/tbody/tr/td[1]/font[2]'
}
data_situa_cadast = {
    'cabecalho': 'DATA DA SITUACAO CADASTRAL',
    'valor': '//*[@id="principal"]/table[1]/tbody/tr/td/table[12]/tbody/tr/td[3]/font[2]'
}
motivo_situa_cadast = {
    'cabecalho': 'MOTIVO DE SITUACAO CADASTRAL',
    'valor': '//*[@id="principal"]/table[1]/tbody/tr/td/table[13]/tbody/tr/td/font[2]'
}
situa_especial = {
    'cabecalho': 'SITUACAO ESPECIAL',
    'valor': '//*[@id="principal"]/table[1]/tbody/tr/td/table[14]/tbody/tr/td[1]/font[2]'
}
data_situa_especial = {
    'cabecalho': 'DATA DA SITUACAO ESPECIAL',
    'valor': '//*[@id="principal"]/table[1]/tbody/tr/td/table[14]/tbody/tr/td[3]/font[2]'
}
