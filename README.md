
### Build container

`docker build .`
`docker image ls`

### Run container

something like this

`docker run -p 127.0.0.1:8080:8080 15f3f03eca82`

### To call Microservice 

http://0.0.0.0:8080/aap

### Possible application

Metropolitan Bank Holding Corp. (MCB)  <-  longName, symbol

NYSE | Currency in USD <-  fullExchangeName, financialCurrency

25.36 -9.66 (-27.584236) <- regularMarketPrice, regularMarketChange, regularMarketChangePercent

Previous Close: 35.02 <- regularMarketPreviousClose

Bid: 28.67 <- bid

Ask: 29.0 <- ask

Open: 35.02 <- regularMarketOpen

Day's Range: 22.05 - 35.02 <- regularMarketDayRange

52 Week Range: 13.98 - 104.839 <- fiftyTwoWeekRange

Volume: 5987194 <- regularMarketVolume

Avg. Volume: 312475 <- averageDailyVolume3Month

Market Cap: 277973504 <- marketCap

PE Ratio (TTM): 4.793951 <-  trailingPE

EPS (TTM): 5.29 <- epsTrailingTwelveMonths

Forward Dividend & Yield: 0.0 <- trailingAnnualDividendYield
