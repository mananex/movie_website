from django.shortcuts import render

# render 404 error 
def error_404(request, exception):
	return render(request, 'error_404/index.html', status = 404)
