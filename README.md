# Mission Control AI - Nebula Watch

## Integrantes

* Kaique Da Silva Assis — RM572718
* Andre Debiazzi — RM569062
* Vinicius Cristal de Oliveira — RM572048

---

## Descrição do Projeto

O projeto Mission Control AI foi desenvolvido para simular o monitoramento inteligente de uma missão espacial experimental.

O sistema analisa diferentes ciclos da missão utilizando dados simulados de:

* temperatura;
* comunicação;
* bateria;
* oxigênio;
* estabilidade operacional.

A partir desses dados, o programa realiza análises automáticas para identificar riscos operacionais, gerar alertas, calcular o nível de risco da missão e apresentar recomendações de segurança.

---

## Objetivo

O objetivo do projeto é desenvolver um sistema em Python capaz de:

* armazenar dados simulados da missão;
* analisar os ciclos automaticamente;
* gerar alertas;
* calcular riscos;
* identificar tendências da missão;
* identificar a área mais afetada;
* gerar um relatório final completo no terminal.

---

## Tecnologias Utilizadas

* Python 3
* VS Code
* GitHub

---

## Estrutura dos Dados

O sistema utiliza uma matriz chamada `dados_missao`.

Cada linha representa um ciclo da missão.

Cada coluna representa uma informação monitorada:

```python
[temperatura, comunicacao, bateria, oxigenio, estabilidade]
```

Exemplo:

```python
[24, 92, 88, 96, 90]
```

---

## Funcionalidades do Sistema

O sistema possui as seguintes funcionalidades:

* análise automática da temperatura;
* análise da comunicação;
* análise da bateria;
* análise do oxigênio;
* análise da estabilidade operacional;
* cálculo de risco por ciclo;
* classificação da missão;
* geração automática de recomendações;
* análise de tendência da missão;
* identificação da área mais afetada;
* geração de relatório final.

---

## Classificações de Risco

O sistema utiliza três classificações:

* NORMAL
* ATENÇÃO
* CRÍTICO

Cada classificação gera uma pontuação:

* NORMAL = 0 pontos
* ATENÇÃO = 1 ponto
* CRÍTICO = 2 pontos

---

## Como Executar o Projeto

1. Abrir o projeto no VS Code.
2. Executar o arquivo Python.
3. O sistema exibirá automaticamente:

   * análise dos ciclos;
   * classificação da missão;
   * relatório final.

---

## Exemplo de Execução

O sistema apresenta:

* ciclos da missão;
* alertas automáticos;
* pontuação de risco;
* tendência da missão;
* área mais afetada;
* relatório final completo.

---

## Conclusão

O projeto Mission Control AI permite simular o monitoramento inteligente de uma missão espacial experimental utilizando lógica computacional, estruturas de repetição, condicionais, listas, matrizes e funções em Python.

O sistema auxilia a identificação de riscos operacionais e apoia a tomada de decisão durante a missão.
