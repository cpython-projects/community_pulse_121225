from app.models import Statistics
from app.schemas import *


class QuestionCreateRequest(QuestionCreate):
    pass


class QuestionUpdateRequest(QuestionUpdate):
    pass

class QuestionResponse(QuestionRead):
    pass


class QuestionDetailResponse(QuestionRead):
    statistics: StatisticsRead | None = None


class QuestionListResponse(QuestionRead):
    pass