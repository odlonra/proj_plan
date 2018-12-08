# -*- coding: utf-8 -*-
"""
Created on Sun Dec  2 16:21:14 2018

@author: Goerlitz
@date: 2.12.2018
"""
class Chain_Element:
    def __init__(
            self, name ='', todo='', istask = True, 
            ismilestone= False, check = False
        ):
        self.name = name
        self.todo = todo
        self.istask = istask
        self.ismilestone = ismilestone
        self.check = check
        return
    
    def rename(self,new_name):
        self.name = new_name
        return
    
    def check(self):
        self.check = True
        return
    
class Proj:
    def __init__(self, name=''):
        self.name = name
        self.tasklist = []
        self.current_task = 0
        return
    
    def rename(self,new_name):
        self.name = new_name
        return 
    
    def insert_element(self, element, pos=-1):
        self.tasklist.insert(pos, element)
        return
    
    def proj_task_soved(self, pos):
        task = self.tasklist[pos]
        
        task.check()
        
        if pos == self.current_task:
            self.current_task += 1
        return
def main():    
    startup = Proj ('Startup')
    start = Chain_Element('Start des Projekts', 'Um Fortzufahren muss man folgendes tun')
    startup.insert_element(start)
    
    print(startup.name)
    print(startup.tasklist[0].todo)
    return 





if __name__ == "__main__":
    main()    
        

    
