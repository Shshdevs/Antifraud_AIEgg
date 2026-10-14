from app.domain.entities.dashboard import DashboardSummary
from app.domain.repositories.dashboard import DashboardRepository
from app.infrastructure.services.dashboard import DashboardService


class DashboardRepositoryAdapter(DashboardRepository):
    def __init__(self, service: DashboardService) -> None:
        self._service = service

    def get_summary(self) -> DashboardSummary:
        return self._service.get_summary()
