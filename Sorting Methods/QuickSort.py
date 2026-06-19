# lomoto Partation

def lomoto_Partation(arr,low,high):
    pivot=arr(high)
    i=low-1

    for j in range(low,high):
        if arr(j)<=pivot:
            i+=1

            arr[i],arr[j]=arr[j],arr[i]
            arr[i+1],arr[high]=arr[high],arr[i+1]
            return i+1

            arr=[70,60,80.40,30]
            pos=lomoto_Partation(arr,0,len(arr)-1)

            print("Array after position",pos)
            print("Sorted Array:",arr)


            # Quick sort
            def quick_sort(arr,low,high):
                if low<high:
                    pi=Partation(arr,low,high)

                    quick_sort(arr,low,pi-1)
                    quick_sort(arr,pi+1,high)

                    arr=[70,60,80.40,30]
                    quick_sort(arr,0,len(arr)-1)

                    print("Sorted Array:",arr)