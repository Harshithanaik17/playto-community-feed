def build_comment_tree(comments):
    comment_map = {c.id: c for c in comments}
    roots = []

    for c in comments:
        c.children_list = []

    for c in comments:
        if c.parent_id:
            comment_map[c.parent_id].children_list.append(c)
        else:
            roots.append(c)

    return roots
