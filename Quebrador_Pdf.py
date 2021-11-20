# pip install pikepdf and pip install tqdm
import pikepdf
from tqdm import tqdm

ver_senha = False
y = 0
while (y != 1):
    
    ver_arq = 0
    while ver_arq != 1:
        nome_pdf = input('Digite o nome do PDF: ')
        nome_pdf = nome_pdf + '.pdf'
        txt = input('Digite o nome da LISTA: ')
        txt = txt + '.txt'

        # Verificar se os arquivos foram digitados corretamente
        try:
            with open(nome_pdf) as pdf:
                if True:
                    with open(txt) as pdf:
                        if True:
                            ver_arq = 1
        except IOError as e:
            print('\nArquivos não existem\nDigite o nome dos arquivos corretamente\n')

    # Retira espaços em branco da lista
    senhas = [x.strip() for x in open(txt)]

    # Mostra % do progresso
    for senha in tqdm(senhas, 'Descriptografando PDF'):
        #Verifica se as senhas da lista batem com a senha do pdf
        try:
            with pikepdf.open(nome_pdf, password=senha) as pdf:
                print('\n>>>Senha PDF:', senha)
                # Para o programa caso a senha for encontrada
                if True:
                    ver_senha = True
                    break
        except pikepdf._qpdf.PasswordError as e:
            continue

    # Mostra se a senha foi ou não encontrada
    if ver_senha == True:
            print('Senha encontrada')
    else:
        print('Senha não encontrada')
    
    # Menu final programa
    print("\n[MENU]")
    print('0 - Repetir processo')
    print('1 - Finalizar programa')
    y = int(input('Digite a opção desejada: '))

    if y == 1:
        print('Programa finalizando...')
    
    
        

    

