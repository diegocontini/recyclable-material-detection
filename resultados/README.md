# Resultados da execução no Colab

Estes arquivos foram extraídos do `triagem-resultados.zip` gerado no Colab em 24/11/2026. O arquivo completo (94 MB, com cópias do TrashNet e o modelo treinado) permanece fora do Git.

- `metrics.json`: acurácia, F1 macro, métricas por classe e matrizes de confusão.
- `predictions_local_test.csv`: previsão de cada uma das 39 fotos próprias. Os caminhos foram convertidos de `/content/runs/local/...` para caminhos relativos ao ZIP de entrada.
- `data_summary.json`: contagens de treino, validação e testes.
- `training.json`: configuração, versão do TensorFlow e histórico do treinamento.
- `confusion_*.png`: matrizes geradas na avaliação do Colab.

O ZIP de entrada das fotos tem SHA-256 `b4aa27dbbff7ed574edf62f4d2ae5bb734fdf6b2f837345e0cb2406e483ff29c`. O ZIP completo de resultados tem SHA-256 `b23c06b74feba1ec2f053b4c08e872e2de4474add1854bf5d4ea930b6e6abadb`.

O teste público teve 316 acertos em 359 imagens (88,0%) e o local, 21 em 39 (53,8%). As fotografias próprias não entraram no treino nem na seleção do modelo.
