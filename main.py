from StockCorrMatrix import StockCorrelationMatrix
from BetaWeightedDelts import  BetaWeightedDelta

if __name__ == "__main__":
    #check the highest correlation stocks 
    #list the stocks that are repeated
    dir = "./correlation"
    correlationMat, references = StockCorrelationMatrix(dir,plot=False)

    #find reference stock
    print(references)
    print("\n\nselected reference : ")
    reference = list(references.items())[0][0]
    print(f"{reference}\n")

    #make portfolio
    portfolio = correlationMat[correlationMat.loc[:,reference].notna()]
    portfolio = portfolio.loc[:,reference]
    portfolio = portfolio[portfolio<1]
    print("selected portfolio based on reference correlation:\n")
    print(f"{portfolio}\n")

    for index, value in portfolio.items():
        beta, _ = BetaWeightedDelta(f"./correlation/{index}.csv", f"./correlation/{reference}.csv",plot=False)

        print(f"{index}  {beta:.3}")
    
