# Calcula Resultado (Não Oficial) Serpro

A CEBRASPE publicou as notas das provas aplicadas, bem como as notas das provas objetivas, porém o resultado do concurso só deve sair em novembro. Isso porque ainda tem alguns passos que precisam ser seguidos, como análise dos pedidos de recurso de revisão de nota e algumas entrevistas. Como sou ansioso e não aguentaria esperar até novembro, eu fiz esse script em Python que calcula as notas finais do concurso.

Basicamente, o que fiz foi o seguinte:
Eu copiei somente as linhas de entrada com os resultados do Edital n°3 do concurso (https://cdn.cebraspe.org.br/concursos/SERPRO_23/arquivos/- ED_3_SERPRO_RES_FIN_OBJ_CONV_PRAT.PDF) e as coloquei no arquivo entrada_objetivas.txt.
Fiz o mesmo com o Edital n°5 do concurso (https://cdn.cebraspe.org.br/concursos/SERPRO_23/arquivos/ED_5_SERPRO_RES_PROV_PROVA_PRATICA.PDF) e salvei suas linhas no arquivo aplicadas.txt.
No arquivo calcula_resultado_serpro.py eu trabalhei com manipulações de string, pra receber essas entradas e produzir a saída no arquivo resultado_concurso.txt.

## Cálculo das Notas

Para calcular as notas eu usei o método descrito no item 10.1 do Edital n°1 do concurso (https://cdn.cebraspe.org.br/concursos/SERPRO_23/arquivos/ED_1_SERPRO_2023_ABERTURA.PDF):

NFC = N1 + (2 x N2) + N3

Sendo:
NFC = Nota Final do Concurso
N1 = Nota Final Obtida na Prova Objetiva P1;
N2 = Nota Final Obtida na Prova Objetiva P2
N3 = Nota Final Obtida na Prova de Conhecimentos Aplicados P3.

## Aviso

Esse resultado não é oficial, no momento de sua publicação o concurso ainda está em andamento.

## Licença

Este projeto está licenciado sob a Licença MIT.