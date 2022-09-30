T = int(input())


for t in range(1, 1+T):
    N = int(input())
    price_list = list(map(int, input().split()))
    all_marg = 0
    sell_price = price_list[N-1]
    for price in price_list[::-1]:   
        if price > sell_price:
            sell_price = price
        all_marg += sell_price - price


    print('#{} {}'.format(t, all_marg))