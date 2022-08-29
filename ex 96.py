
def ls_list(list_tasks):
    if not list_tasks:
        print('nada a mostrar')
        return
    
    print(list_tasks)

def add_list(add_tasks,list_tasks):
    list_tasks.append(add_tasks)


def list_undo(list_tasks,redo_list):

    if not list_tasks: 
        print('nada a remover')
        return
    
    last_item = list_tasks.pop()
    redo_list.append(last_item)
    

def list_redo(list_tasks,redo_list):
    if not redo_list: 
        print('nada a refazer')
        return
     
    return_item = redo_list.pop()
    list_tasks.append(return_item)
  

if __name__ == "__main__":
    list_tasks = []
    redo_list = []

    while True:
    
        add_tasks = input(str('digite a tarefa: '))
        
        if add_tasks == 'ls':
            ls_list(list_tasks)
            continue
            
        elif add_tasks == 'undo':
            list_undo(list_tasks,redo_list)
            continue
        
        elif add_tasks == 'redo':
            list_redo(list_tasks,redo_list)
            continue
            
        elif add_tasks == 'exit': 
            print('saindo..')
            break
        add_list(add_tasks,list_tasks)



