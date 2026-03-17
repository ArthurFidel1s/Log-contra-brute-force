import json

def analisar_logs(caminho_arquivo):

    with open(caminho_arquivo, 'r', encoding='utf-8') as file:

        log = {}
        suspeitos = []
        
        for line in file:
            ip, status = line.strip().split(' - ')
            
            if ip not in log:
                log[ip] = {
                    "tentativas": 0,
                    "sucesso": 0,
                    "taxa de falhas": 0.0
                    } 
            
            if status == 'LOGIN FAILED':
                log[ip]['tentativas'] += 1
            elif status == 'LOGIN SUCCESS':
                log[ip]['sucesso'] += 1
        
        # Calcular taxa de falhas e marcar suspeitos após contar todas as tentativas/sucessos
        for ip, info in log.items():
            total = info['tentativas'] + info['sucesso']
            info['taxa de falhas'] = (info['tentativas'] / total * 100) if total > 0 else 0.0

            if info['tentativas'] > 2 and info['taxa de falhas'] > 40.0:
                suspeitos.append({
                    "IP" : ip,
                    "Falhas": info['tentativas'],
                    "Sucesso": info['sucesso'],
                    "Taxa de Falhas": f"{info['taxa de falhas']:.2f}%",
                    "Classificação": "Suspeito" if info['taxa de falhas'] > 60.0 else "Suspeito Leve",
                    "Risco": "Crítico" if info['taxa de falhas'] > 80.0 else "Alto" if info['taxa de falhas'] > 60.0 else "Médio" if info['taxa de falhas'] > 40.0 else "Baixo"
                })
            
        
        if not log:
            print("Nenhum IP encontrado no arquivo.")
            exit(0)

        # ranking = sorted(log, key=lambda x: log[x]['tentativas'], reverse=True)
    
        relatorio = {
            "suspeitos": suspeitos
        }

        with open('01 - ips_suspeitos.json', 'w', encoding='utf-8') as out:
            json.dump(relatorio, out, ensure_ascii=False, indent=2)

        print("Relatório salvo em 01 - ips_suspeitos.json")

    return relatorio
    
if __name__ == "__main__":
    caminho_arquivo = '01 - logs.txt'
    analisar_logs(caminho_arquivo)