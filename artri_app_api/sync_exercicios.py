import csv
import os
import django

# Configura o ambiente do Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'artri_app_api.settings')
django.setup()

from authentication.models import Exercise

# Mapeamento para o ENUM do Django
diff_map = {
    'Iniciante': 'Easy',
    'Intermediário': 'Medium',
    'Avançado': 'Hard'
}

def sync_exercises(csv_path):
    print("Iniciando sincronização inteligente de exercícios...")
    
    with open(csv_path, mode='r', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        atualizados = 0
        criados = 0

        for row in reader:
            clean_name = row['Exercício'].strip()
            diff_pt = row['Dificuldade'].strip()
            
            # Limpeza de dados
            link = row['Link do Vídeo'].strip()
            obs = row['Instruções / Observações'].strip()
            if 'Mesmo' in link or 'Mesmo' in obs:
                link = '' # Remove links inválidos copiados de tabelas textuais
                
            db_difficulty = diff_map.get(diff_pt, 'Easy')

            # Tática Ninja: Recriar o nome antigo para dar o "match" no banco atual
            legacy_name = f"{clean_name} - {diff_pt.upper()}"
            
            # Busca pelo nome antigo com sufixo
            exercise = Exercise.objects.filter(name=legacy_name).first()
            
            if not exercise:
                # Se não achar o antigo, tenta achar pelo nome limpo + dificuldade 
                # (útil caso você rode esse script mais de uma vez)
                exercise = Exercise.objects.filter(name=clean_name, difficulty=db_difficulty).first()

            if exercise:
                # ATUALIZA MANTENDO O ID (Não quebra os treinos)
                exercise.name = clean_name # Remove o sufixo "- INICIANTE" do banco
                exercise.sets_reps = row.get('Séries / Repetições', '').strip()
                exercise.rest_time = row.get('Descanso', '').strip()
                exercise.description = obs
                exercise.tutorial_link = link
                exercise.difficulty = db_difficulty
                exercise.save()
                atualizados += 1
            else:
                # Se realmente não existir, cria um novo
                Exercise.objects.create(
                    name=clean_name,
                    sets_reps=row.get('Séries / Repetições', '').strip(),
                    rest_time=row.get('Descanso', '').strip(),
                    description=obs,
                    tutorial_link=link,
                    difficulty=db_difficulty
                )
                criados += 1
                
    print(f"Sucesso! {atualizados} atualizados (relações mantidas) e {criados} novos criados.")

if __name__ == '__main__':
    # Certifique-se de que o nome do arquivo bate exatamente
    sync_exercises('Exercicios.csv')