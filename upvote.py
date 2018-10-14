@login_required(login_url='/accounts/')
def upvote(request, ans_id):
    submission = get_object_or_404(Submission, pk=ans_id)
    sub_topic = submission.topic.id
    person = request.user
    vte = person.student.vote_id
    if Vote.objects.filter(submit_id=ans_id,voter_id=request.user.id):
        if request.method == 'POST':
            if vte == 'DM':
                submission.dem_votes -= 1
                submission.save(update_fields=['dem_votes'])
                v = Vote.objects.get(submit_id=submission.id,voter_id=request.user.id)
                v.delete()
                messages.error(request, "Your vote has been removed from the Democrat tally.")
            elif vte == 'LP':
                submission.libp_votes -= 1
                submission.save(update_fields=['libp_votes'])
                v = Vote.objects.get(submit_id=submission.id,voter_id=request.user.id)
                v.delete()
                messages.error(request, "Your vote has been removed from the Libertarian(party) tally.")
            elif vte == 'RP':
                submission.gop_votes -= 1
                submission.save(update_fields=['gop_votes'])
                v = Vote.objects.get(submit_id=submission.id,voter_id=request.user.id)
                v.delete()
                messages.error(request, "Your vote has been removed from the Republican tally.")
            elif vte == 'CL':
                submission.left_votes -= 1
                submission.save(update_fields=['left_votes'])
                v = Vote.objects.get(submit_id=submission.id,voter_id=request.user.id)
                v.delete()
                messages.error(request, "Your vote has been removed from the center-left tally.")
            elif vte == 'CR':
                submission.right_votes -= 1
                submission.save(update_fields=['right_votes'])
                v = Vote.objects.get(submit_id=submission.id,voter_id=request.user.id)
                v.delete()
                messages.error(request, "Your vote has been removed from the center-right tally.")
            elif vte == 'FL':
                submission.fl_votes -= 1
                submission.save(update_fields=['fl_votes'])
                v = Vote.objects.get(submit_id=submission.id,voter_id=request.user.id)
                v.delete()
                messages.error(request, "Your vote has been removed from the far-leftt tally.")
            elif vte == 'FR':
                submission.fr_votes -= 1
                submission.save(update_fields=['fr_votes'])
                v = Vote.objects.get(submit_id=submission.id,voter_id=request.user.id)
                v.delete()
                messages.error(request, "Your vote has been removed from the far-right tally.")
            elif vte == 'LI':
                submission.libr_votes -= 1
                submission.save(update_fields=['libr_votes'])
                v = Vote.objects.get(submit_id=submission.id,voter_id=request.user.id)
                v.delete()
                messages.error(request, "Your vote has been removed from the libertarian(ideology) tally.")
            elif vte == 'SD':
                submission.sd_votes -= 1
                submission.save(update_fields=['sd_votes'])
                v = Vote.objects.get(submit_id=submission.id,voter_id=request.user.id)
                v.delete()
                messages.error(request, "Your vote has been removed from the Social Democrat tally.")
            else:
                messages.error(request, "Something happened when removing your upvote!")
                return redirect('/debates/' + str(sub_topic))
            return redirect('/debates/' + str(sub_topic))
        else:
            messages.error(request, "You shouldn't try to do stuff without a POST request...")
            return redirect('/debates/' + str(sub_topic))
    else:
        if request.method == 'POST':
            if vte == 'DM':
                submission.dem_votes += 1```

                ```submission.save(update_fields=['dem_votes'])
                Vote.objects.create(submit_id=submission.id,voter_id=request.user.id)
            elif vte == 'LP':
                submission.libp_votes += 1
                submission.save(update_fields=['libp_votes'])
                Vote.objects.create(submit_id=submission.id,voter_id=request.user.id)
            elif vte == 'RP':
                submission.gop_votes += 1
                submission.save(update_fields=['gop_votes'])
                Vote.objects.create(submit_id=submission.id,voter_id=request.user.id)
            elif vte == 'CL':
                submission.left_votes += 1
                submission.save(update_fields=['left_votes'])
                Vote.objects.create(submit_id=submission.id,voter_id=request.user.id)
            elif vte == 'CR':
                submission.right_votes += 1
                submission.save(update_fields=['right_votes'])
                Vote.objects.create(submit_id=submission.id,voter_id=request.user.id)
            elif vte == 'FL':
                submission.fl_votes += 1
                submission.save(update_fields=['fl_votes'])
                Vote.objects.create(submit_id=submission.id,voter_id=request.user.id)
            elif vte == 'FR':
                submission.fr_votes += 1
                submission.save(update_fields=['fr_votes'])
                Vote.objects.create(submit_id=submission.id,voter_id=request.user.id)
            elif vte == 'LI':
                submission.libr_votes += 1
                submission.save(update_fields=['libr_votes'])
                Vote.objects.create(submit_id=submission.id,voter_id=request.user.id)
            elif vte == 'SD':
                submission.sd_votes += 1
                submission.save(update_fields=['sd_votes'])
                Vote.objects.create(submit_id=submission.id,voter_id=request.user.id)
            else:
                messages.error(request, "You must select a political id to vote. Please follow the red 'Vote ID' link to choose.")
                return redirect('/debates/' + str(sub_topic))
            return redirect('/debates/' + str(sub_topic))
        else:
            return redirect('/debates/' + str(sub_topic))