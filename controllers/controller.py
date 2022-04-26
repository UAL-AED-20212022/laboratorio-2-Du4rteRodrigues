from models.LinkedList import LinkedList

def make_list():
    return LinkedList()


def registar_pais_inicio(pais, list_countries):
    list_countries.insert_at_start(pais)
    return


def registar_pais_indice(indice, pais, list_countries):
    indice = int(indice)
    list_countries.insert_at_index(indice, pais)
    return 


def registar_pais_fim(pais, list_countries):
    list_countries.insert_at_end(pais)
    return 


def registar_depois_elemento(pais, pais_reg, list_countries):
    list_countries.insert_after_item(pais_reg, pais)
    return 
    

def registar_antes_elemento(pais, pais_reg, list_countries):
    list_countries.insert_before_item(pais_reg, pais)
    return


def verificar_numero_elementos(list_countries):
    return list_countries.get_count()


def verificar_pais(pais, list_countries):
    if list_countries.search_item(pais):
        return True
    return False
    


def eliminar_pais_inicio(list_countries):
    list_countries.delete_at_start()
    return True


def eliminar_pais_fim(list_countries):
    list_countries.delete_at_end()
    return True


def eliminar_pais(pais, list_countries):
    list_countries.delete_element_by_value(pais)
    return True
