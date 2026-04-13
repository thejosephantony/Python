import copy
import math
import random

class NO:
    def __init__(self,chave,nivel):
        self.chave = chave
        self.prox = [None for x in range(nivel+1)]
        
class SkipList:
    def __init__(self, NivelMAX, P):        
        self.__NivelMAX = NivelMAX
        self.__P = P
        self.__nivel = 0
        self.__inicio = NO(-1,NivelMAX)

    def __sorteiaNivel(self):
        # Sorteia o nÃ­vel para o nÃ³
        r = random.random()
        nivel = 0
        while(r < self.__P and nivel < self.__NivelMAX):
            nivel = nivel + 1
            r = random.random()

        return nivel

    def insere(self, chave):
        atual = self.__inicio
        # Cria um array de nÃ³s auxiliar apontando para None
        aux = [None for x in range(self.__NivelMAX+1)]

        # Partindo do maior nÃ­vel, vÃ¡ para o prÃ³ximo nÃ³
        # enquanto a chave for maior do que a do prÃ³ximo nÃ³
        # Caso contrÃ¡rio, insira o nÃ³ no array auxiliar,
        # desca um nÃ­vel e continue a busca
        for i in range(self.__nivel,-1,-1):
            while(atual.prox[i] != None and atual.prox[i].chave < chave):
                atual = atual.prox[i]
            aux[i] = atual

        # Acesse o nÃ­vel 0 do prÃ³ximo nÃ³, que Ã©
        # onde a chave deve ser inserida
        atual = atual.prox[0]

        # Cria e insere um novo nÃ³ se a chave nÃ£o existir
        # Final da lista (atual == None) ou
        # entre auxiliar[0] e atual
        if(atual == None or atual.chave != chave):
            # Sorteia o nÃ­vel
            novo_nivel = self.__sorteiaNivel()
            # Cria um novo nÃ³ apontando para None
            novo = NO(chave, novo_nivel)

            # Se o nÃ­vel sorteado for maior do que o nÃ­vel
            # atual da SkipList, atualizar os novos nÃ­veis
            # do array auxiliar.
            if(novo_nivel > self.__nivel):
                i = self.__nivel+1
                while(i <= novo_nivel):
                    aux[i] = self.__inicio
                    i = i + 1

                # Atualiza o nÃ­vel da SkipList
                self.__nivel = novo_nivel

            # Insere o nÃ³, arrumando os ponteiros
            for i in range(novo_nivel+1):
                novo.prox[i] = aux[i].prox[i]
                aux[i].prox[i] = novo

            return True

        return False

    def remove(self, chave):
        if(self.__inicio.prox[0] == None):
            return False

        atual = self.__inicio
	# Cria um array de nÃ³s auxiliar apontando para None
        aux = [None for x in range(self.__NivelMAX+1)]

        # Partindo do maior nÃ­vel, vÃ¡ para o prÃ³ximo nÃ³
        # enquanto a chave for maior do que a do prÃ³ximo nÃ³
        # Caso contrÃ¡rio, insira o nÃ³ no array auxiliar,
        # desca um nÃ­vel e continue a busca
        for i in range(self.__nivel,-1,-1):
            while(atual.prox[i] != None and atual.prox[i].chave < chave):
                atual = atual.prox[i]
            aux[i] = atual

        # Acesse o nÃ­vel 0 do prÃ³ximo nÃ³, que Ã©
        # onde a chave a ser removida deve estar
        atual = atual.prox[0];

        # Achou a chave a ser removida?
        if(atual != None and atual.chave == chave):
            # ComeÃ§ando no nÃ­vel 0, se o array auxiliar
            # aponta para o nÃ³ a ser removido, faÃ§a ele
            # apontar para o prÃ³ximo nÃ³ (remoÃ§Ã£o de lista encadeada)
            for i in range(self.__nivel+1):
                if(aux[i].prox[i] != atual):
                    break

                aux[i].prox[i] = atual.prox[i]

            # Remova os nÃ­veis sem elemento
            while(self.__nivel > 0 and self.__inicio.prox[self.__nivel] == None):
                self.__nivel = self.__nivel - 1		

            return True

        return False
        
    def busca(self, chave):
        if(self.__inicio.prox[0] == None):
            return False

        atual = self.__inicio
        
	# Partindo do maior nÃ­vel, vÃ¡ para o prÃ³ximo nÃ³
	# enquanto a chave for maior do que a do prÃ³ximo nÃ³
	# Caso contrÃ¡rio, desca um nÃ­vel e continue a busca
        for i in range(self.__nivel,-1,-1):
            while(atual.prox[i] != None and atual.prox[i].chave < chave):
                atual = atual.prox[i]
        
        # Acesse o nÃ­vel 0 do prÃ³ximo nÃ³, que Ã©
        # onde a chave procurada deve estar
        atual = atual.prox[0]
        if(atual != None and atual.chave == chave):
            return True
        else:
            return False

    def vazia(self):
        if(self.__inicio.prox[0] == None):
            return True
        else:
            return False

    def tamanho(self):
        cont = 0
        atual = sk.__inicio.prox[0]

        while(atual != None):
            atual = atual.prox[0]
            cont = cont + 1
    
        return cont

    def print(self):
        print('*****Skip List*****')
        for i in range(self.__nivel+1):
            no = self.__inicio.prox[i]
            str = 'Nivel %d:' % (i)
            while(no != None):
                str = '%s %d ' % (str,no.chave)
                no = no.prox[i]
            print(str)

#=================================================
vet = [3,6,7,9,12,19,17,26,21,25]

sk = SkipList(10, 0.5)
print('Tamanho: ',sk.tamanho())
print('Vazia: ',sk.vazia())

for v in vet:
    sk.insere(v)
    print('Tamanho: ',sk.tamanho())
    
sk.print()
print('Vazia: ',sk.vazia())

print("Busca: ",sk.busca(12))

sk.remove(12)
print('Tamanho: ',sk.tamanho())
print('Vazia: ',sk.vazia())
sk.print()