class Solution(object):

    def maxProfit(self,prices):

        if not prices:
            return 0

        # inicializando com infinito negativo em comprar1 e comprar2 para garantir que -price eh sempre maior que comprar1
        # vender1 e vender2 inicializados com 0 pois faremos somas neles
        
        # comprar1: lucro máximo depois da primeira compra
        comprar1 = float('-inf')
        # vender1: lucro máximo depois da primeira venda
        vender1 = 0
        # comprar2: lucro máximo depois da segunda venda
        comprar2 = float('-inf')
        # vender2: lucro máximo depois da segunda venda
        vender2 = 0

        for price in prices:
            comprar1 = max(comprar1, -price)
            vender1 = max(vender1, comprar1 + price)
            comprar2 = max(comprar2, vender1 - price)
            vender2 = max(vender2, comprar2 + price)
            
        return vender2

teste = Solution()
