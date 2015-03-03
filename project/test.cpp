#include <iostream>
#include <cstdlib>
using namespace std;

int main(int argc, char* argv[]) {
  int val[2];
  for(int i = 1; i < argc; i++) { // retrieve the value from php
      val[i-1] = atoi(argv[i]);
  }
  int total = val[0] - val[1]; // sum up
  std::cout << total;  // std::cout will output to php
  return 0;
}
