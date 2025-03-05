from flask import Flask, render_template, redirect, url_for
import datetime
import locale 

app = Flask(__name__)

frequentantes = [
    {"nome": "Anny de Oyá", "status": False},
    {"nome": "Bruna de Oxum", "status": False},
    {"nome": "Ingrid de Oyá", "status": False},
    {"nome": "Aline de Omolu", "status": False},
    {"nome": "Gabriela de Yemanjá", "status": False},
    {"nome": "Ricardo de Oxóssi", "status": False},
    {"nome": "Beatriz de Xangô", "status": False},
    {"nome": "Carlos de Xangô", "status": False},
    {"nome": "Jhonatan de Oxóssi", "status": False},
    {"nome": "Beatriz de Oxum", "status": False}
]

meses_em_portugues = {
    1: 'Janeiro', 2: 'Fevereiro', 3: 'Março', 4: 'Abril', 5: 'Maio', 6: 'Junho',
    7: 'Julho', 8: 'Agosto', 9: 'Setembro', 10: 'Outubro', 11: 'Novembro', 12: 'Dezembro'
}

@app.route('/')
def index():
    hoje = datetime.datetime.now()
    mes_atual = meses_em_portugues[hoje.month]  

    # Passar o mês atual para o template
    return render_template('index.html', frequentantes=frequentantes, mes_atual=mes_atual)

@app.route('/marcar_pago/<nome>')
def marcar_pago(nome):
    # Marca o frequentante como "Pago"
    for frequentante in frequentantes:
        if frequentante["nome"] == nome:
            frequentante["status"] = True
            break
    return redirect(url_for('index'))

@app.route('/marcar_nao_pago/<nome>')
def marcar_nao_pago(nome):
    # Marca o frequentante como "Não Pago"
    for frequentante in frequentantes:
        if frequentante["nome"] == nome:
            frequentante["status"] = False
            break
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
