from StockCorrMatrix import StockCorrelationMatrix
from BetaWeightedDelta import  BetaWeightedDelta
import os

if __name__ == "__main__":
    #check the highest correlation stocks 
    #list the stocks that are repeated
    dir = "./correlation"
    correlationMat, references = StockCorrelationMatrix(dir,plot=False)

    #find reference stock
    print(references)
    print("\n\nselected reference : ")
    reference = list(references.items())[0][0]
    reference = "XIU.TO"
    print(f"{reference}\n")

    #make portfolio
    portfolio = correlationMat[correlationMat.loc[:,reference].notna()]
    portfolio = portfolio.loc[:,reference]
    portfolio = portfolio[portfolio<1]
    print("selected portfolio based on reference correlation:\n")
    print(f"{portfolio}\n")

    for index in os.listdir(dir):
        beta, r_val = BetaWeightedDelta(f"./correlation/{index}", f"./correlation/XIU.TO",plot=False)

        print(f"{index}     {beta:5.3}  {r_val:5.3}")
    
