class FieldIndexError(IndexError):
    """Выбрасывается, если выбрано значение вне поля."""

    def __init__(
        self,
        # Текст по умолчанию.
        message='Введено значение за границами игрового поля!'  
    ):
        super().__init__(message)  