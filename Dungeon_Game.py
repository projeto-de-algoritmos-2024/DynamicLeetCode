class Solution(object):
    def calculateMinimumHP(self, dungeon):
        linha = len(dungeon)
        coluna = len(dungeon[0])

        #cria matrz para o resultado
        nova_matriz = [[0] * coluna for _ in range(linha)]

        #Calcula o valor que o cavalheiro precisa para entrar na ultima casa
        nova_matriz[linha-1][coluna-1] = max(1,1 - dungeon[linha-1][coluna-1])

        #calcula ultima coluna toda pois ele so anda pra direita e para baixo
        for i in range(linha-2, -1,-1):
            nova_matriz[i][coluna-1] = max(1, nova_matriz[i+1][coluna-1] - dungeon[i][coluna-1])
        
        #calcula ultima linha toda pois ele so anda pra direita e para baixo
        for j in range(coluna-2,-1,-1):
            nova_matriz[linha-1][j] = max (1, nova_matriz[linha-1][j+1] - dungeon[linha-1][j])

        for i in range(linha-2, -1,-1):
            for j in range(coluna-2,-1,-1):
                nova_matriz[i][j] = max(1, min(nova_matriz[i+1][j], nova_matriz[i][j+1]) - dungeon[i][j])
        
        return nova_matriz[0][0]


dungeon = [[-2, -3, 3],
           [-5, -10, 1],
           [10, 30, -5]]

teste = Solution()
print(teste.calculateMinimumHP(dungeon)) 
