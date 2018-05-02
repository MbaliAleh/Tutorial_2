

"Mbali Tut2"
"30 April 2018"

import numpy
import pylab
from numpy.fft import fft,ifft

#Question (1 and 2 )
def corrG(x,y): #defining the correlation funnction
    assert(x.size==y.size) # the vectors of the same size
    ft1 = fft(x)
    ft2 = fft(y)
    ft2conj=numpy.conj(ft2)
    return numpy.real(ifft(ft1*ft2conj))
 
 #Question 3 function              
def shift(x,n=0):#defining a function
    vec=0*x  
    vec[n]=1
    vecft=fft(vec)
    xft=fft(x)
    return numpy.real(ifft(xft*vecft))


#Question 4 function
def circConv(x,y): #defining a function
    assert(x.size==y.size) # the vectors of the same size
    xx=numpy.zeros(2*x.size)
    xx[0:x.size]=x

    yy=numpy.zeros(2*y.size)
    yy[0:y.size]=y
    xxft=fft(xx)
    yyft=fft(yy)
    vec=numpy.real(ifft(xxft*yyft))
    return vec[0:x.size]

#The gaussian function 
def mygauss(x):
    y=numpy.exp(-0.5*x**2/2**2)#sigma = 2
    return y


if __name__=='__main__':

    x=numpy.arange(-15,15,0.1)
    y=mygauss(x)
    
    #Question 1 results
    yshift = shift(y,100)
    pylab.plot(x,y)
    pylab.plot(x,yshift)
    pylab.show()  
    
    #Question 2 results
    ycorr=corrG(y,y)
    pylab.plot(x,ycorr,'r--')
    pylab.show()
    
   #Question 3 results    
    ycorr=corrG(y,y)
    yshift=shift(y,y.size/4)
    yshiftcorr=corrG(yshift,yshift)
    meanerr=numpy.mean(numpy.abs(ycorr-yshiftcorr))
    print 'The mean difference between the two correlation functions is ' + repr(meanerr)
    pylab.plot(x,ycorr)
    pylab.plot(x,yshiftcorr,'g--')        
    pylab.show()       
    
   # Question  4 results
    y=y/y.sum()
    yconv=circConv(y,y)
    pylab.plot(x,y)
    pylab.plot(x,yconv)
    pylab.show()