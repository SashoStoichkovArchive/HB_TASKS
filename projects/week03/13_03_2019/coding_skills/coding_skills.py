import json, sys

def read_json():
    with open(str(sys.argv[1]), 'r') as f:
        data = json.load(f)

    return data

def skills_in_arr():
    skills = []

    for i in range(len(read_json()['people'])):
        for j in range(len(read_json()['people'][i]['skills'])):
            if read_json()['people'][i]['skills'][j]['name'] not in skills:
                skills.append(read_json()['people'][i]['skills'][j]['name'])

    return skills

def find_highest_level_for_every_skill():
    skill_levels = {}

    for i in range(len(skills_in_arr())):
        skill_levels.update({skills_in_arr()[i]: 0})

    for i in range(len(read_json()['people'])):
        for j in range(len(read_json()['people'][i]['skills'])):
            if read_json()['people'][i]['skills'][j]['name'] in skills_in_arr() and read_json()['people'][i]['skills'][j]['level'] > skill_levels[read_json()['people'][i]['skills'][j]['name']]:
                skill_levels.update({read_json()['people'][i]['skills'][j]['name']: read_json()['people'][i]['skills'][j]['level']})

    return skill_levels

def find_result():
    result = {}

    for i in range(len(skills_in_arr())):
        result.update({skills_in_arr()[i]: ''})

    for i in range(len(read_json()['people'])):
        for j in range(len(read_json()['people'][i]['skills'])):
            if read_json()['people'][i]['skills'][j]['name'] in skills_in_arr() and read_json()['people'][i]['skills'][j]['level'] == find_highest_level_for_every_skill():
                result.update({skills_in_arr()[i]: [read_json()['people'][j]['first_name'], read_json()['people'][i]['last_name']]})

    return result

if __name__ == "__main__":
    print(find_result())