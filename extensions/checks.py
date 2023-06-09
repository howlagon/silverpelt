import lightbulb


@lightbulb.Check
def techhelp_only(ctx: lightbulb.Context) -> bool:
    techhelp_ids = [
        1095535502007996447,
        1095535779159232534
    ]

    for role in ctx.member.get_roles():
        if role.id in techhelp_ids:
            return True
    return False
