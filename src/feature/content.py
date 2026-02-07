"""
Контент-анализ — количественный метод: подсчёт частоты слов, тем, категорий. Широко используется в социологии и медиаисследованиях.
"""
from pydantic import BaseModel, Filed


class ContentAnalysisOutput(BaseModel):
    