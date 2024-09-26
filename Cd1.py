# Função para calcular o tempo de download
def calcular_tempo_download(tamanho_arquivo_mb, velocidade_internet_mbps):
    # Converte a velocidade de Mbps para MB/s (1 Mbps = 0.125 MB/s)
    velocidade_internet_mbs = velocidade_internet_mbps * 0.125
    # Calcula o tempo em segundos
    tempo_segundos = tamanho_arquivo_mb / velocidade_internet_mbs
    # Converte o tempo para minutos
    tempo_minutos = tempo_segundos / 60
    return tempo_minutos

# Solicita o tamanho do arquivo e a velocidade da internet ao usuário
tamanho_arquivo_mb = float(input("Digite o tamanho do arquivo para download (em MB): "))
velocidade_internet_mbps = float(input("Digite a velocidade do link de Internet (em Mbps): "))

# Calcula o tempo aproximado de download
tempo_download = calcular_tempo_download(tamanho_arquivo_mb, velocidade_internet_mbps)

# Exibe o resultado
print(f"O tempo aproximado de download é de {tempo_download:.2f} minutos.")
