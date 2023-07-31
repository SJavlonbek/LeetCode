# def maxProfit(prices):
#     price_min=min(prices)
#     prices2=[]

#     for i in range(len(prices)):

#         if price_min==prices[i-1]:
#             prices2.extend(prices[i-1:])
#             price_max=max(prices2)
#             if price_max-price_min>0:
#                 return price_max-price_min
#             else:
#                 return 0

            # for j in range(len(prices2)-1):
            #     if price_min>prices2[j]:
            #         return 0
            #     else:
            #         price_max=max(prices2)
            #         return price_max-price_min



def maxProfit(prices):
    max_price = 0
    min_price = prices[0]

    for price in prices[1:]:
        min_price = min(min_price, price)
        max_price = max(max_price, price - min_price)

    return max_price

print(maxProfit([9,8,7,6,5,4,3,2,1]))
print(maxProfit([2,4,1]))