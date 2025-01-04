from django.shortcuts import render,HttpResponse

def index(request):
    context = {
        'title' : 'Atomic',
        'heading':'Welcome to Atomic',
        'subheading':'this my atomic',
        'banner':'url("http://127.0.0.1:8000/static/img/BocchiTheRock.png");',
        'fontColor':'#FB4141',
        'page':'home'
    }
    return render(request,'index.html',context)

# ini adalah contoh view yang menerima parameter question_id dari urls.py kemudian mengembalikan response berupa string yang berisi question_id tersebut.
# biasanya digunakan untuk menampilkan hasil dari suatu pertanyaan yang telah dijawab oleh user. 
# contoh: /
# http:// 
# seperti contoh di atas, jika user mengakses http://127.0.0.1:8000/5/results/ maka akan menampilkan hasil dari pertanyaan dengan id 5. 
def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)