from controllers import controller as cr
from models.LinkedList import LinkedList

def main():
    list_countries = cr.make_list()
    while True:
        line = input()
        commands = line.split(" ")

        # Registar pais no inicio da lista
        if commands[0] == "RPI":
            commandRPI(commands,list_countries)

        # Registar pais no indice
        elif commands[0] == "RPII":
            commandRPII(commands,list_countries)

        # Registar pais no fim da lista
        elif commands[0] == "RPF":
            commandRPF(commands,list_countries)

        # Registar pais depois de pais registado
        elif commands[0] == "RPDE":
            commandRPDE(commands,list_countries)
             
        # Registar pais antes de pais registado
        elif commands[0] == "RPAE":
            commandRPAE(commands,list_countries)

        # Verificar número de elementos
        elif commands[0] == "VNE":
            commandVNE(commands,list_countries)

        # Verificar se pais está registado
        elif commands[0] == "VP":
            commandVP(commands,list_countries)
        
        # Eliminar primeiro elemento
        elif commands[0] == "EPE":
            commandEPE(commands,list_countries)

        # Eliminar último elemento
        elif commands[0] == "EUE":
            commandEUE(commands,list_countries)

        # Eliminar pais indicado
        elif commands[0] == "EP":
            commandEP(commands,list_countries)


def commandRPI(commands, list_countries):
    pais_novo = commands[1]
    cr.registar_pais_inicio(pais_novo, list_countries)
    list_countries.traverse_list()


def commandRPII(commands, list_countries):
    pais_novo = commands[1]
    indice = commands[2]
    cr.registar_pais_indice(indice, pais_novo, list_countries)
    list_countries.traverse_list()


def commandRPF(commands, list_countries):
    pais_novo = commands[1]
    cr.registar_pais_fim(pais_novo, list_countries)
    list_countries.traverse_list()


def commandRPDE(commands, list_countries):
    pais_novo = commands[1]
    pais_registado = commands[2]
    cr.registar_depois_elemento(pais_novo, pais_registado, list_countries)
    list_countries.traverse_list()


def commandRPAE(commands, list_countries):
    pais_novo = commands[1]
    pais_registado = commands[2]
    cr.registar_antes_elemento(pais_novo, pais_registado, list_countries)
    list_countries.traverse_list()


def commandVNE(commands, list_countries):
    print(f"O número de elementos são {cr.verificar_numero_elementos(list_countries)}.")

    
def commandVP(commands, list_countries):
    pais_registado = commands[1]
    if cr.verificar_pais(pais_registado, list_countries):
        print(f"O país {pais_registado} encontra-se na lista.")
    else:
        print(f"O país {pais_registado} não se encontra na lista.")


def commandEPE(commands, list_countries):
    primeiro_ele = list_countries.start_node.item
    if cr.eliminar_pais_inicio(list_countries):
        print(f"O país {primeiro_ele} foi eliminado da lista.")

def commandEUE(commands, list_countries):
    ultimo_ele = list_countries.get_last_node()
    if cr.eliminar_pais_fim(list_countries):
        print(f"O país {ultimo_ele} foi eliminado da lista.")


def commandEP(commands, list_countries):
    pais_registado = commands[1]
    if cr.eliminar_pais(pais_registado, list_countries):
        print(f"O país {pais_registado} foi eliminado da lista.")
    else:
        print(f"O país {pais_registado} não se encontra na lista.")

    