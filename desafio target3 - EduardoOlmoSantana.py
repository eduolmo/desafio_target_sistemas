import datetime

def calcular_juros(valor,data):
    hoje = datetime.date.today()
    juros = 0.0
    if hoje >= data:
        diferenca = hoje - data
        dias_atraso = diferenca.days
        juros = valor * 0.025 * dias_atraso

    return juros
    
if __name__ == "__main__":
    valor = float(input("Digite o valor do produto: "))
    repetir = True
    while repetir:
        data = input("Digite a data de vencimento (dd/mm/aaaa): ")
        data = datetime.datetime.strptime(data, "%d/%m/%Y").date()
        if data >= datetime.date.today():
            print("Data inválida. A data de vencimento não pode ser maior ou igual que a data atual.")
        else:
            repetir = False
    valor_final = valor + calcular_juros(valor,data)
    print(f"O valor do produto com juros é: {valor_final:.2f}")
