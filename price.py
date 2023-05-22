from pathlib import Path


def shopping(shop_file):
    data_path = Path() / 'data' / shop_file
    shop_dict = {}  # 생성할 사전 객체

    with data_path.open(encoding='utf-8', mode='r') as f:
        for line in f:
            if line.find('원') != -1:
                name, price = line.split()
                shop_dict[name] = int(price[:-1])

    return shop_dict


def item_price(shop_file, item):
    item_dict = shopping(shop_file)

    if item_dict.get(item) is None:
        return "해당 아이템은 존재하지 않습니다."

    return f"해당 아이템 {item}는 {item_dict[item]}원 입니다."
