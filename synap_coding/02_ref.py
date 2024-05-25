import re

# 숫자를 한글로 변환하기 위한 딕셔너리
num_to_korean = {
    1: '일', 2: '이', 3: '삼', 4: '사', 5: '오', 6: '육', 7: '칠', 8: '팔', 9: '구', 10: '십',
    100: '백', 1000: '천', 10000: '만', 100000000: '억', 1000000000000: '조'
}

# 숫자를 한글로 변환하는 함수
def convert_to_korean(num):
    if num == 0:
        return ''
    elif num < 10:
        return num_to_korean[num]
    elif num < 100:
        div, mod = divmod(num, 10)
        return (num_to_korean[div] + num_to_korean[10] + convert_to_korean(mod)).replace('일십', '십')
    elif num < 1000:
        div, mod = divmod(num, 100)
        return (num_to_korean[div] + num_to_korean[100] + convert_to_korean(mod)).replace('일백', '백')
    elif num < 10000:
        div, mod = divmod(num, 1000)
        return (num_to_korean[div] + num_to_korean[1000] + convert_to_korean(mod)).replace('일천', '천')
    else:
        for unit in [1000000000000, 100000000, 10000, 1]:
            if num >= unit:
                div, mod = divmod(num, unit)
                if unit == 1:
                    return convert_to_korean(div) + convert_to_korean(unit) + convert_to_korean(mod)
                return (convert_to_korean(div) + num_to_korean[unit] + ' ' + convert_to_korean(mod)).strip()

# 금액을 한글로 읽는 함수
def read_korean_amount(amount_str):
    amount_str = amount_str.replace('원', '').replace(',', '')
    amount = int(amount_str)
    korean_amount = convert_to_korean(amount)
    korean_amount = korean_amount.replace('일조', '조').replace('일억', '억').replace('일만', '만').replace('일천', '천').replace('일백', '백').replace('일십', '십')
    return korean_amount + '원'

# 한글 글자 수를 세는 함수
def count_korean_chars(korean_str):
    words = korean_str.split()
    num_words = len(words)
    num_chars = sum(len(word) for word in words)
    return num_words * num_chars

def main():
    amounts = [
        "1원", "4원", "8원", "9원", "10원", "17원", "79원", "80원", "95원", "205원", "809원",
        "851원", "878원", "2,000원", "2,800원", "7,008원", "8,174원", "9,718원", "45,150원",
        "50,000원", "69,700원", "382,915원", "431,409원", "921,500원", "5,003,052원",
        "5,039,670원", "6,835,623원", "8,000,000원", "10,000,003원", "35,100,000원",
        "39,997,777원", "90,021,015원", "93,275,690원", "403,197,000원", "459,176,461원",
        "730,080,000원", "999,999,000원", "6,887,000,000원", "7,000,020,000원",
        "7,700,000,500원", "7,848,761,270원", "38,048,620,625원", "57,000,000,000원",
        "74,778,562,249원", "97,417,165,814원", "101,000,120,000원", "343,000,000,000원",
        "458,807,907,862원", "872,818,015,000원", "6,278,000,015,000원",
        "7,991,000,844,000원", "9,000,400,000,675원", "22,018,914,675,100원",
        "78,196,000,000,000원", "85,000,904,224,858원", "95,000,000,404,918원"
    ]

    total_score = 0
    for amount in amounts:
        korean_amount = read_korean_amount(amount)
        score = count_korean_chars(korean_amount)
        total_score += score
        print(f"{amount} -> {korean_amount} -> Score: {score}")

    print(f"Total Score: {total_score}")

if __name__ == "__main__":
    main()
