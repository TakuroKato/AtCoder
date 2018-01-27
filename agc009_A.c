#include<stdio.h>
int main(){
  int n,k,i;
  scanf("%d",&n);
  int a[n],b[n];
  for (i=0; i<n ;i++) {
    scanf("%d %d",&a[i],&b[i]);
  }
  int count = 0;
  for (i=0; i<n; i++) {
    while(1){
      if (a[n-1-i]%b[n-1-i] == 0) {
	break;
      } else {
	for (k=0;k<n-i;k++){
	  a[k]++;
	}
	count++;
      }
    }
  }
  printf("%d\n",count);
  return 0;
}
