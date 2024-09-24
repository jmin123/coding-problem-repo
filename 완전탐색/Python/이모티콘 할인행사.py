from itertools import product

def solution(users, emoticons):
    discount_rates = [10, 20, 30, 40]
    total_subscribers = 0
    total_sales = 0
    
    all_possible_combinations = product(discount_rates, repeat=len(emoticons))
    
    # 가능한 조합으로
    for discounts in all_possible_combinations:
        subscribers = 0
        sales = 0
        # 유저가 설정한 한도내에서
        for user_discount, user_budgets in users:
            total = 0
            # 이모티콘 가격으로 가능한 할인 조합에서
            for emoticon_price, discount in zip(emoticons, discounts):
                print(emoticon_price, discount)
                # 유저가 설정한 할인율을 충족한다면
                if discount >= user_discount:
                    total += emoticon_price * (100 - discount) // 100
            # 만약 한도를 충족하거나 넘어가면
            if total >= user_budgets:
                # 구독자 추가
                subscribers += 1
            else:
                sales += total
        # 1순위 : 구독자 수가 많은 경우
        # 2순위 : 구독자 수가 같으면 매출이 더 많은 경우
        if subscribers > total_subscribers or (subscribers == total_subscribers and sales > total_sales):
            # print(subscribers, sales)
            total_subscribers = subscribers
            total_sales = sales

    return [total_subscribers, total_sales]

print(solution([[40, 10000], [25, 10000]], [7000, 9000]))