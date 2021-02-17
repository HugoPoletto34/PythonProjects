import pandas as pd

tabela_vendas = pd.read_excel('/home/hugo-poletto/JavaStudies/PythonProjects/Vendas.xlsx')
#print(tabela_vendas)
pd.d
tabela_faturamento = tabela_vendas[["ID Loja", "Valor Final"]]\
    .groupby('ID Loja')\
    .sum()\
    .sort_values(by='Valor Final', ascending=True)

#print(tabela_faturamento)

tabela_quantidade = tabela_vendas[["ID Loja", "Quantidade"]]\
    .groupby('ID Loja')\
    .sum()\
    .sort_values(by='Quantidade', ascending=True)
#print(tabela_quantidade)

ticket_medio = (tabela_faturamento['Valor Final'] / tabela_quantidade['Quantidade']).to_frame()
#print(ticket_medio)
def enviar_email(nome_loja, tabela):
    import smtplib
    import email.message

    server = smtplib.SMTP('smtp.gmail.com:587')
    corpo_email = "Corpo do E-mail"

    msg = email.message.Message()
    msg['Subject'] = "Assunto do E-mail"

    # Fazer antes (apenas na 1ª vez): Ativar Aplicativos não Seguros.
    # Gerenciar Conta Google -> Segurança -> Aplicativos não Seguros -> Habilitar
    # Caso mesmo assim dê o erro: smtplib.SMTPAuthenticationError: (534,
    # Você faz o login no seu e-mail e depois entra em: https://accounts.google.com/DisplayUnlockCaptcha
    msg['From'] = 'remetente@gmail.com'
    msg['To'] = 'destinatario@gmail.com'
    password = "senha"
    msg.add_header('Content-Type', 'text/html')
    msg.set_payload(corpo_email)

    s = smtplib.SMTP('smtp.gmail.com: 587')
    s.starttls()
    # Login Credentials for sending the mail
    s.login(msg['From'], password)
    s.sendmail(msg['From'], [msg['To']], msg.as_string().encode('utf-8'))
    print('Email enviado')