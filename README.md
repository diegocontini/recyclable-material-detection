# Triagem de resíduos recicláveis

Experimento de classificação de **papel (incluindo papelão), plástico, vidro e metal**. O modelo usa transferência de aprendizado com MobileNetV2: é treinado apenas com um recorte do [TrashNet](https://github.com/garythung/trashnet) e avaliado tanto no teste público quanto em **39 fotografias próprias da equipe**. Itens de material misto, resíduos orgânicos e rejeitos ficam fora das quatro classes.

## Experimento apresentado

A execução de referência foi feita no **Google Colab** com [notebooks/colab.ipynb](notebooks/colab.ipynb). O notebook contém todas as rotinas de preparação, treinamento e avaliação diretamente nas células; não depende de arquivos Python deste repositório.

| Teste | Acertos | Acurácia | F1 macro |
|---|---:|---:|---:|
| TrashNet público | 316/359 | 88,0% | 0,857 |
| Fotos próprias | 21/39 | 53,8% | 0,531 |

O recorte do TrashNet começa com 2.390 imagens das quatro classes; seis imagens idênticas com rótulos conflitantes foram excluídas nesta execução. As 2.384 restantes foram divididas em treino (1.666), validação (359) e teste público (359), com semente 42. O modelo foi escolhido pela validação pública. **Nenhuma foto própria entrou no treino ou na seleção do modelo.** As métricas, previsões e matrizes de confusão estão em [resultados/](resultados/).

## Reproduzir no Colab

1. No Colab, use **Arquivo → Fazer upload de notebook** e selecione [notebooks/colab.ipynb](notebooks/colab.ipynb).
2. Na célula **Fotos próprias e divisão**, mude `USAR_FOTOS_LOCAIS = False` para `True`.
3. Execute as células em ordem, de preferência em um ambiente novo. Quando o notebook pedir, envie [data-local/fotos-equipe-colab.zip](data-local/fotos-equipe-colab.zip). O ZIP contém exatamente um `labels.csv` com as colunas `path,label`, além das 39 fotos: 9 de papel e 10 de cada outro material.
4. Ao final, baixe `triagem-resultados.zip`. A GPU acelera o treino, mas não é obrigatória.

O notebook instala as dependências, baixa o TrashNet original e carrega pesos pré-treinados no ImageNet. O ZIP completo de saída contém também cópias dos dados e o modelo treinado; por seu tamanho, ele não faz parte do repositório. Os resultados pequenos e necessários para conferir a avaliação estão versionados em [resultados/](resultados/).

## Arquivos e referências

- [data-local/](data-local/): ZIP das fotografias próprias e exemplo do formato de anotação.
- [notebooks/colab.ipynb](notebooks/colab.ipynb): fluxo integral usado no Colab.
- [resultados/](resultados/): resumo verificável da execução no Colab.

O dataset TrashNet é distribuído pelos autores sob [licença MIT](https://github.com/garythung/trashnet/blob/master/LICENSE). O pacote de exemplos públicos do RealWaste, usado apenas em testes técnicos anteriores, pode ser regenerado por `scripts/make_realwaste_smoke.py` e **não entra** nos resultados apresentados.
