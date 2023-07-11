from setuptools import find_packages,setup
from typing import List


# hepen_e_dot = "-e ."
# def get_requirements(file_path:str)-> List[str]:

#     requirements=[]
#     with open(file_path) as obj_file:
#         requirements = obj_file.readlines()
#         for req in requirements:
#             requirements = [req.replace("\n","")]

#         if hepen_e_dot in requirements:
#             requirements.remove(hepen_e_dot)  
#     # print(requirements)
#     return requirements 

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

    
setup(
    name="mlproject",
    version="0.0.1",
    author="Prashul",
    author_email="poojarypsl@gmail.com",
    packages=find_packages(),
    install_requirements=get_requirements("requirements.txt")

)

# get_requirements("requirements.txt")