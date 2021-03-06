@login_required(login_url='/accounts/')
def upvote(request, ans_id):
    submission = get_object_or_404(Submission, pk=ans_id)
    sub_topic = submission.topic.id

    if request.method != 'POST':
        messages.error(request, "You shouldn't try to do stuff without a POST request...")
        return redirect(f'/debates/{str(sub_topic)}')

    vote_type_map = {
        'DM': { 'key': 'dem_votes',   'name': 'Democrat' },
        'LP': { 'key': 'libp_votes',  'name': 'Libertarian(party)' },
        'RP': { 'key': 'gop_votes',   'name': 'Republican' },
        'CL': { 'key': 'left_votes',  'name': 'center-left' },
        'CR': { 'key': 'right_votes', 'name': 'center-right' },
        'FL': { 'key': 'fl_votes',    'name': 'far-left' },
        'FR': { 'key': 'fr_votes',    'name': 'far-right' },
        'LI': { 'key': 'libr_votes',  'name': 'libertarian(ideology)' },
        'SD': { 'key': 'sd_votes',    'name': 'Social Democrat' }
    }
    vote_type = request.user.student.vote_id
    try:
        key = vote_type_map[vote_type]['key']
        name = vote_type_map[vote_type]['name']
    except NameError:
        messages.error(request, 'Something happened when removing your upvote!')
        messages.error(request, "You must select a political id to vote. Please follow the red 'Vote ID' link to choose.")
        return redirect(f'/debates/{str(sub_topic)}')

    user_id = request.user.id
    if Vote.objects.filter(submit_id=ans_id, voter_id=user_id):
        submission.__dict__[key] -= 1
        submission.save(update_fields=[key])
        Vote.objects.get(submit_id=submission.id, voter_id=user_id).delete()
        messages.error(request, f'Your vote has been removed from the {name} tally.')
    else:
        submission.__dict__[key] += 1
        submission.save(update_fields=[key])
        Vote.objects.create(submit_id=submission.id, voter_id=user_id)

    return redirect(f'/debates/{str(sub_topic)}')