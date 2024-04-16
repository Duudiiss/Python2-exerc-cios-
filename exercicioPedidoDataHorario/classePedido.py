'''2A) Escreva a classe Pedido para representar um pedido em um restaurante a ser entregue em
domicílio. (Para facilitar considere que os pedidos só são feitos e entregues no mesmo dia)
Um pedido tem numero (int), cliente(string), valor, horário do pedido (objeto do tipo Horario),
data (data do pedido) e horário de entrega (objeto do tipo Horario).
Um pedido é criado sendo fornecidos: numero, nome do cliente, valor, o horário (objeto
Horario) em que o pedido foi feito e a data. Caso a data não seja fornecida o pedido é criado
com a data de hoje. Todo pedido, no momento da sua criação, tem horário de entrega
inicialmente igual ao horário (objeto Horario) correspondente a 00h00m00s (Obs: com esse
horário de entrega o pedido é considerado não entregue).
 __init__
Ao ser exibido, um pedido exibe uma msg com seu numero,cliente,data, horário e status.
Exemplo : Num:22-Cli:lala-Data:18/09/2023-Horario:14:30:00-Status:EmAndamento
 __str__ e __repr__
Um pedido é menor do que o outro se sua data é anterior a do outro. Caso tenham sido feitos
na mesma data, um pedido é menor do que outro se seu horário for menor do que o outro.
 __lt__
Um pedido pode retornar seu status, retornando 'EmAndamento', caso seu horário de entrega
corresponda ainda a 00h00m00s, ou 'Entregue', caso o horário de entrega inicial tenha sido
alterado.
 método obtemStatus
Um pedido pode registrar o horário em que foi entregue, recebendo para isso um objeto
Horario
 método registraHorarioDeEntrega
Um pedido pode calcular e retornar seu tempo de espera: se o pedido foi entregue, o tempo
de espera é a diferença do horário da entrega e o horário do pedido
 método calculaTempoDeEspera
Um pedido pode calcular e retornar seu valor: se o pedido foi feito no mês 9, o valor do pedido
retornado será o valor original – 10% (não altere o valor original). Do contrário é retornado o
próprio valor original.
 método obtemValor'''
from classehorario import Horario
class Pedido()