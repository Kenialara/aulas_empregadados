from pathlib import Path

src = Path(r"C:/Users/conta/aulas_empregadados/aula_1_banco_de_dados/data/csv")

files = ["patients.csv", "encounters.csv", "conditions.csv"]

for f in files:
    path = src / f
    print("Convertendo:", path)
    
    # Lê qualquer byte (Latin-1 aceita tudo!)
    text = path.read_text(encoding="latin1")
    
    # Regrava como UTF-8 puro
    path.write_text(text, encoding="utf-8")

print("CONCLUÍDO — arquivos agora são UTF-8 REAL.")
