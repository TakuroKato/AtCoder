#include <stdio.h>
long gcd(a,b){
  if (b == 0){
    return a;
  } else {
    return gcd(b,a % b);
  }
}
long lcm(a,b){
  return a * b / gcd(a,b)
}
int main(void){

}
