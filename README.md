# Portfolio Management with beta weighted delta (Directional Risk)

![BetaWeigtedDeltaBanner](./readme%20files/cityscape.jpg)

> A tool that helps manage the directional risk of your portfolio. 


---

### Table of Contents


- [Portfolio Management with beta weighted delta (Directional Risk)](#portfolio-management-with-beta-weighted-delta-directional-risk)
    - [Table of Contents](#table-of-contents)
  - [Description](#description)
      - [Technologies](#technologies)
  - [How To Use](#how-to-use)
      - [Installation](#installation)
      - [API Reference](#api-reference)
  - [References](#references)
  - [Author Info](#author-info)

---

## Description

The purpose of this code is to take your portfolio of stocks, normalize the portfolios price changes to a whole market etf and control directional risk.

The delta value's of your stocks and options can be added up to get a whole portfolio delta. Then all you need to do is look at your reference etf and estimate how your own portfolio is going to move. 

If you have positive delta and the market is going up, then you can add to your positions. 
Positive delta in a bear market, then you can sell call options or add to your short / negative delta positions. 

The idea is all you need to get a handle of your portfolio is to look at one stock, the whole market etf. Usually people default to SPY, but this tool will even help you choose your best reference etf.

#### Technologies

- Beta Weighted Delta of Options and Underlyings
- Correlation Matrix of Portfolio to Reference Stocks

[Back To The Top](#read-me-template)

---

## How To Use

#### Installation
Currently the project consists of 3 functions. Two to find the beta weighted delta of stocks and Options and another to draw a correlation matrix. So to install you simply download and use the functions as you see fit. 
An example of its use is given in main.py which you can run in python. 


#### API Reference
What to import 
```python
    from StockCorrMatrix import StockCorrelationMatrix
    from BetaWeightedDelts import  BetaWeightedDelta
```
Inputs And Outputs

``` 
    StockCorrelationMatrix(dir, plot = True)

        Input : 
            dir -> directory of all stock data 
            plot -> if you want to see a heat map of the correlation matrix
        Output : 
            corr_sorted  :  Correlation Matrix
            highest_corr :  Stocks with the higher number of correlation to
            other stocks in the folder. This can be used as the reference stock.  
        

    BetaWeightedOption(beta, StockPrice, ReferencePrice, OptionDelta)
        
        To calculate the beta weighted delta on an option. 

     

        Input: 
            beta : beta of underlying 
            StockPrice : Current Price of underlying 
            ReferencePrice : Current Price of the stock you beta weighted the 
            portfolio to 
            OptionDelta : The Delta value of the option you want to trade 
            (belonging to the underlying you 
            provided.)
        Output: 
            beta : beta of option weighted to the reference stock. 
    
    BetaWeightedDelta(StockName, ReferenceName, plot = True)

        Find the beta of a underlying using historic price data. You can 
        download price data off of yahoo finance. 

        Inputs : 
            StockName = Directory to you Stock (use the stock ticker as file 
            name)
            ReferenceName = Directory to you Stock (use the stock ticker as 
            file name)
            
            Use yahoo finance histric prices and place them all in the same 
            folder. 
            The number of data points can be different, the function will 
            adjust the sizes. 
            
            plot : If you want to see a plot of the percent price changes and 
            the beta regression line you also get the R^2 value for a wellness 
            of fit. 
               
      Output : 
            Beta : beta weighting of your stocks  delta 
            R^2 : wellness of fit of the beta  
   
```
[Back To The Top](#read-me-template)

---
## References

On How To Code Yourself:

    [1] Kevin Mooney (2020) How to Calculate Beta-Weighted Delta. Available     
        at: [YouTube](https://www.youtube.com/watch?v=YLxV5L6IaFA) (Accessed: 23 
        August 2020).

    [2] Kevin Mooney (2020) Calculating the Correlations Between Stocks Using 
        Python. Available at: 
        [YouTube](https://www.youtube.com/watch?v=Oa7br3Okxac&t=190s) 
        (Accessed: 23 August 2020).

On How To Manage A Core Portfolio and Use Beta Weighted Delta:

    [3] T. (2016). Small Accounts: The Core Portfolio (1 of 6). Retrieved 
        August 23, 2020, from 
        [tastytrade.com](https://bit.ly/2Et98eA) 

[Back To The Top](#read-me-template)

---

## Author Info

- LinkedIn - [@sina sartipzadeh](https://www.linkedin.com/in/sinasartipzadeh/)


[Back To The Top](#read-me-template)
