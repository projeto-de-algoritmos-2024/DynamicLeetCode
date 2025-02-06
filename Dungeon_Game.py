class Solution(object):
    def calculateMinimumHP(self, dungeon):
        m, n = len(dungeon), len(dungeon[0])

        nova_matriz = [[0] * n for _ in range(m)]
        
        # vida necessaria na ultima celula
        nova_matriz[m-1][n-1] = max(1, 1 - dungeon[m-1][n-1])

        # preencher a ultima coluna
        for i in range(m-2, -1, -1):
            nova_matriz[i][n-1] = max(1, nova_matriz[i+1][n-1] - dungeon[i][n-1])
        
        # preencher a ultima linha
        for j in range(n-2, -1, -1):
            nova_matriz[m-1][j] = max(1, nova_matriz[m-1][j+1] - dungeon[m-1][j])
        
        # preencher o restante da matriz
        for i in range(m-2, -1, -1):
            for j in range(n-2, -1, -1):
                arvore = min(nova_matriz[i+1][j], nova_matriz[i][j+1])
                nova_matriz[i][j] = max(1, arvore - dungeon[i][j])

        return nova_matriz[0][0]

dungeon = [[-2, -3, 3],
           [-5, -10, 1],
           [10, 30, -5]]

teste = Solution()
print(teste.calculateMinimumHP(dungeon)) 
