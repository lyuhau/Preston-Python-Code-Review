@login_required(login_url='/accounts/')
def upvote(request, ans_id):
    submission = get_object_or_404(Submission, pk=ans_id)
    sub_topic = submission.topic.id
    person = request.user
    vte = person.student.vote_id
    if Vote.objects.filter(submit_id=ans_id,voter_id=request.user.id):
        if request.method == 'POST':
            if vte == 'DM':
                submission_key = 'dem_votes'
                name = 'Democrat'
            elif vte == 'LP':
                submission_key = 'libp_votes'
                name = 'Libertarian(party)'
            elif vte == 'RP':
                submission_key = 'gop_votes'
                name = 'Republican'
            elif vte == 'CL':
                submission_key = 'left_votes'
                name = 'center-left'
            elif vte == 'CR':
                submission_key = 'right_votes'
                name = 'center-right'
            elif vte == 'FL':
                submission_key = 'fl_votes'
                name = 'far-left'
            elif vte == 'FR':
                submission_key = 'fr_votes'
                name = 'far-right'
            elif vte == 'LI':
                submission_key = 'libr_votes'
                name = 'libertarian(ideology)'
            elif vte == 'SD':
                submission_key = 'sd_votes'
                name = 'Social Democrat'
            else:
                messages.error(request, "Something happened when removing your upvote!")
                return redirect('/debates/' + str(sub_topic))

            submission.__dict__[submission_key] -= 1
            submission.save(update_fields=[submission_key])
            v = Vote.objects.get(submit_id=submission.id,voter_id=request.user.id)
            v.delete()
            messages.error(request, f"Your vote has been removed from the {name} tally.")
            return redirect('/debates/' + str(sub_topic))
        else:
            messages.error(request, "You shouldn't try to do stuff without a POST request...")
            return redirect('/debates/' + str(sub_topic))
    else:
        if request.method == 'POST':
            if vte == 'DM':
                submission_key = 'dem_votes'
                name = 'Democrat'
            elif vte == 'LP':
                submission_key = 'libp_votes'
                name = 'Libertarian(party)'
            elif vte == 'RP':
                submission_key = 'gop_votes'
                name = 'Republican'
            elif vte == 'CL':
                submission_key = 'left_votes'
                name = 'center-left'
            elif vte == 'CR':
                submission_key = 'right_votes'
                name = 'center-right'
            elif vte == 'FL':
                submission_key = 'fl_votes'
                name = 'far-left'
            elif vte == 'FR':
                submission_key = 'fr_votes'
                name = 'far-right'
            elif vte == 'LI':
                submission_key = 'libr_votes'
                name = 'libertarian(ideology)'
            elif vte == 'SD':
                submission_key = 'sd_votes'
                name = 'Social Democrat'
            else:
                messages.error(request, "You must select a political id to vote. Please follow the red 'Vote ID' link to choose.")
                return redirect('/debates/' + str(sub_topic))

            submission.__dict__[submission_key] += 1
            submission.save(update_fields=[submission_key])
            Vote.objects.create(submit_id=submission.id,voter_id=request.user.id)
            return redirect('/debates/' + str(sub_topic))
        else:
            return redirect('/debates/' + str(sub_topic))