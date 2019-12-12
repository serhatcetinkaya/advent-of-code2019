#!/usr/bin/awk -f
BEGIN{
  numZeros = 0
  numOnes = 0
  numTwos = 0
  minZeros = 150
  result = 0
}
{
  split($0, chars, "")
  for (i=1; i <= length($0); i += 150) {
    numZeros = 0
    numOnes = 0
    numTwos = 0
    for (j=0; j < 150; j++) {
      if (chars[i+j] == "0") {
        numZeros++
      }
      if (chars[i+j] == "1") {
        numOnes++
      }
      if (chars[i+j] == "2") {
        numTwos++
      }
    }
    if (numZeros < minZeros) {
      minZeros = numZeros
      result = numOnes * numTwos
    }
  }
}
END{
  printf("Result:\t%d", result)
}
