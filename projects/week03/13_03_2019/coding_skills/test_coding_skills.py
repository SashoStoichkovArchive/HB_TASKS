import unittest
import coding_skills as cs

class TestCodingSkills(unittest.TestCase):
    def test_when_filepath_is_passed_then_json_is_returned(self):
        exp = {'people': [{'first_name': 'Ivo', 'last_name': 'Ivo', 'skills': [{'name': 'C++', 'level': 30},  {'name': 'PHP', 'level': 25}, {'name': 'Python', 'level': 80}, {'name': 'C#', 'level': 25}]}, 
               {'first_name': 'Rado', 'last_name': 'Rado', 'skills': [{'name': 'C++', 'level': 20}, {'name': 'PHP', 'level': 37}, {'name': 'Haskell', 'level': 70}, {'name': 'Java', 'level': 50}, {'name': 'C#', 'level': 10}, {'name': 'JavaScript', 'level': 60}]}, 
               {'first_name': 'Rosi', 'last_name': 'Rosi', 'skills': [{'name': 'JavaScript', 'level': 62}, {'name': 'Python', 'level': 66}, {'name': 'Ruby', 'level': 35}]}, 
               {'first_name': 'Pavli', 'last_name': 'Pavli', 'skills': [{'name': 'Python', 'level': 77}, {'name': 'CSS', 'level': 99}, {'name': 'JavaScript', 'level': 33}, {'name': 'C#', 'level': 70}]}, 
               {'first_name': 'Cherna', 'last_name': 'Ninja', 'skills': [{'name': 'C++', 'level': 99}, {'name': 'C', 'level': 99}]}]}
        
        self.assertEqual(cs.parse('data.json'), exp)

    def test_when_json_is_passed_then_return_dict_of_the_coding_skills(self):
        exp = {'C++': 'Cherna Ninja', 'PHP': 'Rado Rado', 'Python': 'Ivo Ivo', 
               'C#': 'Pavli Pavli', 'Haskell': 'Rado Rado', 'Java': 'Rado Rado', 
               'JavaScript': 'Rosi Rosi', 'Ruby': 'Rosi Rosi', 'CSS': 'Pavli Pavli', 'C': 'Cherna Ninja'}

        self.assertEqual(cs.coding_skills(cs.parse('data.json')), exp)

if __name__ == "__main__":
    unittest.main()