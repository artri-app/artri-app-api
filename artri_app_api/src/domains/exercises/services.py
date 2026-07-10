from .repositories import ExerciseRepository


class ExerciseService:
    @staticmethod
    def list_filtered(query_params):
        # Fluxo de exercícios personalizados: só exercícios com categoria definida.
        if query_params.get('personalized') in ('true', 'True', '1'):
            queryset = ExerciseRepository.with_category()
        else:
            queryset = ExerciseRepository.all()

        category = query_params.get('category')
        if category:
            queryset = ExerciseRepository.filter_by_category(queryset, category)

        difficulty = query_params.get('difficulty')
        if difficulty:
            queryset = ExerciseRepository.filter_by_difficulty(queryset, difficulty)

        return queryset
