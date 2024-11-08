def calcular_media(notas):
  somar = 0
  quantidade = 0
  for nota in notas:
    somar += nota
    quantidade += 1
    
  media = somar / quantidade
  return media

def classificar_aluno(notas):
  media = calcular_media(notas)
  if media >= 7:
    return 'Aprovado'
  elif media >= 5:
    return 'Recuperação'
  else:
    return 'Reprovado'
