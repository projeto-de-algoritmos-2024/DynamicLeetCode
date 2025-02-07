class Solution(object):
    def maximalRectangle(self, matrix):
        linha = len(matrix)
        coluna = len(matrix[0])

        nova_matriz = [[0] * coluna for _ in range(linha)]
        maior_area = 0

        #popula a matriz nova com o valor da altura das colunas
        for i in range(linha):
            for j in range(coluna):
                if matrix[i][j] == "1":
                    nova_matriz[i][j] = 1 if i == 0 else nova_matriz[i-1][j] + 1
                else:
                    nova_matriz[i][j] = 0
            
            maior_area = max(maior_area, self.calculaArea(nova_matriz[i]))
        
        return maior_area
    
    def calculaArea(self, matrix):
        pilha = []
        area = 0
        matrix.append(0)

        for i in range(len(matrix)):
            while pilha and matrix[i] < matrix[pilha[-1]]:
                h = matrix[pilha.pop()]
                w = i if not pilha else i - pilha[-1] - 1
                area = max(area, h * w)
        

            pilha.append(i)

        return area


teste = Solution()

matriz = [["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]

print(teste.maximalRectangle(matriz))
        