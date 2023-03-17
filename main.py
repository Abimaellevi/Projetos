import os 



def listar(tarefas):
  print()
  if not tarefas:
    print('Nenhuma tarefa para listar')
    return
  
  print('Tarefas:')
  for tarefa in tarefas: 
    print(f'\t{tarefa}')
  
def desfazer(tarefas, tarefas_desfazer):
  print() 
  if not tarefas:
    print('Nenhuma tarefa para desfazer')
    return

  tarefa = tarefas.pop()
  tarefas_refazer.append(tarefa) 

def refazer(tarefas, tarefas_refazer): 
  print()
  if not tarefas_refazer: 
    print('Nenhuma tarefa para refazer')
    return 

  tarefa = tarefas.pop()
  print(f'{tarefa=} adicionada na lista de tarefas.') 
  tarefas.append(tarefa)  
  print() 

def adicionar(tarefa, tarefas): 
  print() 
  if not tarefa.strip():
    print('Você não digitou uma tarefa')
    return 
  tarefas.append(tarefa) 
  (f'{tarefa=} adicionada na lista de tarefas.') 
  

tarefas = []
tarefas_refazer = []
while True:
  print('Comandos: adicionar, listar, desfazer e refazer')
  tarefa = input("Digite uma tarefa ou comando: ") 

  if tarefa == 'listar':
    listar(tarefas)
    print() 
    continue
  elif tarefa == 'desfazer':
    desfazer(tarefas, tarefas_refazer)
    listar(tarefas)
    print() 
    continue
  elif tarefa == 'refazer':
    refazer(tarefas, tarefas_refazer)
    listar(tarefas)
    print() 
  
    continue 
    
  elif tarefa == 'clear':
    os.system('clear')
  
    continue 
      
  else:
    adicionar(tarefa, tarefas)
    listar(tarefas)
    print() 
    continue