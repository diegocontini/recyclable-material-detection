# Avaliar transferência em imagens locais

A equipe treinará o classificador apenas com imagens do TrashNet e reservará todas as imagens próprias para um teste local separado. Essa escolha permite comparar o desempenho no fundo branco do dataset público com fotos reais da equipe; incluir imagens locais no treino responderia a uma pergunta diferente e reduziria o conjunto disponível para avaliar a transferência. O TrashNet será dividido de forma fixa e estratificada em treino (70%), validação (15%) e teste público (15%), com a lista de arquivos e a semente registradas para reprodução.
