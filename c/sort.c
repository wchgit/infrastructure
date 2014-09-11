#include<stdio.h>
#include<stdlib.h>

void swap(int *a, int *b){
  int tmp=*a;
  *a = *b;
  *b = tmp;
}

void show(int A[], int len){
  int i;
  printf("[ ");
  for(i=0;i<len;i++){
    printf("%d ",A[i]);
  }
  printf("]\n");
}

int partition(int A[], int low, int high){
  int pivot = A[low];
  int i=low,j=high+1;
  while(1){
    while(A[++i]<pivot);
    while(A[--j]>pivot);
    if(i<j)
      swap(&A[i], &A[j]);
    else
      break;
  }
  swap(&A[low], &A[j]);
  return j;
}

void quick_sort(int A[], int low, int high){
  if(low>=high)
    return;
  int i = partition(A, low, high);
  quick_sort(A, low, i-1);
  quick_sort(A, i+1, high);
}

void heap_adjust(int A[], int low, int high){
  int i;
  for(i=2*low+1; i<=high; low=i,i=2*low+1){
    if(i<high && A[i]<A[i+1])
      i++;
    if(A[low]<A[i])
      swap(&A[low], &A[i]);
    else
      break;
  }
}

void heap_sort(int A[], int low, int high){
  int i;
  int N=high-low+1;
  for(i=N/2; i>=0; --i){
    heap_adjust(A, i, high);
  }

  for(i=high; i>0; --i){
    swap(&A[0], &A[i]);
    heap_adjust(A, 0, i-1);
  }
}

void merge(int A[], int low, int mid, int high){
  int tmp[mid-low+1];
  int i,j,k;
  for(i=0; i<=mid-low; i++)
    tmp[i]=A[low+i];
  i=0;
  j=mid+1;
  k=low;
  while(i<=mid-low && j<=high)
    A[k++] = tmp[i]<A[j]?tmp[i++]:A[j++];
  while(i<=mid-low)
    A[k++] = tmp[i++];
}

void merge_sort(int A[], int low, int high){
  if(low>=high)
    return;
  int mid=(low+high)/2;
  merge_sort(A, low, mid);
  merge_sort(A, mid+1, high);
  merge(A, low, mid, high);
}

int main(){
  int A[]={3,1,4,1,5,9,2,6};
  //quick_sort(A, 0, 7);
  //heap_sort(A, 0, 7);
  merge_sort(A, 0, 7);
  show(A,8);
  return 0;
}
