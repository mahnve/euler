#include <stdio.h>

int multipleOf3Or5(int i) {
  if( i%3 == 0 || i%5 == 0) {
    return 0;
  } else {
    return -1;
  }
}

int sum(int x) 
{
  int summa = 0;
  int i;
  for (i=1; i<x; i++) {
    if (multipleOf3Or5(i) == 0)
      summa += i;
  }
  return summa;
}

int main(void) 
{
  int summa = sum(1000);
  printf("%d", summa);
  return 0;
}
