# Tokima

## Tools for my own use. using Akamai API

<<<<<<< HEAD
To use Akamai API you need some formatted date 'from' and 'to' as '2015-01-31' in 
[List Products per Contract](https://developer.akamai.com/api/luna/contracts/resources.html#getproductspercontract)  
or in [List Usage per Contract](https://developer.akamai.com/api/luna/billing-usage/resources.html#getcontractmeasure) 

    tokima = TokimaDate(year="2018", month="6")
    
    tokima.month -> 6
    tokima.year ->  2018
    tokima.year_month -> "2018-06"
    tokima.first_day() ->  "2018-06-01"
    tokima.last_day() ->  "2018-06-30"
    tokima.day_numbers -> 30
=======
To use Akamai API you need some formatted date
'from' and 'to' as '2015-01-31' in [List Products per Contract](https://developer.akamai.com/api/luna/contracts/resources.html#getproductspercontract)
or in (List Usage per Contract)[]https://developer.akamai.com/api/luna/billing-usage/resources.html#getcontractmeasure]"""
>>>>>>> 8b510bf867b34af42f13f77d501d6a62e1bafee2
