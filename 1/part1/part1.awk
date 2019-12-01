#!/usr/bin/awk -f
BEGIN{
  sum = 0
}
{
  sum += (int($1 / 3) - 2)
}
END{
  print "SUM:\t" sum
}
