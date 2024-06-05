from flask import Flask, flash, render_template, request, redirect
from random import randint
import time

app = Flask(__name__)

def bub_sort(arr):     # Function for Bubble Sort
    sort = arr[:]
    itime = time.time()
    for j in range(len(sort)):
        for l in range(len(sort)-j-1):
            if sort[l+1] < sort[l]:
                sort[l], sort[l+1] = sort[l+1], sort[l]
    ftime = time.time()
    extime = ftime - itime
    return sort,extime

def insert_sort_f(arr):     #Function for Insertion Sort
    sort = arr[:]
    itime = time.time()
    for n in range(1,len(sort)):
        k = sort[n]
        i = n
        while i > 0 and k < sort[i-1]:
            sort[i] = sort[i-1]
            i -= 1
        sort[i] = k
    ftime = time.time()
    extime = ftime - itime    
    return sort,extime

def msort(arr_l,arr_r):       #Function that Merge Sorts the left and right sub arrays
    
    sort = []
    r = 0
    l = 0
    while len(sort) < len(arr_r) + len(arr_l):
        if arr_l[l] <= arr_r[r]:
            sort.append(arr_l[l])
            l += 1
        else:
            sort.append(arr_r[r])
            r += 1 

        if len(arr_l)  == l:
            sort.extend(arr_r[r:]) 
            break        
        if len(arr_r)  == r:
            sort.extend(arr_l[l:]) 
            break

    return sort

def msort_f(arr):            #Function for Merge Sort

    if len(arr) < 2:
        return arr

    m = len(arr)//2
    
    r_arr = msort_f(arr[m:])
    l_arr = msort_f(arr[0:m])

    sort = msort(l_arr,r_arr)

    return sort

def hsort(sort, m, n):            #Function for heapifying the input
    max = n
    lnode_ = 2*n + 1
    rnode_ = 2*n + 2
    sort
    if lnode_ < m and sort[max] < sort[lnode_]:
        max = lnode_

    if rnode_ < m and sort[max] < sort[rnode_]:
        max = rnode_
    
    if max != n:
        sort[max], sort[n] =  sort[n], sort[max]
        hsort(sort, m, max)


def hsort_f(arr):                        #Function for Heap Sort
    sort = arr[:]
    i_t = time.time()
    alen_ = len(sort)

    for i in range(alen_//2 -1, -1, -1):
        hsort(sort,alen_, i )
    
    for i in range(alen_-1 , 0, -1):
        sort[0], sort[i] = sort[i] , sort[0]
        hsort(sort,i, 0 )
    f_t = time.time()
    ex_time = f_t - i_t
    return sort,ex_time

def qsort(sort,s,e):                #Function for Quick Sort partitioning using last element(pivot)
    a = s-1
    q = sort[e]
    for m in range(s,e,1):
        if sort[m] < q:
            a+=1
            sort[m], sort[a] = sort[a], sort[m]
    sort[e], sort[a+1] = sort[a+1], sort[e]
    return a+1


def qsort_f(sort,s,e):           #Function for Quick Sort
    
    if len(sort) == 1:
        return sort
    
    if s < e:
        pindex_ = qsort(sort,s,e)

        qsort_f(sort, s, pindex_-1)
        qsort_f(sort, pindex_+1, e)

def qsort_3(sort,s,e):            # 3 Median Quick Sort
    f_pivot = sort[s]
    mid_pivot = sort[e//2]
    l_pivot = sort[e]
    m_arr = [f_pivot,mid_pivot,l_pivot]
    m_arr.sort()
    median = m_arr[1]
    sort[s] = m_arr[0]
    sort[e] = m_arr[1]
    sort[e//2] = m_arr[2]


def qsort_3f(sort,s,e):         
    if s < e:
        qsort_3(sort,s,e)
        qsort_f(sort,s,e)


    

def select_sort(arr):
    sort = arr[:]
    itime = time.time()
    for m in range(0,len(sort)-1):
        min = m
        for n in range(m+1, len(sort)):
            if  sort[min] > sort[n]:
                min = n
        sort[min], sort[m] = sort[m], sort[min]
    ftime = time.time()
    extime = ftime - itime    
    return sort,extime

def random_arr(alen_):   #Generates random numbers
    a = []
    for m in range(0,alen_):
        a.append(randint(10,600))
    print(a)
    return a

# Home Route 
# To sort random input array and print sorted array and execution time
@app.route("/", methods=['GET','POST'])
@app.route("/home", methods=['GET','POST'])
def home_f():
    if request.method == 'POST':
        try:
            if 'alen_' in request.form:
                alen_ = int(request.form["alen_"])
                algo = request.form["algo"]
                arr = random_arr(alen_)
                if algo == "Mergesort":
                    itime = time.time()
                    sort = msort_f(arr)
                    ftime = time.time()
                    extime = ftime - itime
                    print("Merge sort = ",sort,extime)
                
                if algo == "Heapsort":
                    sort,extime = hsort_f(arr)
                    print("Heap sort = ",sort,extime)

                if algo == "Quicksort":
                    sort = arr[:]
                    itime = time.time()
                    qsort_f(sort,0,len(sort)-1)
                    ftime = time.time()
                    extime = ftime - itime
                    print("Quick sort = ",sort,extime)

                if algo == "Quicksort3":
                    sort = arr[:]
                    itime = time.time()
                    qsort_3f(sort,0,len(sort)-1)
                    ftime = time.time()
                    extime = ftime - itime
                    print("Quick sort 3med = ",sort,extime)

                if algo == "Insertionsort":
                    sort,extime = insert_sort_f(arr)
                    print("Insertion sort = ",sort,extime) 

                if algo == "Selectionsort":
                    sort,extime = select_sort(arr)
                    print("Selection sort = ",sort,extime) 

                if algo == "Bubblesort":
                    sort,extime = bub_sort(arr)
                    print("Bubble sort = ",sort,extime) 
                                   
                input_string = f"{arr}"
                time_string = f"{sorted}"
                return render_template('home.html', algo=algo, alen_=alen_, sort=sort, arr=arr, extime=extime*1000) 
                 
        except Exception as a:
            print(a,"Error has occured")
    
    return render_template('home.html')

# Compare Route 
# To compare execution time of all sorting alogorithms using Google Charts
@app.route("/compare", methods=['GET','POST'])
def comp_f():
    if request.method == 'POST':
        try:
            if 'alen_' in request.form:  
                
                alen_ = int(request.form["alen_"])
                arr = random_arr(alen_)
                data=[]

                i_time = time.perf_counter()
                sort = msort_f(arr)
                f_time = time.perf_counter()
                extime = f_time - i_time
                data.append(["Mergesort",extime*1000])

                sort,extime = hsort_f(arr)
                data.append(["Heapsort",extime*1000])

                sort = arr[:]
                itime = time.time()
                qsort_f(sort,0,len(sort)-1)
                ftime = time.time()
                extime = ftime - itime
                data.append(["Quicksort",extime*1000])

                sort = arr[:]
                itime = time.time()
                qsort_3f(sort,0,len(sort)-1)
                ftime = time.time()
                etime = ftime - itime
                data.append(["Quicksort 3median",extime*1000])

                sort,extime = insert_sort_f(arr)
                data.append(["Insertionsort",extime*1000])

                sort,extime = select_sort(arr)
                data.append(["Selectionsort",extime*1000])

                sort,extime = bub_sort(arr)
                data.append(["Bubblesort",extime*1000])
                # print(data)
                input = f"Length of Input array is {alen_}."
                return render_template('chart.html',data_for_chart=data,input_size_string=input)

        except Exception as e:
            print(e,"Error")
    return render_template('compare.html')        

if __name__ == '__main__':
    app.run(debug=True)

