# Nome da missão: Nebula Watch
# Nome da equipe: Equipe Apollo
# Integrantes:
# Kaique Da Silva Assis — RM-572718
# Andre Debiazzi — RM-569062
# Vinicius Cristal de Oliveira — RM-572048
# Link do vídeo pitch no YouTube:
# https://www.youtube.com/watch?v=BzuYokZEfyU
# Link do repostório do Github:
# https://github.com/KaiqueKai/mission-control-ai-nebula-watch

# ============================================================
# MISSION CONTROL AI
# Sistema Inteligente de Monitoramento de Missão Espacial
# ============================================================


# ============================================================
# DADOS PRINCIPAIS DA MISSÃO
# ============================================================

nome_missao = "Nebula Watch"
nome_equipe = "Equipe Apollo"

areas_monitoradas = [
    "Temperatura interna",
    "Comunicação com a base",
    "Sistema de energia",
    "Suporte de oxigênio",
    "Estabilidade operacional"
]

dados_missao = [
    [24, 92, 88, 96, 90],
    [27, 80, 72, 94, 85],
    [31, 65, 58, 91, 70],
    [36, 42, 38, 87, 55],
    [39, 28, 19, 78, 35],
    [34, 55, 32, 82, 50]
]


# ============================================================
# FUNÇÕES DE ANÁLISE
# ============================================================

def analisar_temperatura(valor):

    if valor < 18:
        return "ATENÇÃO", 1, "Temperatura abaixo do ideal"

    elif valor <= 30:
        return "NORMAL", 0, "Temperatura estável"

    elif valor <= 35:
        return "ATENÇÃO", 1, "Temperatura elevada"

    else:
        return "CRÍTICO", 2, "Risco de superaquecimento"


def analisar_comunicacao(valor):

    if valor < 30:
        return "CRÍTICO", 2, "Comunicação com a base em nível crítico"

    elif valor <= 59:
        return "ATENÇÃO", 1, "Comunicação instável"

    else:
        return "NORMAL", 0, "Comunicação estável"


def analisar_bateria(valor):

    if valor < 20:
        return "CRÍTICO", 2, "Bateria em nível crítico"

    elif valor <= 49:
        return "ATENÇÃO", 1, "Bateria abaixo do recomendado"

    else:
        return "NORMAL", 0, "Energia estável"


def analisar_oxigenio(valor):

    if valor < 80:
        return "CRÍTICO", 2, "Oxigênio em nível crítico"

    elif valor <= 89:
        return "ATENÇÃO", 1, "Oxigênio abaixo do ideal"

    else:
        return "NORMAL", 0, "Oxigênio adequado"


def analisar_estabilidade(valor):

    if valor < 40:
        return "CRÍTICO", 2, "Estabilidade operacional crítica"

    elif valor <= 69:
        return "ATENÇÃO", 1, "Estabilidade operacional reduzida"

    else:
        return "NORMAL", 0, "Estabilidade operacional adequada"


# ============================================================
# FUNÇÃO DE CLASSIFICAÇÃO DO CICLO
# ============================================================

def classificar_ciclo(pontos):

    if pontos <= 2:
        return "MISSÃO ESTÁVEL"

    elif pontos <= 5:
        return "MISSÃO EM ATENÇÃO"

    else:
        return "MISSÃO CRÍTICA"


# ============================================================
# FUNÇÃO DE RECOMENDAÇÃO
# ============================================================

def gerar_recomendacao(classificacao):

    if classificacao == "MISSÃO ESTÁVEL":
        return "Manter operação normal e continuar monitoramento."

    elif classificacao == "MISSÃO EM ATENÇÃO":
        return "Monitorar sistemas em atenção e preparar plano de contingência."

    else:
        return "Ativar modo de segurança e priorizar suporte à vida, energia e comunicação."


# ============================================================
# FUNÇÃO DE TENDÊNCIA DA MISSÃO
# ============================================================

def analisar_tendencia(primeiro_risco, ultimo_risco):

    if ultimo_risco > primeiro_risco:
        return "A missão apresentou tendência de piora."

    elif ultimo_risco < primeiro_risco:
        return "A missão apresentou tendência de melhora."

    else:
        return "A missão permaneceu estável em relação ao início."


# ============================================================
# FUNÇÃO PARA IDENTIFICAR ÁREA MAIS AFETADA
# ============================================================

def identificar_area_mais_afetada(pontos_areas):

    maior_pontuacao = max(pontos_areas)
    indice = pontos_areas.index(maior_pontuacao)

    return areas_monitoradas[indice]


# ============================================================
# VARIÁVEIS DE CONTROLE
# ============================================================

riscos_ciclos = []

pontuacao_areas = [0, 0, 0, 0, 0]

total_temperatura = 0
total_comunicacao = 0
total_bateria = 0
total_oxigenio = 0
total_estabilidade = 0

quantidade_ciclos_criticos = 0


# ============================================================
# CABEÇALHO DO SISTEMA
# ============================================================

print("=" * 60)
print("MISSION CONTROL AI")
print("=" * 60)

print(f"Missão: {nome_missao}")
print(f"Equipe: {nome_equipe}")
print(f"Quantidade de ciclos analisados: {len(dados_missao)}")

print("=" * 60)


# ============================================================
# ANÁLISE DOS CICLOS
# ============================================================

for indice, ciclo in enumerate(dados_missao):

    print(f"\nCICLO {indice + 1}")
    print("-" * 60)

    temperatura = ciclo[0]
    comunicacao = ciclo[1]
    bateria = ciclo[2]
    oxigenio = ciclo[3]
    estabilidade = ciclo[4]

    total_temperatura += temperatura
    total_comunicacao += comunicacao
    total_bateria += bateria
    total_oxigenio += oxigenio
    total_estabilidade += estabilidade

    status_temp, pontos_temp, mensagem_temp = analisar_temperatura(temperatura)
    status_com, pontos_com, mensagem_com = analisar_comunicacao(comunicacao)
    status_bat, pontos_bat, mensagem_bat = analisar_bateria(bateria)
    status_oxi, pontos_oxi, mensagem_oxi = analisar_oxigenio(oxigenio)
    status_est, pontos_est, mensagem_est = analisar_estabilidade(estabilidade)

    print(f"Temperatura: {temperatura} °C | {status_temp} | {mensagem_temp}")
    print(f"Comunicação: {comunicacao}% | {status_com} | {mensagem_com}")
    print(f"Bateria: {bateria}% | {status_bat} | {mensagem_bat}")
    print(f"Oxigênio: {oxigenio}% | {status_oxi} | {mensagem_oxi}")
    print(f"Estabilidade: {estabilidade}% | {status_est} | {mensagem_est}")

    risco_total = (
        pontos_temp +
        pontos_com +
        pontos_bat +
        pontos_oxi +
        pontos_est
    )

    riscos_ciclos.append(risco_total)

    pontuacao_areas[0] += pontos_temp
    pontuacao_areas[1] += pontos_com
    pontuacao_areas[2] += pontos_bat
    pontuacao_areas[3] += pontos_oxi
    pontuacao_areas[4] += pontos_est

    classificacao = classificar_ciclo(risco_total)

    if classificacao == "MISSÃO CRÍTICA":
        quantidade_ciclos_criticos += 1

    recomendacao = gerar_recomendacao(classificacao)

    print(f"\nPontuação de risco do ciclo: {risco_total}")
    print(f"Classificação do ciclo: {classificacao}")
    print(f"Recomendação: {recomendacao}")


# ============================================================
# RELATÓRIO FINAL
# ============================================================

media_temperatura = total_temperatura / len(dados_missao)
media_comunicacao = total_comunicacao / len(dados_missao)
media_bateria = total_bateria / len(dados_missao)
media_oxigenio = total_oxigenio / len(dados_missao)
media_estabilidade = total_estabilidade / len(dados_missao)

maior_risco = max(riscos_ciclos)
ciclo_mais_critico = riscos_ciclos.index(maior_risco) + 1

risco_medio = sum(riscos_ciclos) / len(riscos_ciclos)

tendencia = analisar_tendencia(
    riscos_ciclos[0],
    riscos_ciclos[-1]
)

area_mais_afetada = identificar_area_mais_afetada(
    pontuacao_areas
)

classificacao_final = classificar_ciclo(round(risco_medio))


print("\n" + "=" * 60)
print("RELATÓRIO FINAL DA MISSÃO")
print("=" * 60)

print(f"Missão: {nome_missao}")
print(f"Equipe: {nome_equipe}")
print(f"Quantidade de ciclos analisados: {len(dados_missao)}")

print(f"\nMédia de temperatura: {media_temperatura:.2f} °C")
print(f"Média de comunicação: {media_comunicacao:.2f}%")
print(f"Média de bateria: {media_bateria:.2f}%")
print(f"Média de oxigênio: {media_oxigenio:.2f}%")
print(f"Média de estabilidade: {media_estabilidade:.2f}%")

print(f"\nCiclo mais crítico: Ciclo {ciclo_mais_critico}")
print(f"Maior pontuação de risco: {maior_risco}")
print(f"Risco médio da missão: {risco_medio:.2f}")

print(f"\nQuantidade de ciclos críticos: {quantidade_ciclos_criticos}")

print("\nTendência da missão:")
print(tendencia)

print("\nPontuação acumulada por área:")

for indice, area in enumerate(areas_monitoradas):
    print(f"{area}: {pontuacao_areas[indice]} pontos")

print(f"\nÁrea mais afetada:")
print(area_mais_afetada)

print(f"\nClassificação final da missão:")
print(classificacao_final)

print("\nConclusão:")

if classificacao_final == "MISSÃO ESTÁVEL":
    print("A missão permaneceu estável durante os ciclos analisados.")

elif classificacao_final == "MISSÃO EM ATENÇÃO":
    print("A missão apresentou instabilidade relevante durante a operação.")

else:
    print("A missão apresentou alto risco operacional e exige ações imediatas.")

print("=" * 60)
