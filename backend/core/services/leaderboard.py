from datetime import timedelta
from django.utils.timezone import now
from django.db.models import Sum, Case, When, IntegerField
from core.models import Like

def get_leaderboard():
    since = now() - timedelta(hours=24)

    return (
        Like.objects
        .filter(created_at__gte=since)
        .values("user__username")
        .annotate(
            karma=Sum(
                Case(
                    When(post__isnull=False, then=5),
                    When(comment__isnull=False, then=1),
                    output_field=IntegerField(),
                )
            )
        )
        .order_by("-karma")[:5]
    )
