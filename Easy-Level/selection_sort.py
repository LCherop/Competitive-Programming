class Solution: 
    def select(self, arr, i):
        # code here 
        return arr[i]
    
    def selectionSort(self, arr,n):
        #code here
        for i in range(n-1):
            mini=i
            for j in range(i+1,n):
                if arr[j]<arr[mini]:
                    mini=j
                    
            x,arr[i]=arr[i],arr[mini]
            arr[mini]=x
            
        return arr
