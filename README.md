# desafio_robótica
Todas as versões da parte 1 do desafio da inicial a final, com explicações da abordagem de cada etapa e o meu fluxo de pensamento até a ideia final. Todas feitas e testadas no gears simulator.

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
Para resolver o problema de sobrevivência da primeira versão, agora o algoritimo usa o sensor de cor para identificar a borda vermelha e "foge" dela(da ré e vira). A velocidade para ir para frente foi diminuída pois o momento linear era muito grande com a velocidade máxima e eu queria tentar diminuir o recuo brusco quando identificava a borda, o. Foi adicionada uma condição para o robô só virar quando o obstáculo estiver perto o suficiente, diminuindo a frequência em que ele fica preso entre dois obstáculos sem saber para qual ir.

Na sua primeira execução bem sucedida demorou 1 minuto e 40 segundos para derrubar todos os obstáculos. Na segunda: 1 minuto e 13 segundos.

Problemas a abordar: O Robô ainda dá muitos giros desnecessários, perdendo tempo. Às vezes ainda fica confuso com dois obstáculos perto. Perde muito tempo repetindo os mesmos caminhos vazios.

## Versão 3 -
A primeira alteração nessa versão é o recuo quando chega na borda, concertando dois problemas ocasionais: o robô não recuava o suficiente e ficava batendo na borda e relacionado com esse problema ele ficava preso na borda ocasionalmente, dando ré para fora.
Essa alteração eu fiz adicionando uma condição para ele ver se saiu da borda depois de recuar e recuando mais se preciso, além disso a verificação de borda ficou bem mais segura e fluída desligando o motor entre mudanças de direção bruscas.
A segunda mudança foi começar a registrar o tempo usando a lib time e adicionar uma condição para o robô virar para a direita caso tenha se passado 6 segundos sem encontrar bordas ou obstáculos. O número 6 foi usado após alguns testes pois foi o que teve a melhor resposta no sentido: Ainda alcança obstáculos longe sem virar antes de encontrá-los, mas não fica preso em uma área limpa já. Antes disso, tentei adicionar certa aleatoriedade no movimento inicialmente, achando que isso diversificaria as rotas, mas eu senti que isso piorou a execução, por isso a tentativa foi abortada. 

Na primeira execução: 33 segundos. Na segunda: 42 segundos.

Essa versão tem movimentos mais fluídos que a 2 e perde menos tempo em caminhos vazios, mas mantém o problema da 2 versão de ficar confuso quando está entre dois obstáculos muito próximos.

## Falha - 
Essa tecnicamente seria a versão 4, não é necessariamente uma falha, mas foi nomeada assim pois as ideias dela não foram aproveitadas na próxima versão(no caso a final). A primeira mudança que eu tentei fazer nela foi adicionar uma função para desascelerar o robô linearmente quando estivesse carregando um obstáculo, o objetivo era tentar deixar a animação do robô batendo na borda mais fluída já que o recuo era meio feio, mas a mudança não teve uma melhora estética que justificasse os problemas que trouxe e o tempo a mais que o algoritimo gastaria, por isso foi abortada. A segunda mudança foi que eu adicionei uma função para o robô ver se ficou preso entre objetos muito próximos usando os sensores ultrassônicos e caso esteja preso ele consegue escapar, essa alteração resolveu o maior problema das versões anteriores, mas eu mudei um pouco a abordagem na versão 4 oficial então não foi utilizada. Ela também introduziu uma tentativa de mapear a borda usando o giroscópio, ele basicamente sempre que encontra uma borda adiciona em uma lista e quando o robô anda se identificar que o ângulo do giroscópio está próximo de uma borda salva ele salva como borda e recua. Eu tive a ideia após aprender um pouco mais sobre o giroscópio achando que ficaria mais seguro, mas teve vários problemas incluindo: dificuldade de pegar objetos presos na borda, robô preso girando na borda, ou girando demais dando ré e caindo para fora, enfim o programa ficou bem mais instável/difícil de controlar e por isso decidi dar um passo para trás e voltar para a versão anterior e tentar pensar como otimizar ela. Outra peculiaridade é que essa versão em algum momento parecia ter entrado em duas estruturas if diferentes ao mesmo tempo, o que eu não fazia ideia de que era possível, deixando o robô bem maluco, o que eu consertei usando continue dentro do loop depois de ações importantes para o robô sempre dar prioridade a verificar se está na borda ou preso antes de continuar o movimento normal, o que resolveu.
