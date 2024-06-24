from django.shortcuts import render,redirect

# Create your views here.
def inicio(request):
    return render(request, 'inicio.html') 

def es_primo(request,a=0,b=100):
    primos = []
    if a > b:
        return redirect('primos', a=b, b=a)    
    for i in range(a,b+1):
        contador = 0
        for j in range(1,i+1):
            if i % j == 0:
                contador += 1
        if contador == 2:
            primos.append(i)

    return render(request,'primos.html',{'primos':primos,'a':a,'b':b})