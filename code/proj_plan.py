# -*- coding: utf-8 -*-
"""
Created on Sun Dec  2 16:21:14 2018

@author: Goerlitz
@date: 2.12.2018
"""
projlist = []
###############################################################################
########################define chain-element class#############################
class Chain_Element:
    def __init__(
            self, name ='', info='',  
            ismilestone= False, state = False
        ):
        self.name = name
        self.info = info
        self.ismilestone = ismilestone
        self.state = state
        return
    
    def rename(self,new_name):
        self.name = new_name
        return
    
    def check(self):
        self.state = True
        return
    
###############################################################################   
#########################define proj objekt####################################
class Proj:
    def __init__(self, name='', current_task_index = 0):
        self.name = name
        self.tasklist = []
        #Set a Start-Milestone
        self.tasklist.append(
            Chain_Element(
                'start: '+self.name,
                ismilestone = True,
                state = True
            )
        )
        self.current_task_index = current_task_index
        return
    
    def rename(self,new_name):
        self.name = new_name
        return 
    
    def insert_element(self, element, pos=-1):
        if pos == -1:
            self.tasklist.append(element)
            if self.tasklist[pos-1].state == True:
                self.current_task_index += 1
        else:
            self.tasklist.insert(pos, element)
            #If state of last task is True(solved) set itertater on new task
            if self.tasklist[pos-1].state ==True and self.tasklist[pos].state==False:
                self.current_task_index =pos
            elif self.tasklist[pos-1].state ==True and self.tasklist[pos].state==True:
                self.current_task_index += 1
        return
    
    def del_element(self,pos=-1):
        del self.tasklist[pos]
        return
    
    def task_solved(self, pos):
        task = self.tasklist[pos]
        print(self.name+': '+task.name+' solved')
        task.check()
        
        if pos == self.current_task_index and pos == len(self.tasklist)-1:
            self.current_task_index += 1
        return
###############################################################################
###########################Global Functions####################################        

def update_indecies(projlist):   
    for proj in projlist:
        proj.current_task_index = 0
        while proj.tasklist[proj.current_task_index].state != False:
            if proj.tasklist[len(proj.tasklist)-1].state == True:
                proj.current_task_index = len(proj.tasklist)-1
                break
            proj.current_task_index += 1
    return
 
def add_projekt(proj_name):
    projlist.append(Proj(proj_name))
    return

def del_projekt(num):
    del projlist[num]
    
    return

def add_task(proj,element_name, info='', ismilestone= False, state = False):
    element = Chain_Element (element_name, info, ismilestone, state)
    proj.insert_element(element)
    return

def del_task(proj,pos):
    proj.del_element(pos)
    return
###############################################################################
#################################Testing Aera##################################


def main():  
    add_projekt('Startup')
    add_task(projlist[0],'Erster Task')
    add_task(projlist[0],'Zweiter Task','')
    add_task(projlist[0],'Dritter Task')
    #startup = Proj('Startup')
    #start = Chain_Element('Erster Task', 'Um Fortzufahren muss man folgendes tun')
    #zweiter_task = Chain_Element('Zwei')
    #startup.insert_element(start) 
    #startup.insert_element(zweiter_task)
    #projlist.append(startup)
    #update_indecies(projlist)    
        

    print(projlist[0].name)
    print(projlist[0].tasklist[0].name)
    print(projlist[0].tasklist[1].name)
    print(projlist[0].current_task_index)    
    
    projlist[0].task_solved(1)
    #del_projekt(0)
    update_indecies(projlist)
    
    print(projlist[0].current_task_index)
    print('Anzahl der Elemente:',len(projlist[0].tasklist))


if __name__ == "__main__":
    main()