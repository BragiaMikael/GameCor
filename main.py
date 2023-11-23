import random
ponto_seu = 0
ponto_pc = 0

while(True):
  cor_secreta = random.choice(['R', 'G', 'B']);
  palpite = input("Adivinhe a cor (R, G, B):").upper()
  if palpite not in ['R', 'G', 'B']:
    print('Resposta inválida. Escolha a cor (R, G, B)')
  elif palpite == cor_secreta:
    print('Você Acertouuu!!')
    ponto_seu = ponto_seu + 1
    print(f'Pontuação: Você {ponto_seu} x  PC {ponto_pc}')
  else:
    print('Você Errou!!')
    ponto_pc = ponto_pc + 1
    print(f'A cor era {cor_secreta}')
    print(f'Pontuação: Você {ponto_seu} x  PC {ponto_pc}')
  if ponto_seu == 5:
    print('Você Ganhou!')
