dicionario = {}
dicionario["P0000"] = {
    "Descrição" : "Acesso aos Parâmetros",
    "Faixa de Valores" : "0 a 999",
    "Ajuste de Fábrica" : 0,
    "Ajuste do Usuário" : "",
    "Propr." : "",
    "Grupos" : "",
    "Pág." : "5-2",
}

dicionario["P0001"] = {
    "Descrição" : "Referência Velocidade",
    "Faixa de Valores" : "0 a 65535",
    "Ajuste de Fábrica" : "",
    "Ajuste do Usuário" : "",
    "Propr." : "ro",
    "Grupos" : "READ",
    "Pág." : "17-1",
}

dicionario["P0002"] = {
    "Descrição" : "Velocidade de Saída (Motor)",
    "Faixa de Valores" : "0 a 65535",
    "Ajuste de Fábrica" : "",
    "Ajuste do Usuário" : "",
    "Propr." : "ro",
    "Grupos" : "READ",
    "Pág." : "17-1",
}

dicionario["P0003"] = {
    "Descrição" : "Corrente do Motor",
    "Faixa de Valores" : "0,0 a 200,0 A",
    "Ajuste de Fábrica" : "",
    "Ajuste do Usuário" : "",
    "Propr." : "ro",
    "Grupos" : "READ",
    "Pág." : "17-1",
}

dicionario["P0004"] = {
    "Descrição" : "Tensão Barram. CC (Ud)",
    "Faixa de Valores" : "0 a 2000V",
    "Ajuste de Fábrica" : "",
    "Ajuste do Usuário" : "",
    "Propr." : "ro",
    "Grupos" : "READ",
    "Pág." : "17-1",
}

dicionario["P0005"] = {
    "Descrição" : "Frequência de Saída (Motor)",
    "Faixa de Valores" : "0,0 a 500,0 Hz",
    "Ajuste de Fábrica" : "",
    "Ajuste do Usuário" : "",
    "Propr." : "ro",
    "Grupos" : "READ",
    "Pág." : "17-2",
}

dicionario["P0006"] = {
    "Descrição" : "Estado do Inversor",
    "Faixa de Valores" : "0 = Ready\n1 = Run\n2 = Subtensão\n3 = Falha\n4 = Autoajuste\n5 = Configuração\n6 = Frenagem CC\n7 = Estado Dormir",
    "Ajuste de Fábrica" : "",
    "Ajuste do Usuário" : "",
    "Propr." : "ro",
    "Grupos" : "READ",
    "Pág." : "17-2",
}

dicionario["P0007"] = {
    "Descrição" : "Tensão de Saída",
    "Faixa de Valores" : "0 a 2000 V",
    "Ajuste de Fábrica" : "",
    "Ajuste do Usuário" : "",
    "Propr." : "ro",
    "Grupos" : "READ",
    "Pág." : "17-3",
}

dicionario["P0009"] = {
    "Descrição" : "Torque do Motor",
    "Faixa de Valores" : "-1000,0 a 1000,0 %",
    "Ajuste de Fábrica" : "",
    "Ajuste do Usuário" : "",
    "Propr." : "ro",
    "Grupos" : "READ",
    "Pág." : "17-3",
}

dicionario["P0010"] = {
    "Descrição" : "Potência de Saída",
    "Faixa de Valores" : "0,0 a 6553,5 kW",
    "Ajuste de Fábrica" : "",
    "Ajuste do Usuário" : "",
    "Propr." : "ro",
    "Grupos" : "READ",
    "Pág." : "17-4",
}

dicionario["P0011"] = {
    "Descrição" : "Fator de Potência",
    "Faixa de Valores" : "-1,00 a 1,00",
    "Ajuste de Fábrica" : "",
    "Ajuste do Usuário" : "",
    "Propr." : "ro",
    "Grupos" : "READ",
    "Pág." : "17-4",
}

for key, value in dicionario.items():
    print(key, '->', value)