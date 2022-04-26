from views import cli
import sys
sys.stdout.reconfigure(encoding="utf-8") 

if __name__ == '__main__':
    cli.main() 

# Este programa tem o objetivo de acrescentar,
# eliminar, verificar e listar paises tendo em 
# conta o seu indice, posição ou nome.

# RPI pais - Acrescenta o pais no inicio da classe
# RPF pais - Acrescenta o pais no fim da classe
# VNE - Verifica o número de elementos na classe
# RPDE pais pais_registo - Acrescenta o pais depois do pais previamente registado
# RPII pais indice - Acrescenta o pais no indice indicado
# VP pais - Verifica se o pais se encontra registado
# EPE - Elimina o primeiro pais da classe 
# EUE - Elimina o último pais da classe
# EP pais - Elimina o pais indicado