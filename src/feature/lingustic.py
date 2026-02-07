"""
Лингвистический анализ — изучение языковых средств: фонетика, морфология, синтаксис, лексика. 
Сюда же относится стилистический анализ (определение стиля речи — научный, публицистический, художественный и т.д.).
"""
from pydantic import Field, BaseModel
from typing import Literal

class LinguseticAnalysisResult(BaseModel):
    text_type: Literal['Деловой документ', 'Ху']