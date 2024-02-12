# ######################################################
# Author :  Aidan Dannhausen-Brun
# email : adannhau@purdue.edu
# ID : ee364a10
# Date : 02/10/2024
# ######################################################

import os  # List of module import statements
import sys  # Each one on a line
import re
import glob
import string
import math

# ######################################################
# No Module - Level Variables or Statements !
# ONLY FUNCTIONS BEYOND THIS POINT !
# ######################################################

# helper functions
def readProjects():
    project_circuit = {}
    with open("maps/projects.dat", "r") as file:
        next(file)      # skip header lines
        next(file)
        for line in file:
            circuit, id = line.split()
            if id in project_circuit:
                project_circuit[id].append(circuit)
            else:
                project_circuit[id] = [circuit]
    
    return project_circuit

def readStudents():
    name_id = dict()
    with open("maps/students.dat", 'r') as file:
        # skip over header lines
        next(file)
        next(file)
        for line in file:
            last, first, seperator, id = line.split()
            name_id[f"{last} {first}"] = id

    return name_id  

def readStudentsID():
    name_id = dict()
    with open("maps/students.dat", 'r') as file:
        # skip over header lines
        next(file)
        next(file)
        for line in file:
            last, first, seperator, id = line.split()
            name_id[id] = f"{last} {first}"

    return name_id  

def readComponent(componentSymbol):
    component_map = {'T':"maps/transistors.dat", 'I':"maps/inductors.dat", 'R':"maps/resistors.dat", 'C':"maps/capacitors.dat"}
    component_file = open(component_map[componentSymbol], 'r')
    # skip over headers
    next(component_file)
    next(component_file)
    next(component_file)

    component_dict = dict()

    for line in component_file.readlines():
        id, price = line.split()
        component_dict[id] = float(price[1:5])
    
    component_file.close()
    return component_dict


# To test your code, you can use the following variables:
test_projectID = "082D6241-40EE-432E-A635-65EA8AA374B6"
test_projectID2 = "90BE0D09-1438-414A-A38B-8309A49C02EF"
test_studentName = "Watson, Martin"
test_studentName2 = "Scott, Michael"
test_component = 'ZHR-274'
test_component2 = 'MAL-574'
test_circuitID = '39-3-07'


def getComponentCountByProject(projectID, componentSymbol):
    """Q1: Returns the number of components of the given type that the project has used."""
    result = 0

    # gets all the circuits in relation to a project
    circuit_list = readProjects()[projectID]

    # if circuit list is empty raise a value error
    if not circuit_list:
        raise ValueError("Project does not exist")

    # get components by type
    component_type = readComponent(componentSymbol)

    component_set = set()       # storing in a set gets rid of any duplicates
    for circuit in circuit_list:
        with open(f"circuits/circuit_{circuit}.dat", 'r') as circuit_file:
            for line in circuit_file:
                if line.strip() in component_type:
                    component_set.add(line.strip())
  
    result = len(component_set)
    return result


def getComponentCountByStudent(studentName, componentSymbol):
    """Q2: Returns the number of components of the given type that the student has used."""
    result = 0

    student_id = readStudents()[studentName]
    if not student_id:
        raise ValueError("student name does not exist.")

    component_type = set(readComponent(componentSymbol).keys())

    # search every circuit for the student id then append the components that match
    component_list = set()
    for circuit in os.scandir("circuits"):
        file = open(circuit, 'r')
        contents = file.read()
        # if the id is in the circuit get the components needed
        if student_id in contents:
            component_list.update(component_type.intersection(set(contents.split())))
        file.close()
    
    result += len(component_list)

    return result


def getParticipationByStudent(studentName):
    """Q3: Returns the set of project IDs in which the student has participated."""

    student_id = readStudents()[studentName]
    if not student_id:
        raise ValueError("student name does not exist.")
    
    circuits_participated = []
    for circuit in os.scandir("circuits"):
        file = open(circuit, 'r')
        contents = file.read()

        # if the id is in the circuit get the components needed
        if student_id in contents:
            circuits_participated.append(os.path.basename(circuit)[8:15])

        file.close()
    
    
    result = set()
    project_dict = readProjects()
    for circuit in circuits_participated:
        for projects in project_dict:
            if circuit in project_dict[projects]:
                result.add(projects)

    
    return result


def getParticipationByProject(projectID):
    """Q4: Returns the set of student names who have participated in the project."""
    circuit_list = readProjects()[projectID]
    if not circuit_list:
        raise ValueError("Project does not exist.")

    student_dict = readStudentsID() # [id] = name

    student_name_set = set()
    for circuit in circuit_list:
        file = open(f"circuits/circuit_{circuit}.dat")
        for line in file.read().split():
            if line in student_dict:
                student_name_set.add(student_dict[line])
        file.close()

    return student_name_set


def getCostOfProjects():
    """Q5: Returns a dictionary where the keys are project IDs and the values are the total cost of the project."""

    transistor_prices = readComponent('T')
    inductor_prices = readComponent('I')
    resistor_prices = readComponent('R')
    capacitor_prices = readComponent('C')

    project_dict = readProjects()
    project_cost = dict()
    for project in project_dict:
        project_cost[project] = 0

    
    for p_name, c_list in project_dict.items():
        for circuit in c_list:
            circ_file = open(f"circuits/circuit_{circuit}.dat")
            for component in circ_file.read().split():
                if component in transistor_prices:
                    project_cost[p_name] += transistor_prices[component]
                elif component in capacitor_prices:
                    project_cost[p_name] += capacitor_prices[component]
                elif component in inductor_prices:
                    project_cost[p_name] += inductor_prices[component]
                elif component in resistor_prices:
                    project_cost[p_name] += resistor_prices[component]

    for project in project_cost:
        project_cost[project] = round(project_cost[project], 2)
    sample_project_cost = 8.444218515250482
    # Example of rounding a float to 2 decimal places
    final_dict = {test_projectID: round(sample_project_cost, 2)}
    return project_cost


def getProjectByComponent(componentIDs: set):
    """Q6: Returns the set of project IDs that have used any of the given components."""
    

    circuit_list = []

    for circuit in os.scandir("circuits"):
        file = open(circuit, 'r')
        contents = file.read()
        
        if len(componentIDs.intersection(set(contents.split()))) != 0:  # if their is any intersection
            circuit_list.append(os.path.basename(circuit)[8:15])
        file.close()

    result = set()
    projects_dict = readProjects()
    for proj, circ in projects_dict.items():
        for circuit in circuit_list:
            if circuit in circ:
                result.add(proj)

    
    return result


def getCommonByProject(projectID1, projectID2):
    """Q7: Returns the sorted list of components that are common to both projects."""
    result = 0

    # gets all the circuits in relation to a project
    circuit_list1 = readProjects()[projectID1]
    circuit_list2 = readProjects()[projectID2]
    # if circuit list is empty raise a value error
    if not circuit_list1:
        raise ValueError("First project does not exist")
    if not circuit_list2:
        raise ValueError("Second project does not exist")

    components_set1 = set()
    components_set2 = set()

    for circuit in circuit_list1:
        with open(f"circuits/circuit_{circuit}.dat", 'r') as circuit_file:
            components_section = False
            for line in circuit_file:
                if line.strip() == "Components:":
                    components_section = True
                    next(circuit_file)
                elif components_section:
                    component_id = line.strip()
                    components_set1.add(component_id)

    for circuit in circuit_list2:
        with open(f"circuits/circuit_{circuit}.dat", 'r') as circuit_file:
            components_section = False
            for line in circuit_file:
                if line.strip() == "Components:":
                    components_section = True
                    next(circuit_file)
                elif components_section:
                    component_id = line.strip()
                    components_set2.add(component_id)

    return sorted(components_set1.intersection(components_set2))


def getCircuitByStudent(studentNames):
    """Q8: Returns the set of circuit IDs that the students have used."""

    student_dict = readStudents()
    student_id = []
    for name in studentNames:
        student_id.append(student_dict[name])

    circuits_participated = set()
    for circuit in os.scandir("circuits"):
        file = open(circuit, 'r')
        contents = file.read()

        # if the id is in the circuit get the components needed
        for id in student_id:    
            if id in contents:
                circuits_participated.add(os.path.basename(circuit)[8:15])
            

        file.close()

    return circuits_participated


def getCircuitByComponent(componentIDs):
    """Q9: Returns the set of circuit IDs that have used any of the given components."""

    circuits_with_components = set()
    for circuit in os.scandir("circuits"):
        file = open(circuit, 'r')
        contents = set(file.read().split())

        if len(componentIDs.intersection(contents)) != 0:
            circuits_with_components.add(os.path.basename(circuit)[8:15])

            

        file.close()

    return circuits_with_components


# ######################################################
# This block is optional and can be used for testing .
# We will NOT look into its content .
# ######################################################

if __name__ == "__main__":
    # Write anything here to test your code .
    # Some sample tests are provided with all or part of the expected output
    # readProjects()
    # print(getComponentCountByProject(test_projectID, "C"))
    # 63

    # print(getComponentCountByProject(test_projectID2, "T"))
    # 83
    # print("")
    # print(getComponentCountByStudent(test_studentName, "R"))
    # 40
    # print("")
    # print(getParticipationByStudent(test_studentName))
    # {'96CC6F98-B44B-4FEB-A06B-390432C1F6EA', '90BE0D09-1438-414A-A38B-8309A49C02EF', ...}
    # print("")
    # print(getParticipationByProject(test_projectID))
    # {'James, Randy', 'Collins, Anthony', 'Long, Joshua', ...}
    # print("")
    # print(getCostOfProjects())
    # {'56B13184-D087-48DB-9CBA-84B40FE17CC5': 355.36, ...}
    # print("")
    # print(getProjectByComponent({test_component}))
    # {'6CCCA5F3-3008-46FF-A779-2D2F872DAF82', '56B13184-D087-48DB-9CBA-84B40FE17CC5',...}
    # print("")
    # print(getCommonByProject(test_projectID, test_projectID2))
    # ['ART-641', 'AVL-897', 'BKC-326', 'BLT-317', 'BOT-567', ...]

    print(getCircuitByStudent({test_studentName}))
    # {'67-4-02', '78-7-77', '69-1-62', '84-2-05', ...}

    print(getCircuitByComponent({test_component}))
    # {'10-2-91', '29-9-59', '75-9-18', '77-3-73', '49-6-69', '39-3-07'}

    print(getCircuitByComponent({test_component, test_component2}))
    # {'81-7-77', '49-6-69', '93-1-30', '77-3-73', '29-9-59', ...}