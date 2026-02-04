## The Tree
I modeled nested comments using a self-referential approach.

Each comment belongs to a post and can optionally have a parent comment.
This allows comments to reply to other comments and form a nested structure.

All comments for a post are fetched in a single query.
The nested comment tree is then built in Python instead of querying the database multiple times.
This avoids unnecessary database queries.

---------------------------------------------------------------------------------------------------

## The Math
The leaderboard shows users based on karma earned in the last 24 hours.

Rules used:
- Like on a post = 5 karma
- Like on a comment = 1 karma

Karma is calculated dynamically from the Like table using a time-based filter.

Query used:

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

