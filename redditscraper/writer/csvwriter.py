def write(ls, output_file):
    """ write a post list to a csv """
    pass


def _convert_post_to_line_list(ps):
    ret = []

    for p in ps:
        ret.append(_convert_post_line(p))

    return ret


def _convert_post_line(p):
   ret = []

   ret.append(str(p.pid))
   ret.append(str(p.title))
   ret.append(str(p.up))
   ret.append(str(p.down))
   ret.append(str(p.domain))
   ret.append(str(p.created.isoformat()))

   ret.append(str(p.author))
   ret.append(str(p.author_link_karma))
   ret.append(str(p.author_comment_karma))
   ret.append(str(p.author_account_created_date.isoformat()))


   return ",".join(ret)
