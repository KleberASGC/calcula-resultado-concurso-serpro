input_file_practice = open('entrada_aplicadas.txt')
all_data_practice = input_file_practice.read()
input_file_practice.close()

candidates_practice = all_data_practice.split('/')

result = list()
for candidate in candidates_practice:
    new_candidate = dict()
    aux = candidate.split()
    new_candidate['id'] = aux[0].replace(',', '')
    new_candidate['name'] = aux[1].replace(',', '') + ' ' + aux[2].replace(',', '')
    score_practice = aux[-1].replace(',', '')
    new_candidate['score_practice'] = float(score_practice)
    result.append(new_candidate)

input_file_objectives = open('entrada_objetivas.txt', 'r')
all_data_objetivas = input_file_objectives.read()
input_file_objectives.close()

candidates_objectives = all_data_objetivas.split('/')
scores = list()
final_result = list()
for candidate in candidates_objectives:
    aux = candidate.split()
    candidate_found = False
    for candidate_practice in result:
        aux[0] = aux[0].replace(',', '')
        if aux[0] == candidate_practice['id']:
            candidate_found = candidate_practice
            break
    
    if not candidate_found:
        continue

    score_specific = aux[-3].replace(',', '')
    score_basic = aux[-5].replace(',', '')
    
    candidate_found['score_specific'] = float(score_specific)
    candidate_found['score_basic'] = float(score_basic)
    candidate_found['final_score_objectives'] = candidate_found['score_basic'] + 2 * candidate_found['score_specific']
    final_score_contest = candidate_found['score_practice'] + candidate_found['final_score_objectives']
    candidate_found['final_score_contest'] = round(final_score_contest)

result = sorted(result, key=lambda x: x['final_score_contest'], reverse=True)

arquivo_saida = open('resultado_concurso.txt', 'w')
print('--------- RESULTADO (NÃO OFICIAL) DO CONCURSO SERPRO 2023 - ANALISTA – ESPECIALIZAÇÃO: TECNOLOGIA (Ampla Concorrência): --------- \n', file=arquivo_saida)
print('Modelo: ', file=arquivo_saida)
print('Número de Inscrição - Nome do Candidato - Nota Objetivas Básicas (N1) - Nota Objetivas Específicas (N2) - Total Notas Objetivas TNO (N1 + (2 * N2)) - Nota Aplicadas (N3) - Nota Final Concurso NFC (N1 + (2 x N2) + N3) \n', file=arquivo_saida)

counter = 1
previous_score = 1
previous_position = 1
for candidate in result:
    if(candidate['score_practice'] == 0):
        continue
    if(candidate['final_score_contest'] == previous_score):
        position = previous_position
    else:
        position = counter
        previous_position = position

    previous_score = candidate['final_score_contest']
    print(f"{str(position)}º - {candidate['id']} - {candidate['name']} - N1: {candidate['score_basic']} - N2: {candidate['score_specific']} - TNO: {candidate['final_score_objectives']} - N3: {candidate['score_practice']} - NFC: {candidate['final_score_contest']}", file=arquivo_saida)

    counter += 1
    
arquivo_saida.close()