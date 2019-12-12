#!/usr/bin/awk -f
BEGIN{
  for (k=0; k < 150; k++) {
    decoded[k] = "2"
  }
}
{
  split($0, chars, "")
  for (i=1; i <= length($0); i += 150) {
    for (j=0; j < 150; j++) {
      if (decoded[j] == "2") {
        decoded[j] = chars[i+j]
      }
    }
  }
}
END{
  printf("Result: ")
  for (n=0; n < 150; n++) {
    if (n % 25 == 0) {
      printf("\n")
    }
    if (decoded[n] == "0") {
      printf("-")
    }
    if (decoded[n] == "1") {
      printf("X")
    }
  }
  printf("\n")
}
