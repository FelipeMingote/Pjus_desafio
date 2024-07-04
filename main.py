import selenium
from selenium import webdriver
import pandas as pd
from selenium.webdriver.common.by import By
import variables as vb
from time import sleep
def get_cnpjs(input_file):
    df_cnpj = pd.read_csv(input_file)
    cnpj_list = df_cnpj['CNPJs'].tolist()
    return list(set(cnpj_list))


def get_cnpj_solicitacao_data(driver):
    data_dict = {}
    data_dict[vb.num_inscricao['cabecalho']] = driver.find_element(By.XPATH, vb.num_inscricao['valor']).text
    data_dict[vb.data_abert['cabecalho']] = driver.find_element(By.XPATH, vb.data_abert['valor']).text
    data_dict[vb.nome_emprs['cabecalho']] = driver.find_element(By.XPATH, vb.nome_emprs['valor']).text
    data_dict[vb.nom_fant['cabecalho']] = driver.find_element(By.XPATH, vb.nom_fant['valor']).text
    data_dict[vb.porte['cabecalho']] = driver.find_element(By.XPATH, vb.porte['valor']).text
    data_dict[vb.cod_descr_princ['cabecalho']] = driver.find_element(By.XPATH, vb.cod_descr_princ['valor']).text
    data_dict[vb.cod_descr_secund['cabecalho']] = driver.find_element(By.XPATH, vb.cod_descr_secund['valor']).text
    data_dict[vb.cod_descr_jurid['cabecalho']] = driver.find_element(By.XPATH, vb.cod_descr_jurid['valor']).text
    data_dict[vb.logradouro['cabecalho']] = driver.find_element(By.XPATH, vb.logradouro['valor']).text
    data_dict[vb.num_logr['cabecalho']] = driver.find_element(By.XPATH, vb.num_logr['valor']).text
    data_dict[vb.complem_logr['cabecalho']] = driver.find_element(By.XPATH, vb.complem_logr['valor']).text
    data_dict[vb.cep['cabecalho']] = driver.find_element(By.XPATH, vb.cep['valor']).text
    data_dict[vb.bairro['cabecalho']] = driver.find_element(By.XPATH, vb.bairro['valor']).text
    data_dict[vb.municipio['cabecalho']] = driver.find_element(By.XPATH, vb.municipio['valor']).text
    data_dict[vb.uf['cabecalho']] = driver.find_element(By.XPATH, vb.uf['valor']).text
    data_dict[vb.ender_eletr['cabecalho']] = driver.find_element(By.XPATH, vb.ender_eletr['valor']).text
    data_dict[vb.fone['cabecalho']] = driver.find_element(By.XPATH, vb.fone['valor']).text
    data_dict[vb.efr['cabecalho']] = driver.find_element(By.XPATH, vb.efr['valor']).text
    data_dict[vb.situa_cadast['cabecalho']] = driver.find_element(By.XPATH, vb.situa_cadast['valor']).text
    data_dict[vb.data_situa_cadast['cabecalho']] = driver.find_element(By.XPATH, vb.data_situa_cadast['valor']).text
    data_dict[vb.motivo_situa_cadast['cabecalho']] = driver.find_element(By.XPATH, vb.motivo_situa_cadast['valor']).text
    data_dict[vb.situa_especial['cabecalho']] = driver.find_element(By.XPATH, vb.situa_especial['valor']).text
    data_dict[vb.data_situa_especial['cabecalho']] = driver.find_element(By.XPATH, vb.data_situa_especial['valor']).text
    return data_dict.copy()


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    cnpjs = get_cnpjs(vb.name_file)
    driver = webdriver.Chrome()
    result_to_xlsx = []
    #for cnpj in cnpjs:
    #    driver.get(vb.url_cnpj_solicitacoes)
    #    driver.implicitly_wait(10)
    #    sleep(5)
    #    driver.find_element(By.ID, "cnpj").send_keys(cnpj)
    #    driver.implicitly_wait(10)
    #    sleep(15)
    #    driver.find_element(By.CLASS_NAME, "btn-primary").click()
    #    driver.implicitly_wait(30)
    #    result_to_xlsx.append(get_cnpj_solicitacao_data(driver))
    #    driver.quit()
    for cnpj in ['teste1.html', 'teste2.html', 'teste3.html']:
        driver.get('file:///C:/Users/louza/OneDrive/Área%20de%20Trabalho/GitHub/Pjus_desafio/' + cnpj)
        result_to_xlsx.append(get_cnpj_solicitacao_data(driver))
        driver.quit()
    df = pd.DataFrame(result_to_xlsx)
    df.to_excel('output.xlsx', index=False)

