from django.shortcuts import render_to_response
from article.models import Article
from django.http import HttpResponse
from forms import ArticleForm
from django.http import HttpResponseRedirect
from django.core.context_processors import csrf

def articles(request):
	language = 'en-gb'
	session_language = 'en-gb'
	if 'lang' in request.COOKIES:
		language = request.COOKIES['lang']

	if 'lang' in request.session:
		session_language = request.session['lang']
	#
	args = {}
	args.update(csrf(request))
	args['articles'] = Article.objects.all()
	args['language'] = language
	args['session_language'] = session_language

	return render_to_response('articles.html', args)
	#

def article (request, article_id=1):
	return render_to_response('article.html',
								{'article': Article.objects.get(id=article_id)	})	

def language(request, language='en-gb'):
		response = HttpResponse("setting language to %s" % language)
		response.set_cookie('lang', language)
		request.session['lang'] = language
		return response

def create(request):
	#if POST has info, then create article dictionary
	if request.POST:
		form = ArticleForm(request.POST, request.FILES) #to show where files come from
		if form.is_valid():
			form.save()
			return HttpResponseRedirect('/articles/all')

	else:
		form = ArticleForm()
		args = {}
		args.update(csrf(request))
		args['form'] = form # pop form into args
		return render_to_response('create_article.html', args)

def like_article(request, article_id):
	if article_id:
		a = Article.objects.get(id=article_id) #get article that matches id
		a.likes = a.likes+1
		a.save()
	return HttpResponseRedirect('/articles/get/%s' % article_id)

# def add_comment(request, article_id):
# 	a = Article.objects.get(id=article_id)

# 	if request.method == "POST":
# 		f = CommentForm(request.POST)
# 		if f.is_valid():
# 			c = f.save(commit=False)
# 			c.pub_date = timezone.now()
# 			c.article = a
# 			c.save()
# 			return HttpResponseRedirect('/articles/get/%s' %article_id)

# 		else:
# 			f = CommentForm()

# 		args = {}
# 		args.update(csrf(request))
# 		args['article'] = a
# 		args['form'] = f	
# 		return render_to_response('add_comment.html', args)	

def search_titles(request):
	if request.method == "POST":
		search_text = request.POST['search_text']
	else:
		search_text = ''
		#filter by title__contains method by search text that we pass in
		#CHECK for more filters
	articles = Article.objects.filter(tags__contains=search_text) 
	if articles != None:
		if search_text != '' and search_text != ' ' and len(search_text) > 2:
			return render_to_response('ajax_search.html', {'articles' : articles})
		else:
			return render_to_response('ajax_search.html', None)

# def ajax_search(request):
#     if request.method == 'POST':
#         search_text = request.POST['search_text']
#         if search_text > '':
#             articles = Article.objects.filter(tags__contains=search_text)
#         else:
#             articles = Article.objects.none()
#             text = 1
#     else:
#         search_text = ''
#     return render(request, "ajax_search.html", {'articles' : articles})
