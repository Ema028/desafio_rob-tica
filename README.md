# desafio_robótica
Todas as versões da parte 1 do desafio da inicial a final, com explicações da abordagem de cada etapa e o meu fluxo de pensamento até a ideia final.

Fluxograma da versão final feito na canva: https://www.canva.com/design/DAGlA0cr6u0/9jj2VaCKQ2rqt5wGnL2rmQ/view?utm_content=DAGlA0cr6u0&utm_campaign=designshare&utm_medium=link2&utm_source=uniquelinks&utlId=hd6a9b83ef1

### Materias de referência usados:
  
  playlist de aulas de Dave Fisher: 
   'https://www.youtube.com/playlist?list=PLmxhFaESqq3TIPYOUbdDNR87PL0qLe2MH'
 
  documentação ev3dev: 
    'https://ev3dev-lang.readthedocs.io/projects/python-ev3dev/en/stable/'
  
  repositório de demos no github:
  
    [robô EDUCATOR: 
      color.py: 'https://github.com/ev3dev/ev3dev-lang-python-demo/blob/stretch/robots/EDUCATOR/color.py',
      ultrassonic.py: 'https://github.com/ev3dev/ev3dev-lang-python-demo/blob/stretch/robots/EDUCATOR/ultrasonic.py']

## Versão 1 - 
A versão inicial é o mais simples possível, feita para se acostumar com a documentação e funcionalidades da biblioteca ev3dev.
O robô basicamente usa os sensores ultrassônicos para detectar se têm obstáculos na frente, à esquerda e/ou à direita e avança com velocidade máxima em direção ao obstáculo que estiver mais perto que nem um maluco. 
O robô cai pra fora da borda e não sobrevive, por isso o tempo de execução não foi registrado.

## Versão 2 -
Para resolver o problema de sobrevivência da primeira versão, agora o algoritimo usa o sensor de cor para identificar a borda vermelha e "foge" dela(da ré e vira). A velocidade para ir para frente foi diminuída pois o momento linear era muito grande com a velocidade máxima e às vezes o robô "virava" quando identificava a borda, o recuo era muito grande). Foi adicionada uma condição para o robô só virar quando o obstáculo estiver perto o suficiente para resolver o bug em que ele às vezes ficava preso entre 2 obstáculos muito perto um do outro.

Na sua primeira execução bem sucedida demorou 1 minuto e 40 segundos para derrubar todos os obstáculos.

Problemas a abordar: O Robô ainda dá muitos giros desnecessários, perdendo tempo e tem dificuldade de pegar obstáculos presos perto da borda. Às vezes ainda fica confuso com dois obstáculos perto. Perde muito tempo repetindo os mesmos caminhos vazios.
