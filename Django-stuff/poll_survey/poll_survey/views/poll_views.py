from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_protect
from django.template.defaultfilters import slugify
from django.core.urlresolvers import reverse
from poll_survey.models import UserProfile, Poll_Post, Comments
from django.http import HttpResponse

@login_required
@csrf_protect
def get_posts_auth_user(request):
	if request.method == 'GET':
		logged_user = request.user
		poll_objects = Poll_Post.objects.filter(posted_by=logged_user).values('slug_post', 'poll_post')
		return render(request, 'user_polls.html', {'polls': poll_objects}) 
	elif request.method == 'POST':
		email_addr = request.user.email_addr
		try:
			logged_user = UserProfile.objects.get(email_addr=email_addr)
		except UserProfile.MultipleObjectsReturned as ex:
			print ex
		try:
			poll_post_obj = Poll_Post.objects.order_by('-poll_id')[0]
			poll_id = poll_post_obj.poll_id + 1
		except:
			poll_id = 1
		poll_post = request.POST.get('post_poll_area')
		posted_by = request.user
		slug_post = slugify(poll_post)

		post_obj = Poll_Post(poll_id=poll_id, poll_post=poll_post)
		post_obj.posted_by = posted_by
		post_obj.slug_post = slug_post
		post_obj.save()

@login_required
def get_details_polls(request, slug=None):
	if request.method == 'GET':
		poll_question_obj = Poll_Post.objects.get(slug_post=slug)
		poll_question = poll_question_obj.poll_post
		try:
			required_key = request.session['commented_posts']
		except KeyError:
			request.session['commented_posts'] = ['dummy']
		comments = Comments.objects.filter(post_id=poll_question_obj).order_by('-comment_id').\
		values('comment', 'commented_date')
		comments_set = Comments.objects.filter(post_id=poll_question_obj).order_by('-comment_id')
		#print comments
		commented_by_list, list_authors = [], []
		list_comments = list(comments)
		#print 'dict is: ', list_comments
		for c in comments_set:
			full_name = c.commented_by.firstname + ' ' +c.commented_by.lastname
			list_authors.append({'commented_by': full_name})
		for i in xrange(0, len(list_comments)):
			list_comments[i].update(list_authors[i])
		print list_comments
		#last = dict(dict(comments).items() + dict(commented_by_list).items())
		#print last
		#print comments.userprofile_set
		return render(request, 'details_poll.html', {'poll_post': poll_question, 'slug': slug, 'comments': list_comments})

@login_required
@csrf_protect
def comment_post(request, slug=None):
	if request.method == 'POST':
		commented_posts_list = request.session.get('commented_posts')
		commented_posts_list.append(slug)
		request.session['commented_posts'] = commented_posts_list
		#request.session.save()
		comment = request.POST.get('comment_area')
		commented_by = request.user
		post_obj = Poll_Post.objects.get(slug_post=slug)
		try:
			comment_obj = Comments.objects.order_by('-comment_id')[0]
			comment_id = comment_obj.comment_id + 1
		except:
			comment_id = 1
		#print comment, commented_by, post_obj, comment_id
		comment_obj = Comments(comment_id=comment_id, comment=comment)
		comment_obj.commented_by = commented_by
		comment_obj.post_id = post_obj
		comment_obj.save()
		return redirect(reverse('Get Details', kwargs = {'slug': slug}))

def list_polls_comments(request):
	if request.method == 'GET':
		list_polls = []
		list_slugs = []
		list_polls_slugs = []
		polls = Poll_Post.objects.all().order_by('-poll_id')
		for poll in polls:
			comments_dict = {}
			#print '============================================'
			#print poll.comments_set.values()
			poll_post = poll.poll_post
			slug_post = poll.slug_post
			comment_entire = []
			comment_date = []
			commented_by = []
			list_polls.append(poll_post)
			list_slugs.append(slug_post)
		for i in range(0, len(list_polls)):
			dict_inter = {}
			dict_inter['poll'] = list_polls[i]
			dict_inter['slug'] = list_slugs[i]
			list_polls_slugs.append(dict_inter)
		return render(request, 'home.html', {'polls': list_polls_slugs})


