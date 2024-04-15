import random

styles = {
    'прическа': [
        'нет волос',
        'длинные в пучок',
        'длинные волнистые',
        'длинные прямые',
        'короткая волнистые',
        'короткая прямые',
        'короткая курчавые'
    ],
    'цвет волос': [
        'черный',
        'блонд',
        'каштановый',
        'пастельный розовый',
        'рыжий',
        'серебристо серый',
    ],
    'аксесуар': [
        'нет очков',
        'круглые очки',
        'солнцезащитные очки',
    ],
    'одежда': [
        'худи',
        'комбинезон',
        'футболка с круглым вырезом',
        'футболка с V-вырезом',
    ],
    'цвет одежды': [
        'черный',
        'синий',
        'серый',
        'зеленый',
        'оранжевый',
        'розовый',
        'красный',
        'белый'
    ],
}

styles_count = {
    'прическа': [
        7,
        0,
        1,
        23,
        1,
        11,
        7
    ],
    'цвет волос': [
        7,
        6,
        2,
        3,
        8,
        24,
    ],
    'аксесуар': [
        11,
        22,
        17,
    ],
    'одежда': [
        7,
        18,
        19,
        6,
    ],
    'цвет одежды': [
        4,
        5,
        6,
        8,
        6,
        8,
        7,
        6
    ],
}
new_array = {}
for key, subarray in styles.items():
    i = 0
    new_array[key] = {}
    for item in subarray:
        new_array[key][item] = styles_count[key][i]
        i += 1

i, index = 0, 0

totalPpl = 50

def check_array(features):
    totalFreq = 0
    for _, subarray in new_array.items():
        totalFreq += sum(subarray.values())

    return totalFreq

totalFreq = check_array(new_array)

assert totalPpl == totalFreq // len(new_array), 'Проверка не пройдена'

increases = 0

for key, subarray in new_array.items():
    for index, freq in subarray.items():
        new_array[key][index] = freq + 1
        increases += 1

increases += totalPpl
chances = {}

for key, subarray in new_array.items():
    chances[key] = {}
    for index, freq in subarray.items():
        chances[key][index] = freq/increases

# print(chances)


def generate_combinations(chances):
    keys, values = list(chances.keys()), list(chances.values())
    result = []

    def generate_helper(combination, index):
        if index == len(keys):
            probability = 1
            for i, key in enumerate(keys):
                probability *= values[i][combination[key]]
            result.append({'probability': probability, 'combination': {**combination}})
            return
        for value in values[index]:
            new_combination = {**combination, keys[index]: value}
            generate_helper(new_combination, index + 1)

    generate_helper({}, 0)
    return result

unique_styles = generate_combinations(chances)

probabilities = [item['probability'] for item in unique_styles]
# print(probabilities)

print(random.choices(unique_styles, weights=probabilities))
