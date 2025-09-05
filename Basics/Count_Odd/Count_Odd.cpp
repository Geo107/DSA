#include <iostream>
 int main(){
  int high,low,count=0;
  std::cout<<"Enter the Lowest number";
  std::cin>> low;
  std::cout<<"Enter the Highest number";
  std::cin>> high;
  //My Approach and Solved Solution T(n)=O(n)
  for(int i=low;i<=high;i++){
    if(i%2==1){
      count+=1;
    }
  }
  return count;
  //Better Approach is this
  if(low%2==0)low+=1;
  if(high%2==0)high-=1;
  return(((high-low)/2)+1);
}
