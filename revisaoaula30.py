"""
CONSTANTE = "Variáveis" que não vão mudar
Muitas condições no mesmo if (ruim)
    <- Contagem de complexidade (ruim)
"""
velocidade = 66 # velocidade atual do carro
local_carro = 100  # local em que o carro está na estrada

RADAR_1 = 60  # velocidade máxima do radar 1
LOCAL_1 = 100  # local onde o radar 1 está
RADAR_RANGE = 1  # A distância onde o radar pega


velocidade_passou_local1 = velocidade > RADAR_1
range1 = LOCAL_1 - RADAR_RANGE
range2 = LOCAL_1 + RADAR_RANGE
carro_passou_radar1 = local_carro >= (range1) and local_carro <= (range2)
carro_multado = velocidade_passou_local1 and carro_passou_radar1

if velocidade_passou_local1:
    print('Velocidade passou local 1')
    
if carro_passou_radar1:
    print('Carro passou no radar 1')

if carro_multado:
    print('CARRO MULTADO!!!')