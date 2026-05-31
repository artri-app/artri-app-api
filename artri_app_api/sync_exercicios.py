import csv
import os
import django

# Configura o ambiente do Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'artri_app_api.settings')
django.setup()

from authentication.models import Exercise

# Mapeamento expandido para aceitar os novos termos que você usou na planilha
diff_map = {
    'INICIANTE': 'Easy',
    'FÁCIL': 'Easy',
    'FACIL': 'Easy',
    'INTERMEDIÁRIO': 'Medium',
    'INTERMEDIARIO': 'Medium',
    'MÉDIO': 'Medium',
    'AVANÇADO': 'Hard',
    'AVANCADO': 'Hard',
    'DIFÍCIL': 'Hard',
    'DIFICIL': 'Hard',
}

def sync_exercises(csv_path):
    print("Iniciando sincronização inteligente de exercícios...")
    
    # utf-8-sig remove caracteres invisíveis (BOM) que o Excel coloca no início de arquivos CSV
    with open(csv_path, mode='r', encoding='utf-8-sig') as file:
        reader = csv.DictReader(file)
        
        # Remove espaços sobrando no começo ou fim dos nomes das colunas
        reader.fieldnames = [str(field).strip() for field in reader.fieldnames if field]
        
        atualizados = 0
        criados = 0

        for row in reader:
            # Limpa chaves e valores para evitar erros de digitação (ex: " Dificil " vira "Dificil")
            clean_row = {str(k).strip(): str(v).strip() for k, v in row.items() if k is not None}
            
            # Pula linhas completamente vazias
            if not clean_row.get('Nome do exercício'):
                continue

            clean_name = clean_row['Nome do exercício']
            diff_pt = clean_row.get('Dificuldade', 'Fácil').upper()
            
            link = clean_row.get('Link do vídeo', '')
            obs = clean_row.get('Instruções/Observações', '')
            sets = clean_row.get('Séries e Repetições', '')
            rest = clean_row.get('Descanso', '')

            # Remove links genéricos/inválidos que vieram da tabela
            if 'Mesmo' in link or 'Mesmo' in obs:
                link = '' 
                
            db_difficulty = diff_map.get(diff_pt, 'Easy')

            # Tática: O banco antigo usava " - INICIANTE". A planilha nova usa "Fácil".
            # Vamos traduzir para o termo antigo para conseguir achar o ID correto no banco.
            legacy_diff = "INICIANTE"
            if db_difficulty == "Medium": legacy_diff = "INTERMEDIÁRIO"
            if db_difficulty == "Hard": legacy_diff = "AVANÇADO"
            
            # Tenta encontrar o exercício com as nomenclaturas antigas ou já limpas
            exercise = Exercise.objects.filter(name=f"{clean_name} - {legacy_diff}").first()
            if not exercise:
                exercise = Exercise.objects.filter(name=f"{clean_name} - {legacy_diff.upper()}").first()
            if not exercise:
                exercise = Exercise.objects.filter(name=clean_name).first()

            if exercise:
                # ATUALIZA MANTENDO O ID
                exercise.name = clean_name # Salva o nome limpo de vez
                exercise.sets_reps = sets
                exercise.rest_time = rest
                exercise.description = obs
                exercise.tutorial_link = link
                exercise.difficulty = db_difficulty
                exercise.save()
                atualizados += 1
            else:
                # Se não achar nada parecido, cria um novo
                Exercise.objects.create(
                    name=clean_name,
                    sets_reps=sets,
                    rest_time=rest,
                    description=obs,
                    tutorial_link=link,
                    difficulty=db_difficulty
                )
                criados += 1
                
    print(f"Sucesso! {atualizados} atualizados (relações mantidas) e {criados} novos criados.")

if __name__ == '__main__':
    sync_exercises('Exercicios.csv')