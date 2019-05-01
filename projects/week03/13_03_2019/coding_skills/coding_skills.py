import json, sys

def parse(filename):
    try:
        with open(filename) as file:
            json_data = json.load(file)
    except FileNotFoundError:
        print('Error, file not found in current directory!')
        exit(-1)
    except ValueError:
        print("Error, provided file not in json format!")
        exit(-1)
    else:
        return json_data

def coding_skills(json_data):
    best_in_skill = {}
    people_lst = json_data["people"]
    for person in people_lst:
        person_names = person['first_name'] + ' ' + person['last_name']
        skills = person['skills']
        for skill in skills:
            if skill['name'] not in best_in_skill:
                best_in_skill.update({skill['name']: (person_names, skill['level'])})
            else:
                curr_level = best_in_skill[skill['name']][1]
                if curr_level < skill['level']:
                    best_in_skill[skill['name']] = (person_names, skill['level'])
    return {skill: name_and_level[0] for skill, name_and_level in best_in_skill.items()}

def print_best_in_every_skill(best_in_every_skill):
    for skill, name in best_in_every_skill.items():
        print(skill + ' - ' + name)

if __name__ == '__main__':
    jsondata = parse(sys.argv[1])
    best_in_every_skill = coding_skills(jsondata)
    print_best_in_every_skill(best_in_every_skill)