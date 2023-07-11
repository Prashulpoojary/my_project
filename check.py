from typing import List




def get_requirements(file_path:str)-> List[str]:

    hepen_e_dot = "-e ."
    req_list=[]
    with open(file_path) as obj_file:
        requirements = obj_file.readlines()
        for req in requirements:
            requirements = req.replace("\n","")
            print(requirements)
            req_list.append(requirements)
        # print("Requirement1 is",req_list)


        if hepen_e_dot in req_list:
            req_list.remove(hepen_e_dot)  
        # print("Requirement2 is",req_list)
    return req_list 


get_requirements("requirements.txt")