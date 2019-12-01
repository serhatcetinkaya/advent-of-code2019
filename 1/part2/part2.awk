#!/usr/bin/awk -f
BEGIN{
  sum = 0
}
{
  tmp = (int($1 / 3) - 2)
  while (tmp > 0) {
    sum += tmp
    tmp = (int(tmp / 3) - 2)
  }
}
END{
  print "SUM:\t" sum
}
