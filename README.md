# desafio_robótica
Todas as versões da parte 1 do desafio da inicial a final, com explicações da abordagem de cada etapa

Fluxograma da versão final feito na canva: https://www.canva.com/design/DAGlA0cr6u0/9jj2VaCKQ2rqt5wGnL2rmQ/view?utm_content=DAGlA0cr6u0&utm_campaign=designshare&utm_medium=link2&utm_source=uniquelinks&utlId=hd6a9b83ef1

Materias de referência usados:
  playlist de aulas de Dave Fisher: https://www.youtube.com/playlist?list=PLmxhFaESqq3TIPYOUbdDNR87PL0qLe2MH
  documentação ev3dev: https://ev3dev-lang.readthedocs.io/projects/python-ev3dev/en/stable/
  repositório de demos no github: [ robô EDUCATOR: color.py: https://github.com/ev3dev/ev3dev-lang-python-demo/blob/stretch/robots/EDUCATOR/color.py , ultrassonic.py: https://github.com/ev3dev/ev3dev-lang-python-demo/blob/stretch/robots/EDUCATOR/ultrasonic.py ]

Versão 1 - 
A versão inicial é o mais simples possível, feita para se acostumar com a documentação e funcionalidades da biblioteca ev3dev.
O robô basicamente usa os sensores ultrassônicos para detectar se têm obstáculos na frente, à esquerda e/ou à direita e avança com velocidade máxima em direção ao obstáculo que estiver mais perto que nem um maluco. 
O robô cai pra fora da borda e não sobrevive, por isso o tempo de execução não foi registrado.
